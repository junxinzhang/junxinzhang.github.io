#!/bin/bash
#
# 图片压缩脚本 - 保持分辨率不变，大幅减小文件体积
# Image Compression Script - Maintain resolution, reduce file size
#
# 策略:
#   1. 将所有 PNG/JPG 超过阈值的文件转为 WebP（压缩率最高）
#   2. 已有 WebP 文件如果过大，重新以更低质量压缩
#   3. 更新 Markdown 文件中的图片引用（png/jpg → webp）
#   4. 备份原文件到 .backup 目录
#
# 用法:
#   ./scripts/compress-images.sh              # 预览模式（dry-run）
#   ./scripts/compress-images.sh --run        # 实际执行
#   ./scripts/compress-images.sh --run --no-backup  # 执行且不备份
#
# 依赖: cwebp (brew install webp), sips (macOS 自带)
#

set -e

# ===== 配置 =====
IMAGE_DIR="assets/images"
BACKUP_DIR="assets/images/.backup"
SIZE_THRESHOLD=$((500 * 1024))         # 500KB - 超过此大小的文件才处理
WEBP_QUALITY=82                        # WebP 质量 (0-100)，82 是质量与大小的最佳平衡点
WEBP_RECOMPRESS_QUALITY=78             # 对已有过大 WebP 的重压缩质量
LARGE_WEBP_THRESHOLD=$((1500 * 1024))  # 1.5MB - WebP 超过此大小则重新压缩

# ===== 参数解析 =====
DRY_RUN=true
DO_BACKUP=true
UPDATE_REFS=true

for arg in "$@"; do
    case $arg in
        --run)       DRY_RUN=false ;;
        --no-backup) DO_BACKUP=false ;;
        --no-refs)   UPDATE_REFS=false ;;
    esac
done

# ===== 颜色 =====
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# ===== 工具检测 =====
if ! command -v cwebp &>/dev/null; then
    echo -e "${RED}错误: cwebp 未安装。请运行: brew install webp${NC}"
    exit 1
fi

# ===== 工具函数 =====
get_size() {
    stat -f%z "$1" 2>/dev/null || stat -c%s "$1" 2>/dev/null
}

format_size() {
    local size=$1
    if [ $size -gt 1048576 ]; then
        printf "%.1fMB" $(echo "scale=1; $size / 1048576" | bc)
    elif [ $size -gt 1024 ]; then
        printf "%.0fKB" $(echo "scale=0; $size / 1024" | bc)
    else
        echo "${size}B"
    fi
}

get_dimensions() {
    sips -g pixelWidth -g pixelHeight "$1" 2>/dev/null | awk '/pixel/ {print $2}' | tr '\n' 'x' | sed 's/x$//'
}

# ===== 统计变量 =====
TOTAL_ORIGINAL=0
TOTAL_AFTER=0
FILES_WOULD_CONVERT=0
FILES_WOULD_RECOMPRESS=0
FILES_SKIPPED=0
REFS_TO_UPDATE=0

echo ""
echo -e "${BOLD}╔══════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║     📸 图片压缩脚本 - Image Compressor      ║${NC}"
echo -e "${BOLD}╚══════════════════════════════════════════════╝${NC}"
echo ""

if [ "$DRY_RUN" = true ]; then
    echo -e "${CYAN}[预览模式] 不会修改任何文件，仅显示将会发生的变更${NC}"
    echo -e "${CYAN}使用 --run 参数来实际执行压缩${NC}"
else
    echo -e "${YELLOW}[执行模式] 将实际压缩文件！${NC}"
fi
echo ""

# ===== 收集需要处理的文件 =====
declare -a FILES_TO_CONVERT=()    # PNG/JPG → WebP
declare -a FILES_TO_RECOMPRESS=() # 过大的 WebP 重新压缩
declare -a REF_UPDATES=()         # 需要更新的引用 (原文件名)

# 1) 扫描大 PNG/JPG 文件
while IFS= read -r file; do
    size=$(get_size "$file")
    if [ $size -gt $SIZE_THRESHOLD ]; then
        webp_file="${file%.*}.webp"
        if [ -f "$webp_file" ]; then
            webp_size=$(get_size "$webp_file")
            if [ $webp_size -lt $size ]; then
                # WebP 版本已存在且更小，只需要删除原文件/更新引用
                FILES_SKIPPED=$((FILES_SKIPPED + 1))
                continue
            fi
        fi
        FILES_TO_CONVERT+=("$file")
    fi
done < <(find "$IMAGE_DIR" -type f \( -name "*.png" -o -name "*.PNG" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.JPG" -o -name "*.JPEG" \) | sort)

# 2) 扫描过大的 WebP 文件
while IFS= read -r file; do
    size=$(get_size "$file")
    if [ $size -gt $LARGE_WEBP_THRESHOLD ]; then
        FILES_TO_RECOMPRESS+=("$file")
    fi
done < <(find "$IMAGE_DIR" -type f -name "*.webp" | sort)

# ===== 显示转换计划 =====
echo -e "${BOLD}━━━ PNG/JPG → WebP 转换 ━━━${NC}"
echo ""

if [ ${#FILES_TO_CONVERT[@]} -eq 0 ]; then
    echo -e "  ${GREEN}✓ 没有需要转换的 PNG/JPG 文件${NC}"
else
    echo -e "  找到 ${BOLD}${#FILES_TO_CONVERT[@]}${NC} 个文件需要转换:"
    echo ""
    printf "  %-65s %10s %10s %12s\n" "文件名" "当前大小" "分辨率" "预估压缩后"
    echo "  $(printf '─%.0s' {1..100})"
    
    for file in "${FILES_TO_CONVERT[@]}"; do
        size=$(get_size "$file")
        dims=$(get_dimensions "$file")
        TOTAL_ORIGINAL=$((TOTAL_ORIGINAL + size))
        
        # 预估 WebP 大小（PNG → WebP 通常压缩到 15-25%）
        ext="${file##*.}"
        if [[ "$ext" =~ ^[Pp][Nn][Gg]$ ]]; then
            est_size=$((size * 20 / 100))  # PNG → WebP ~20%
        else
            est_size=$((size * 50 / 100))  # JPG → WebP ~50%
        fi
        TOTAL_AFTER=$((TOTAL_AFTER + est_size))
        FILES_WOULD_CONVERT=$((FILES_WOULD_CONVERT + 1))
        
        basename=$(basename "$file")
        printf "  %-65s %10s %10s %12s\n" "$basename" "$(format_size $size)" "$dims" "~$(format_size $est_size)"
    done
fi

echo ""
echo -e "${BOLD}━━━ 过大 WebP 重新压缩 ━━━${NC}"
echo ""

if [ ${#FILES_TO_RECOMPRESS[@]} -eq 0 ]; then
    echo -e "  ${GREEN}✓ 没有过大的 WebP 文件需要重新压缩${NC}"
else
    echo -e "  找到 ${BOLD}${#FILES_TO_RECOMPRESS[@]}${NC} 个 WebP 文件需要重新压缩 (>$(format_size $LARGE_WEBP_THRESHOLD)):"
    echo ""
    printf "  %-65s %10s %10s %12s\n" "文件名" "当前大小" "分辨率" "预估压缩后"
    echo "  $(printf '─%.0s' {1..100})"
    
    for file in "${FILES_TO_RECOMPRESS[@]}"; do
        size=$(get_size "$file")
        dims=$(get_dimensions "$file")
        est_size=$((size * 60 / 100))  # 重新压缩 ~60%
        TOTAL_ORIGINAL=$((TOTAL_ORIGINAL + size))
        TOTAL_AFTER=$((TOTAL_AFTER + est_size))
        FILES_WOULD_RECOMPRESS=$((FILES_WOULD_RECOMPRESS + 1))
        
        basename=$(basename "$file")
        printf "  %-65s %10s %10s %12s\n" "$basename" "$(format_size $size)" "$dims" "~$(format_size $est_size)"
    done
fi

# ===== 统计摘要 =====
echo ""
echo -e "${BOLD}━━━ 预估摘要 ━━━${NC}"
echo ""
TOTAL_FILES=$((FILES_WOULD_CONVERT + FILES_WOULD_RECOMPRESS))
echo -e "  待处理文件:      ${BOLD}${TOTAL_FILES}${NC} 个"
echo -e "  ├ PNG/JPG → WebP: ${FILES_WOULD_CONVERT} 个"
echo -e "  └ WebP 重压缩:    ${FILES_WOULD_RECOMPRESS} 个"
echo -e "  跳过(已优化):     ${FILES_SKIPPED} 个"
echo ""
if [ $TOTAL_ORIGINAL -gt 0 ]; then
    SAVINGS=$((TOTAL_ORIGINAL - TOTAL_AFTER))
    PERCENT=$((SAVINGS * 100 / TOTAL_ORIGINAL))
    echo -e "  原始总大小:  $(format_size $TOTAL_ORIGINAL)"
    echo -e "  预估压缩后:  ${GREEN}$(format_size $TOTAL_AFTER)${NC}"
    echo -e "  预估节省:    ${GREEN}$(format_size $SAVINGS) (~${PERCENT}%)${NC}"
fi

# ===== 实际执行 =====
if [ "$DRY_RUN" = true ]; then
    echo ""
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${CYAN}  这是预览模式。要实际执行压缩，请运行:${NC}"
    echo -e "${CYAN}  ./scripts/compress-images.sh --run${NC}"
    echo -e "${CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    exit 0
fi

# === 执行模式 ===
echo ""
echo -e "${YELLOW}开始压缩...${NC}"
echo ""

# 创建备份目录
if [ "$DO_BACKUP" = true ]; then
    mkdir -p "$BACKUP_DIR"
    echo -e "  📁 备份目录: ${BACKUP_DIR}"
fi

ACTUAL_SAVED=0
ACTUAL_PROCESSED=0

# 处理 PNG/JPG → WebP
for file in "${FILES_TO_CONVERT[@]}"; do
    size_before=$(get_size "$file")
    webp_file="${file%.*}.webp"
    basename=$(basename "$file")
    
    echo -ne "  压缩 ${basename} ... "
    
    # 备份原文件
    if [ "$DO_BACKUP" = true ]; then
        cp "$file" "$BACKUP_DIR/"
    fi
    
    # 转换为 WebP
    cwebp -q $WEBP_QUALITY "$file" -o "$webp_file" -quiet 2>/dev/null
    
    if [ -f "$webp_file" ]; then
        size_after=$(get_size "$webp_file")
        saved=$((size_before - size_after))
        ACTUAL_SAVED=$((ACTUAL_SAVED + saved))
        ACTUAL_PROCESSED=$((ACTUAL_PROCESSED + 1))
        
        echo -e "${GREEN}$(format_size $size_before) → $(format_size $size_after) (节省 $(format_size $saved))${NC}"
        
        # 删除原始 PNG/JPG
        rm "$file"
    else
        echo -e "${RED}失败${NC}"
    fi
done

# 处理过大 WebP 重新压缩
for file in "${FILES_TO_RECOMPRESS[@]}"; do
    size_before=$(get_size "$file")
    basename=$(basename "$file")
    tmp_file="${file}.tmp"
    
    echo -ne "  重压缩 ${basename} ... "
    
    # 备份
    if [ "$DO_BACKUP" = true ]; then
        cp "$file" "$BACKUP_DIR/"
    fi
    
    # 先解码再重新编码（用更低的质量）
    dwebp "$file" -o "${file}.png" -quiet 2>/dev/null
    if [ -f "${file}.png" ]; then
        cwebp -q $WEBP_RECOMPRESS_QUALITY "${file}.png" -o "$tmp_file" -quiet 2>/dev/null
        rm "${file}.png"
        
        if [ -f "$tmp_file" ]; then
            size_after=$(get_size "$tmp_file")
            if [ $size_after -lt $size_before ]; then
                mv "$tmp_file" "$file"
                saved=$((size_before - size_after))
                ACTUAL_SAVED=$((ACTUAL_SAVED + saved))
                ACTUAL_PROCESSED=$((ACTUAL_PROCESSED + 1))
                echo -e "${GREEN}$(format_size $size_before) → $(format_size $size_after) (节省 $(format_size $saved))${NC}"
            else
                rm "$tmp_file"
                echo -e "${YELLOW}已跳过（重压缩后更大）${NC}"
            fi
        else
            echo -e "${RED}失败${NC}"
        fi
    else
        echo -e "${RED}解码失败${NC}"
    fi
done

# ===== 更新 Markdown 引用 =====
if [ "$UPDATE_REFS" = true ] && [ ${#FILES_TO_CONVERT[@]} -gt 0 ]; then
    echo ""
    echo -e "${BOLD}━━━ 更新 Markdown 文件中的图片引用 ━━━${NC}"
    echo ""
    
    for file in "${FILES_TO_CONVERT[@]}"; do
        # 获取不带扩展名的基础名
        base_path="${file%.*}"
        ext="${file##*.}"
        
        # 在 _posts 目录中查找引用
        ref_pattern=$(basename "$file")
        webp_ref="$(basename "$base_path").webp"
        
        # 查找并替换引用
        grep -rl "$ref_pattern" _posts/ 2>/dev/null | while read md_file; do
            sed -i '' "s|${ref_pattern}|${webp_ref}|g" "$md_file"
            echo -e "  ${GREEN}✓${NC} ${md_file}: ${ref_pattern} → ${webp_ref}"
            REFS_TO_UPDATE=$((REFS_TO_UPDATE + 1))
        done
    done
fi

# ===== 最终报告 =====
echo ""
echo -e "${BOLD}╔══════════════════════════════════════════════╗${NC}"
echo -e "${BOLD}║          ✅ 压缩完成！                       ║${NC}"
echo -e "${BOLD}╚══════════════════════════════════════════════╝${NC}"
echo ""
echo -e "  处理文件数:  ${BOLD}${ACTUAL_PROCESSED}${NC}"
echo -e "  总节省空间:  ${GREEN}${BOLD}$(format_size $ACTUAL_SAVED)${NC}"
if [ "$DO_BACKUP" = true ]; then
    echo -e "  备份位置:    ${BACKUP_DIR}/"
    echo ""
    echo -e "  ${YELLOW}确认无误后可删除备份: rm -rf ${BACKUP_DIR}${NC}"
fi
echo ""

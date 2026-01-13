#!/bin/bash
#
# Image Optimization Script for Jekyll Blog
# 图片优化脚本 - 压缩 PNG/JPG 并生成 WebP 版本
#
# Usage: ./scripts/optimize-images.sh [directory]
# Default directory: assets/images
#
# Requirements:
#   - imagemagick (convert command)
#   - cwebp (for WebP conversion)
#   - optipng (for PNG optimization)
#   - jpegoptim (for JPEG optimization)
#
# Install on macOS:
#   brew install imagemagick webp optipng jpegoptim
#
# Install on Ubuntu/Debian:
#   sudo apt-get install imagemagick webp optipng jpegoptim

set -e

# Configuration
MAX_WIDTH=1920
QUALITY_WEBP=85
QUALITY_JPEG=85
SIZE_THRESHOLD=200000  # 200KB - files larger than this will be compressed

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default directory
IMAGE_DIR="${1:-assets/images}"

# Check if directory exists
if [ ! -d "$IMAGE_DIR" ]; then
    echo -e "${RED}Error: Directory $IMAGE_DIR does not exist${NC}"
    exit 1
fi

# Check for required tools
check_tool() {
    if ! command -v "$1" &> /dev/null; then
        echo -e "${YELLOW}Warning: $1 is not installed. Some optimizations will be skipped.${NC}"
        return 1
    fi
    return 0
}

echo "======================================"
echo "  Image Optimization Script"
echo "  图片优化脚本"
echo "======================================"
echo ""
echo "Target directory: $IMAGE_DIR"
echo ""

# Check available tools
HAS_CONVERT=$(check_tool "convert" && echo 1 || echo 0)
HAS_CWEBP=$(check_tool "cwebp" && echo 1 || echo 0)
HAS_OPTIPNG=$(check_tool "optipng" && echo 1 || echo 0)
HAS_JPEGOPTIM=$(check_tool "jpegoptim" && echo 1 || echo 0)

echo ""

# Stats
TOTAL_ORIGINAL=0
TOTAL_OPTIMIZED=0
FILES_PROCESSED=0
WEBP_CREATED=0

# Function to get file size
get_size() {
    stat -f%z "$1" 2>/dev/null || stat -c%s "$1" 2>/dev/null
}

# Function to format size
format_size() {
    local size=$1
    if [ $size -gt 1048576 ]; then
        echo "$(echo "scale=2; $size / 1048576" | bc)MB"
    elif [ $size -gt 1024 ]; then
        echo "$(echo "scale=2; $size / 1024" | bc)KB"
    else
        echo "${size}B"
    fi
}

# Process PNG files
process_png() {
    local file="$1"
    local size_before=$(get_size "$file")
    TOTAL_ORIGINAL=$((TOTAL_ORIGINAL + size_before))

    echo -e "Processing: ${file}"
    echo -e "  Original size: $(format_size $size_before)"

    # Optimize PNG
    if [ "$HAS_OPTIPNG" = "1" ] && [ $size_before -gt $SIZE_THRESHOLD ]; then
        optipng -o2 -quiet "$file"
    fi

    # Resize if too large
    if [ "$HAS_CONVERT" = "1" ]; then
        local width=$(identify -format "%w" "$file" 2>/dev/null || echo 0)
        if [ "$width" -gt "$MAX_WIDTH" ]; then
            convert "$file" -resize "${MAX_WIDTH}x>" "$file"
            echo -e "  ${YELLOW}Resized to max width: ${MAX_WIDTH}px${NC}"
        fi
    fi

    # Create WebP version
    local webp_file="${file%.*}.webp"
    if [ "$HAS_CWEBP" = "1" ] && [ ! -f "$webp_file" ]; then
        cwebp -q $QUALITY_WEBP "$file" -o "$webp_file" 2>/dev/null
        if [ -f "$webp_file" ]; then
            WEBP_CREATED=$((WEBP_CREATED + 1))
            echo -e "  ${GREEN}Created WebP: $(format_size $(get_size "$webp_file"))${NC}"
        fi
    fi

    local size_after=$(get_size "$file")
    TOTAL_OPTIMIZED=$((TOTAL_OPTIMIZED + size_after))
    FILES_PROCESSED=$((FILES_PROCESSED + 1))

    if [ $size_before -gt $size_after ]; then
        local saved=$((size_before - size_after))
        echo -e "  ${GREEN}Optimized: $(format_size $size_after) (saved $(format_size $saved))${NC}"
    else
        echo -e "  Final size: $(format_size $size_after)"
    fi
    echo ""
}

# Process JPEG files
process_jpeg() {
    local file="$1"
    local size_before=$(get_size "$file")
    TOTAL_ORIGINAL=$((TOTAL_ORIGINAL + size_before))

    echo -e "Processing: ${file}"
    echo -e "  Original size: $(format_size $size_before)"

    # Resize if too large
    if [ "$HAS_CONVERT" = "1" ]; then
        local width=$(identify -format "%w" "$file" 2>/dev/null || echo 0)
        if [ "$width" -gt "$MAX_WIDTH" ]; then
            convert "$file" -resize "${MAX_WIDTH}x>" -quality $QUALITY_JPEG "$file"
            echo -e "  ${YELLOW}Resized to max width: ${MAX_WIDTH}px${NC}"
        fi
    fi

    # Optimize JPEG
    if [ "$HAS_JPEGOPTIM" = "1" ] && [ $size_before -gt $SIZE_THRESHOLD ]; then
        jpegoptim --max=$QUALITY_JPEG --strip-all --quiet "$file"
    fi

    # Create WebP version
    local webp_file="${file%.*}.webp"
    if [ "$HAS_CWEBP" = "1" ] && [ ! -f "$webp_file" ]; then
        cwebp -q $QUALITY_WEBP "$file" -o "$webp_file" 2>/dev/null
        if [ -f "$webp_file" ]; then
            WEBP_CREATED=$((WEBP_CREATED + 1))
            echo -e "  ${GREEN}Created WebP: $(format_size $(get_size "$webp_file"))${NC}"
        fi
    fi

    local size_after=$(get_size "$file")
    TOTAL_OPTIMIZED=$((TOTAL_OPTIMIZED + size_after))
    FILES_PROCESSED=$((FILES_PROCESSED + 1))

    if [ $size_before -gt $size_after ]; then
        local saved=$((size_before - size_after))
        echo -e "  ${GREEN}Optimized: $(format_size $size_after) (saved $(format_size $saved))${NC}"
    else
        echo -e "  Final size: $(format_size $size_after)"
    fi
    echo ""
}

# Find and process large images (> SIZE_THRESHOLD)
echo "Looking for images larger than $(format_size $SIZE_THRESHOLD)..."
echo ""

# Process PNG files
find "$IMAGE_DIR" -type f \( -name "*.png" -o -name "*.PNG" \) -size +${SIZE_THRESHOLD}c | while read file; do
    process_png "$file"
done

# Process JPEG files
find "$IMAGE_DIR" -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.JPG" -o -name "*.JPEG" \) -size +${SIZE_THRESHOLD}c | while read file; do
    process_jpeg "$file"
done

# Summary
echo "======================================"
echo "  Optimization Complete!"
echo "======================================"
echo ""
echo "Files processed: $FILES_PROCESSED"
echo "WebP files created: $WEBP_CREATED"
if [ $TOTAL_ORIGINAL -gt 0 ]; then
    echo "Total original size: $(format_size $TOTAL_ORIGINAL)"
    echo "Total optimized size: $(format_size $TOTAL_OPTIMIZED)"
    if [ $TOTAL_ORIGINAL -gt $TOTAL_OPTIMIZED ]; then
        local total_saved=$((TOTAL_ORIGINAL - TOTAL_OPTIMIZED))
        local percent=$((total_saved * 100 / TOTAL_ORIGINAL))
        echo -e "${GREEN}Total saved: $(format_size $total_saved) ($percent%)${NC}"
    fi
fi
echo ""
echo "Tips:"
echo "  - Run this script before committing new images"
echo "  - Consider using an online service like TinyPNG for further compression"
echo "  - WebP images provide 25-35% better compression than JPEG"

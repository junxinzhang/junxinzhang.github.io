#!/usr/bin/env node
/**
 * 将博客文章推送到微信公众号草稿箱
 * 用法: node scripts/push-to-wechat.mjs _posts/2026-04-16-xxx.md
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');

// ===== 配置 =====
const WECHAT_APP_ID = 'wx1a1d6f220430079b';
const WECHAT_APP_SECRET = 'd7dac2e7a5a487a551a86a6af43b5556';

// ===== 微信 API =====
async function getAccessToken() {
  const url = `https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=${WECHAT_APP_ID}&secret=${WECHAT_APP_SECRET}`;
  const resp = await fetch(url);
  const data = await resp.json();
  if (data.errcode || !data.access_token) {
    throw new Error(`获取 Access Token 失败: ${data.errmsg} (${data.errcode})`);
  }
  console.log('✅ Access Token 获取成功');
  return data.access_token;
}

async function uploadImage(accessToken, imagePath) {
  const url = `https://api.weixin.qq.com/cgi-bin/material/add_material?access_token=${accessToken}&type=image`;
  const imageBuffer = fs.readFileSync(imagePath);
  const filename = path.basename(imagePath);
  const ext = path.extname(filename).toLowerCase();
  const mimeTypes = { '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp', '.gif': 'image/gif' };
  const mimeType = mimeTypes[ext] || 'image/png';

  const formData = new FormData();
  const blob = new Blob([imageBuffer], { type: mimeType });
  formData.append('media', blob, filename);

  const resp = await fetch(url, { method: 'POST', body: formData });
  const data = await resp.json();
  if (data.errcode || !data.media_id) {
    throw new Error(`上传图片失败 (${filename}): ${data.errmsg} (${data.errcode})`);
  }
  console.log(`  ✅ 上传成功: ${filename} → ${data.media_id}`);
  return { media_id: data.media_id, url: data.url };
}

async function uploadContentImage(accessToken, imagePath) {
  const url = `https://api.weixin.qq.com/cgi-bin/media/uploadimg?access_token=${accessToken}`;
  const imageBuffer = fs.readFileSync(imagePath);
  const filename = path.basename(imagePath);
  const ext = path.extname(filename).toLowerCase();
  const mimeTypes = { '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp', '.gif': 'image/gif' };
  const mimeType = mimeTypes[ext] || 'image/png';

  const formData = new FormData();
  const blob = new Blob([imageBuffer], { type: mimeType });
  formData.append('media', blob, filename);

  const resp = await fetch(url, { method: 'POST', body: formData });
  const data = await resp.json();
  if (!data.url) {
    throw new Error(`上传正文图片失败 (${filename}): ${data.errmsg} (${data.errcode})`);
  }
  console.log(`  ✅ 正文图片上传: ${filename} → ${data.url}`);
  return data.url;
}

async function createDraft(accessToken, article) {
  const url = `https://api.weixin.qq.com/cgi-bin/draft/add?access_token=${accessToken}`;
  const resp = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ articles: [article] }),
  });
  const data = await resp.json();
  if (data.errcode || !data.media_id) {
    throw new Error(`创建草稿失败: ${data.errmsg} (${data.errcode})`);
  }
  console.log(`✅ 草稿创建成功! media_id: ${data.media_id}`);
  return data.media_id;
}

// ===== Markdown → HTML =====
function parseFrontMatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return { meta: {}, body: content };
  const metaStr = match[1];
  const body = match[2];
  const meta = {};
  for (const line of metaStr.split('\n')) {
    const m = line.match(/^(\w+):\s*"?(.+?)"?\s*$/);
    if (m) meta[m[1]] = m[2];
  }
  return { meta, body };
}

function markdownToWechatHtml(mdBody, imageUrlMap) {
  let html = '';
  const lines = mdBody.split('\n');

  for (let i = 0; i < lines.length; i++) {
    let line = lines[i];

    // 跳过"相关阅读"部分
    if (line.trim() === '## 相关阅读') break;

    // 跳过空行
    if (line.trim() === '') {
      html += '\n';
      continue;
    }

    // 跳过分隔线
    if (line.trim() === '---') continue;

    // 图片
    const imgMatch = line.match(/!\[([^\]]*)\]\(([^)]+)\)/);
    if (imgMatch) {
      const alt = imgMatch[1];
      const imgPath = imgMatch[2];
      const wxUrl = imageUrlMap[imgPath];
      if (wxUrl) {
        html += `<p style="text-align:center;margin:20px 0;"><img src="${wxUrl}" style="max-width:100%;height:auto;border-radius:8px;" /></p>\n`;
        if (alt) {
          html += `<p style="text-align:center;color:#999;font-size:13px;margin:-10px 0 20px;">${escapeHtml(alt)}</p>\n`;
        }
      }
      continue;
    }

    // <mark> 高亮 → 黄底加粗
    line = line.replace(/<mark>([\s\S]*?)<\/mark>/g, '<span style="background:#fff3cd;padding:2px 6px;border-radius:4px;font-weight:700;">$1</span>');

    // 标题
    const h2Match = line.match(/^## (.+)/);
    if (h2Match) {
      html += `<h2 style="margin:32px 0 16px;font-size:20px;font-weight:700;color:#111;border-left:4px solid #2563eb;padding-left:12px;">${processBold(escapeHtml(h2Match[1]))}</h2>\n`;
      continue;
    }
    const h3Match = line.match(/^### (.+)/);
    if (h3Match) {
      html += `<h3 style="margin:24px 0 12px;font-size:18px;font-weight:700;color:#222;">${processBold(escapeHtml(h3Match[1]))}</h3>\n`;
      continue;
    }

    // 表格
    if (line.includes('|') && line.trim().startsWith('|')) {
      const tableLines = [];
      while (i < lines.length && lines[i].includes('|') && lines[i].trim().startsWith('|')) {
        tableLines.push(lines[i]);
        i++;
      }
      i--; // 回退一行
      html += renderTable(tableLines);
      continue;
    }

    // 引用块
    if (line.startsWith('> ')) {
      html += `<blockquote style="margin:16px 0;padding:12px 16px;border-left:4px solid #2563eb;background:#f8fafc;color:#333;font-size:15px;line-height:1.8;">${processBold(processLinks(escapeHtml(line.slice(2))))}</blockquote>\n`;
      continue;
    }

    // 普通段落
    html += `<p style="margin:0 0 16px;color:#222;font-size:16px;line-height:1.8;">${processBold(processLinks(processInlineMarkup(line)))}</p>\n`;
  }

  return html;
}

function processInlineMarkup(line) {
  // 处理 <mark> 标签 (在 escapeHtml 之前处理)
  line = line.replace(/<mark>([\s\S]*?)<\/mark>/g, '%%%MARK_START%%%$1%%%MARK_END%%%');
  line = escapeHtml(line);
  line = line.replace(/%%%MARK_START%%%([\s\S]*?)%%%MARK_END%%%/g, '<span style="background:#fff3cd;padding:2px 6px;border-radius:4px;font-weight:700;">$1</span>');
  return line;
}

function processBold(text) {
  return text.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
}

function processLinks(text) {
  // [text](url) → <a href="url">text</a>
  return text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" style="color:#2563eb;text-decoration:none;">$1</a>');
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

function renderTable(tableLines) {
  // 解析表头和数据行
  const rows = tableLines
    .filter(line => !line.match(/^\|[\s-:|]+\|$/)) // 过滤分隔行
    .map(line => line.split('|').slice(1, -1).map(cell => cell.trim()));

  if (rows.length === 0) return '';

  const headerRow = rows[0];
  const dataRows = rows.slice(1);

  let tableHtml = '<table style="width:100%;border-collapse:collapse;margin:16px 0 24px;font-size:14px;">';
  tableHtml += '<thead><tr>';
  for (const cell of headerRow) {
    tableHtml += `<th style="padding:10px 12px;background:#1e293b;color:#fff;font-weight:600;text-align:left;border:1px solid #334155;">${processBold(cell)}</th>`;
  }
  tableHtml += '</tr></thead><tbody>';
  for (const row of dataRows) {
    tableHtml += '<tr>';
    for (const cell of row) {
      tableHtml += `<td style="padding:8px 12px;border:1px solid #e2e8f0;color:#333;">${processBold(cell)}</td>`;
    }
    tableHtml += '</tr>';
  }
  tableHtml += '</tbody></table>';
  return tableHtml + '\n';
}

// ===== 主流程 =====
async function main() {
  const articlePath = process.argv[2];
  if (!articlePath) {
    console.error('用法: node scripts/push-to-wechat.mjs <article.md>');
    process.exit(1);
  }

  const fullPath = path.resolve(ROOT, articlePath);
  console.log(`📄 读取文章: ${fullPath}`);

  const content = fs.readFileSync(fullPath, 'utf-8');
  const { meta, body } = parseFrontMatter(content);

  console.log(`📝 标题: ${meta.title}`);

  // 1. 提取所有图片路径
  const imageRegex = /!\[[^\]]*\]\(([^)]+)\)/g;
  const imagePaths = [];
  let match;
  while ((match = imageRegex.exec(body)) !== null) {
    imagePaths.push(match[1]);
  }
  console.log(`🖼️  发现 ${imagePaths.length} 张图片`);

  // 2. 获取 Access Token
  const accessToken = await getAccessToken();

  // 3. 上传封面图（front matter 中的 image）
  let thumbMediaId = null;
  if (meta.image) {
    const coverPath = path.resolve(ROOT, meta.image);
    console.log(`\n📸 上传封面图: ${coverPath}`);
    const result = await uploadImage(accessToken, coverPath);
    thumbMediaId = result.media_id;
  }

  // 4. 上传正文图片
  console.log('\n📸 上传正文图片...');
  const imageUrlMap = {};
  for (const imgPath of imagePaths) {
    // 转为绝对路径
    const absPath = path.resolve(ROOT, imgPath.startsWith('/') ? imgPath.slice(1) : imgPath);
    if (fs.existsSync(absPath)) {
      const wxUrl = await uploadContentImage(accessToken, absPath);
      imageUrlMap[imgPath] = wxUrl;
    } else {
      console.warn(`  ⚠️ 图片不存在: ${absPath}`);
    }
  }

  // 5. 转换 Markdown → HTML
  console.log('\n🔄 转换文章为 HTML...');
  const htmlContent = markdownToWechatHtml(body, imageUrlMap);

  const fullHtml = `
<div style="padding:0;">
  ${htmlContent}
  <p style="text-align:center;color:#aaa;font-size:12px;margin-top:32px;">— 完 —</p>
</div>`.trim();

  // 6. 创建草稿
  console.log('\n📮 推送到公众号草稿箱...');

  if (!thumbMediaId && imagePaths.length > 0) {
    // 如果没有封面，用第一张正文图当封面
    const firstImgPath = imagePaths[0];
    const absPath = path.resolve(ROOT, firstImgPath.startsWith('/') ? firstImgPath.slice(1) : firstImgPath);
    if (fs.existsSync(absPath)) {
      const result = await uploadImage(accessToken, absPath);
      thumbMediaId = result.media_id;
    }
  }

  const article = {
    article_type: 'news',
    title: meta.title || '未命名文章',
    thumb_media_id: thumbMediaId,
    content: fullHtml,
    digest: (meta.description || '').slice(0, 120),
    need_open_comment: 1,
    only_fans_can_comment: 0,
  };

  const draftMediaId = await createDraft(accessToken, article);
  console.log(`\n🎉 完成！草稿 ID: ${draftMediaId}`);
  console.log('请前往微信公众号后台「草稿箱」查看');
}

main().catch(err => {
  console.error('❌ 推送失败:', err.message);
  process.exit(1);
});

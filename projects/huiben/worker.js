const RAW_BASE = 'https://raw.githubusercontent.com/junxinzhang/junxinzhang.github.io/master/projects/huiben';
const DEFAULT_MODEL = 'gpt-5.5';
const ASSET_VERSION = 'd9e7305';

addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request) {
  const url = new URL(request.url);

  if (url.pathname === '/api/story') {
    if (request.method !== 'POST') return json({ error: 'method not allowed' }, 405);
    return createStory(request);
  }

  if (request.method !== 'GET' && request.method !== 'HEAD') {
    return new Response('Method not allowed', { status: 405 });
  }

  return serveStatic(url.pathname, request);
}

async function createStory(request) {
  const apiKey = typeof ZAOKIT_API_KEY !== 'undefined' ? ZAOKIT_API_KEY : '';
  if (!apiKey) return json({ error: 'story api key is not configured' }, 500);

  const input = await request.json().catch(() => null);
  if (!input || typeof input !== 'object') return json({ error: 'invalid request' }, 400);

  const safe = sanitizeInput(input);
  const model = typeof ZAOKIT_MODEL !== 'undefined' && ZAOKIT_MODEL ? ZAOKIT_MODEL : DEFAULT_MODEL;
  const base = typeof ZAOKIT_API_BASE !== 'undefined' && ZAOKIT_API_BASE ? ZAOKIT_API_BASE : 'https://cc.zaokit.ai/v1';

  const upstream = await fetch(`${base.replace(/\/$/, '')}/chat/completions`, {
    method: 'POST',
    headers: {
      authorization: `Bearer ${apiKey}`,
      'content-type': 'application/json'
    },
    body: JSON.stringify({
      model,
      temperature: 0.85,
      max_tokens: 1800,
      response_format: { type: 'json_object' },
      messages: [
        {
          role: 'system',
          content: '你是儿童绘本作者。只输出 JSON，不要 Markdown。故事必须温暖、适合亲子阅读、没有惊吓和危险行为。'
        },
        {
          role: 'user',
          content: buildPrompt(safe)
        }
      ]
    })
  });

  const data = await upstream.json().catch(() => ({}));
  if (!upstream.ok) {
    return json({ error: data.error?.message || 'story api request failed' }, 502);
  }

  const content = data.choices?.[0]?.message?.content || '';
  const book = parseBook(content, safe);
  return json({ book, model });
}

function sanitizeInput(input) {
  const pick = (key, fallback, max = 120) => String(input[key] || fallback).trim().slice(0, max);
  const theme = ['勇气', '分享', '睡觉', '自信'].includes(input.theme) ? input.theme : '勇气';
  const style = ['水彩绘本', '蜡笔童画', '剪纸拼贴'].includes(input.style) ? input.style : '水彩绘本';
  const role = ['她', '他', 'TA'].includes(input.childRole) ? input.childRole : 'TA';
  return {
    childName: pick('childName', '小朋友', 12),
    childAge: pick('childAge', '5', 2),
    childRole: role,
    theme,
    style,
    traits: pick('traits', '有好奇心，也会有一点点担心'),
    details: pick('details', '最喜欢的玩具和睡前的小习惯')
  };
}

function buildPrompt(input) {
  return `请根据这些信息生成一本 8 页儿童绘本。
孩子名字：${input.childName}
年龄：${input.childAge}
称呼：${input.childRole}
主题：${input.theme}
画风：${input.style}
孩子特点：${input.traits}
真实细节：${input.details}

输出 JSON，结构必须是：
{
  "title": "不超过 18 个中文字符",
  "subtitle": "一句短副标题",
  "style": "${input.style}",
  "prompt": "整本书的插画统一提示词",
  "pages": [
    {"heading":"封面","text":"60 到 90 个中文字符","scene":"home"}
  ]
}
pages 必须刚好 8 页。scene 只能从 home、forest、sea、night、stage 中选择。故事要有起承转合，最后一页给孩子一句温柔的话。`;
}

function parseBook(content, input) {
  let parsed;
  try {
    parsed = JSON.parse(content);
  } catch {
    const match = content.match(/\{[\s\S]*\}/);
    parsed = match ? JSON.parse(match[0]) : null;
  }
  if (!parsed || !Array.isArray(parsed.pages)) throw new Error('invalid story response');
  const allowedScenes = new Set(['home', 'forest', 'sea', 'night', 'stage']);
  const pages = parsed.pages.slice(0, 8).map((page, index) => ({
    heading: String(page.heading || `第 ${index + 1} 页`).slice(0, 24),
    text: String(page.text || '').slice(0, 180),
    scene: allowedScenes.has(page.scene) ? page.scene : ['home', 'forest', 'sea', 'night', 'stage'][index % 5]
  })).filter(page => page.text);

  if (pages.length < 4) throw new Error('not enough pages');
  return {
    title: String(parsed.title || `${input.childName}的专属绘本`).slice(0, 40),
    subtitle: String(parsed.subtitle || `${input.childAge} 岁孩子的${input.theme}主题绘本`).slice(0, 60),
    style: String(parsed.style || input.style).slice(0, 30),
    prompt: String(parsed.prompt || '').slice(0, 600),
    pages
  };
}

async function serveStatic(pathname, request) {
  const cleanPath = normalizePath(pathname);
  const assetUrl = `${RAW_BASE}${cleanPath}?v=${ASSET_VERSION}`;
  const upstream = await fetch(assetUrl, {
    headers: { 'user-agent': 'huiben-worker' },
    cf: { cacheTtl: cleanPath === '/index.html' ? 60 : 3600, cacheEverything: true }
  });
  if (!upstream.ok) return new Response('Not found', { status: 404 });
  const headers = new Headers(upstream.headers);
  headers.delete('content-security-policy');
  headers.delete('x-frame-options');
  headers.delete('cross-origin-resource-policy');
  headers.delete('x-content-type-options');
  headers.set('content-type', contentType(cleanPath));
  headers.set('cache-control', cleanPath === '/index.html' ? 'public, max-age=60' : 'public, max-age=3600');
  return new Response(request.method === 'HEAD' ? null : upstream.body, { status: 200, headers });
}

function normalizePath(pathname) {
  let path = pathname.replace(/^\/projects\/huiben/, '');
  if (path === '' || path === '/') return '/index.html';
  if (!/^\/(css|js|assets)\//.test(path)) return '/index.html';
  return path;
}

function contentType(path) {
  if (path.endsWith('.html')) return 'text/html; charset=utf-8';
  if (path.endsWith('.css')) return 'text/css; charset=utf-8';
  if (path.endsWith('.js')) return 'application/javascript; charset=utf-8';
  if (path.endsWith('.svg')) return 'image/svg+xml';
  return 'application/octet-stream';
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'content-type': 'application/json; charset=utf-8',
      'cache-control': 'no-store'
    }
  });
}

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Static multi-language HTML generator for Zaokit ClaudeOps (claudeops.zaokit.ai).
Generates 4 pages (index.html, privacy.html, terms.html, refund.html) across all 19 locales = 76 HTML files.
"""
import argparse
import html
import json
import os
import sys
import unicodedata
from urllib.parse import quote

ROOT = "/Users/jason/workspace/junxinzhang.github.io/projects/claude-ops"
I18N_DIR = os.path.join(ROOT, "_i18n")
LOCALES_DIR = os.path.join(I18N_DIR, "locales")
SITE_ORIGIN = "https://claudeops.zaokit.ai"

LOCALES = [
    {
        "slug": "zh",
        "is_root": True,
        "html_lang": "zh-CN",
        "hreflang": "zh-CN",
        "og_locale": "zh_CN",
        "dir": "ltr",
        "native_name": "简体中文",
        "short_label": "简中",
        "default_currency": "AUD",
        "google_font": None,
        "font_extra": '"Noto Sans SC", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei"',
        "serif_extra": '"Source Han Serif SC", "Noto Serif SC", "Songti SC"',
    },
    {
        "slug": "zh-tw",
        "is_root": False,
        "html_lang": "zh-TW",
        "hreflang": "zh-TW",
        "og_locale": "zh_TW",
        "dir": "ltr",
        "native_name": "繁體中文",
        "short_label": "繁中",
        "default_currency": "USD",
        "google_font": "Noto+Sans+TC:wght@400;600;700",
        "font_extra": '"Noto Sans TC", "PingFang TC", "Hiragino Sans CNS", "Microsoft JhengHei"',
        "serif_extra": '"Noto Serif TC", "Source Han Serif TC", "Songti TC"',
    },
    {
        "slug": "en",
        "is_root": False,
        "x_default": True,
        "html_lang": "en-AU",
        "hreflang": "en",
        "og_locale": "en_AU",
        "dir": "ltr",
        "native_name": "English",
        "short_label": "EN",
        "default_currency": "AUD",
        "google_font": None,
        "font_extra": '"Noto Sans SC", "PingFang SC"',
        "serif_extra": '"Source Han Serif SC", "Noto Serif SC"',
    },
    {
        "slug": "ja",
        "is_root": False,
        "html_lang": "ja",
        "hreflang": "ja",
        "og_locale": "ja_JP",
        "dir": "ltr",
        "native_name": "日本語",
        "short_label": "日本語",
        "default_currency": "USD",
        "google_font": "Noto+Sans+JP:wght@400;600;700",
        "font_extra": '"Noto Sans JP", "Hiragino Kaku Gothic ProN", "Yu Gothic", "Meiryo"',
        "serif_extra": '"Noto Serif JP", "Hiragino Mincho ProN", "Yu Mincho"',
    },
    {
        "slug": "ko",
        "is_root": False,
        "html_lang": "ko",
        "hreflang": "ko",
        "og_locale": "ko_KR",
        "dir": "ltr",
        "native_name": "한국어",
        "short_label": "한국어",
        "default_currency": "USD",
        "google_font": "Noto+Sans+KR:wght@400;600;700",
        "font_extra": '"Noto Sans KR", "Apple SD Gothic Neo", "Malgun Gothic"',
        "serif_extra": '"Noto Serif KR", "AppleMyungjo", "Batang"',
    },
    {
        "slug": "es",
        "is_root": False,
        "html_lang": "es",
        "hreflang": "es",
        "og_locale": "es_ES",
        "dir": "ltr",
        "native_name": "Español",
        "short_label": "ES",
        "default_currency": "EUR",
        "google_font": None,
        "font_extra": "system-ui, -apple-system",
        "serif_extra": "Georgia",
    },
    {
        "slug": "fr",
        "is_root": False,
        "html_lang": "fr",
        "hreflang": "fr",
        "og_locale": "fr_FR",
        "dir": "ltr",
        "native_name": "Français",
        "short_label": "FR",
        "default_currency": "EUR",
        "google_font": None,
        "font_extra": "system-ui, -apple-system",
        "serif_extra": "Georgia",
    },
    {
        "slug": "de",
        "is_root": False,
        "html_lang": "de",
        "hreflang": "de",
        "og_locale": "de_DE",
        "dir": "ltr",
        "native_name": "Deutsch",
        "short_label": "DE",
        "default_currency": "EUR",
        "google_font": None,
        "font_extra": "system-ui, -apple-system",
        "serif_extra": "Georgia",
    },
    {
        "slug": "pt",
        "is_root": False,
        "html_lang": "pt",
        "hreflang": "pt",
        "og_locale": "pt_BR",
        "dir": "ltr",
        "native_name": "Português",
        "short_label": "PT",
        "default_currency": "USD",
        "google_font": None,
        "font_extra": "system-ui, -apple-system",
        "serif_extra": "Georgia",
    },
    {
        "slug": "it",
        "is_root": False,
        "html_lang": "it",
        "hreflang": "it",
        "og_locale": "it_IT",
        "dir": "ltr",
        "native_name": "Italiano",
        "short_label": "IT",
        "default_currency": "EUR",
        "google_font": None,
        "font_extra": "system-ui, -apple-system",
        "serif_extra": "Georgia",
    },
    {
        "slug": "ru",
        "is_root": False,
        "html_lang": "ru",
        "hreflang": "ru",
        "og_locale": "ru_RU",
        "dir": "ltr",
        "native_name": "Русский",
        "short_label": "RU",
        "default_currency": "USD",
        "google_font": None,
        "font_extra": "system-ui, -apple-system",
        "serif_extra": "Georgia",
    },
    {
        "slug": "ar",
        "is_root": False,
        "html_lang": "ar",
        "hreflang": "ar",
        "og_locale": "ar_AE",
        "dir": "rtl",
        "native_name": "العربية",
        "short_label": "العربية",
        "default_currency": "USD",
        "google_font": "Noto+Sans+Arabic:wght@400;600;700",
        "font_extra": '"Noto Sans Arabic", "Geeza Pro", "SF Arabic", "Tahoma"',
        "serif_extra": '"Noto Sans Arabic", "Geeza Pro"',
    },
    {
        "slug": "id",
        "is_root": False,
        "html_lang": "id",
        "hreflang": "id",
        "og_locale": "id_ID",
        "dir": "ltr",
        "native_name": "Bahasa Indonesia",
        "short_label": "ID",
        "default_currency": "USD",
        "google_font": None,
        "font_extra": "system-ui, -apple-system",
        "serif_extra": "Georgia",
    },
    {
        "slug": "ms",
        "is_root": False,
        "html_lang": "ms",
        "hreflang": "ms",
        "og_locale": "ms_MY",
        "dir": "ltr",
        "native_name": "Bahasa Melayu",
        "short_label": "MS",
        "default_currency": "SGD",
        "google_font": None,
        "font_extra": "system-ui, -apple-system",
        "serif_extra": "Georgia",
    },
    {
        "slug": "vi",
        "is_root": False,
        "html_lang": "vi",
        "hreflang": "vi",
        "og_locale": "vi_VN",
        "dir": "ltr",
        "native_name": "Tiếng Việt",
        "short_label": "VI",
        "default_currency": "USD",
        "google_font": None,
        "font_extra": "system-ui, -apple-system",
        "serif_extra": "Georgia",
    },
    {
        "slug": "th",
        "is_root": False,
        "html_lang": "th",
        "hreflang": "th",
        "og_locale": "th_TH",
        "dir": "ltr",
        "native_name": "ไทย",
        "short_label": "ไทย",
        "default_currency": "USD",
        "google_font": "Noto+Sans+Thai:wght@400;600;700",
        "font_extra": '"Noto Sans Thai", "Thonburi", "Leelawadee UI", "Tahoma"',
        "serif_extra": '"Noto Sans Thai", "Thonburi"',
    },
    {
        "slug": "hi",
        "is_root": False,
        "html_lang": "hi",
        "hreflang": "hi",
        "og_locale": "hi_IN",
        "dir": "ltr",
        "native_name": "हिन्दी",
        "short_label": "हिन्दी",
        "default_currency": "USD",
        "google_font": "Noto+Sans+Devanagari:wght@400;600;700",
        "font_extra": '"Noto Sans Devanagari", "Kohinoor Devanagari", "Mangal"',
        "serif_extra": '"Noto Sans Devanagari", "Kohinoor Devanagari"',
    },
    {
        "slug": "km",
        "is_root": False,
        "html_lang": "km",
        "hreflang": "km",
        "og_locale": "km_KH",
        "dir": "ltr",
        "native_name": "ភាសាខ្មែរ",
        "short_label": "ខ្មែរ",
        "default_currency": "USD",
        "google_font": "Noto+Sans+Khmer:wght@400;600;700",
        "font_extra": '"Noto Sans Khmer", "Khmer Sangam MN", "Leelawadee UI", "Khmer OS"',
        "serif_extra": '"Noto Sans Khmer", "Khmer Sangam MN"',
    },
    {
        "slug": "tr",
        "is_root": False,
        "html_lang": "tr",
        "hreflang": "tr",
        "og_locale": "tr_TR",
        "dir": "ltr",
        "native_name": "Türkçe",
        "short_label": "TR",
        "default_currency": "USD",
        "google_font": None,
        "font_extra": "system-ui, -apple-system",
        "serif_extra": "Georgia",
    },
]

LOCALE_BY_SLUG = {loc["slug"]: loc for loc in LOCALES}
NODE_ORDER = ["AU", "US", "SG", "MY", "ID", "JP", "KH", "NZ", "CA"]
CURRENCY_ORDER = ["AUD", "USD", "EUR", "NZD", "CAD", "SGD", "CNY"]


def esc(s: str) -> str:
    return html.escape(str(s), quote=True)


def fmt_num(n) -> str:
    if isinstance(n, float) and n % 1 != 0:
        return f"{n:.2f}"
    return f"{int(n):,}"


def estimate_svg_text_px(text: str) -> float:
    w = 0.0
    for ch in text:
        if unicodedata.combining(ch):
            continue
        eaw = unicodedata.east_asian_width(ch)
        if eaw in ("W", "F"):
            w += 12.2
        elif ord(ch) < 128:
            w += 6.7
        else:
            w += 7.6
    return w


def page_abs_url(loc: dict, page_name: str) -> str:
    suffix = "" if page_name == "index.html" else page_name
    if loc["is_root"]:
        return f"{SITE_ORIGIN}/{suffix}"
    return f"{SITE_ORIGIN}/{loc['slug']}/{suffix}"


def rel_link_between(from_loc: dict, to_loc: dict, page_name: str) -> str:
    suffix = "" if page_name == "index.html" else page_name
    if from_loc["slug"] == to_loc["slug"]:
        return "./" if page_name == "index.html" else page_name
    if from_loc["is_root"]:
        # from root `/` to `/<to_slug>/<suffix>`
        return f"{to_loc['slug']}/{suffix}"
    if to_loc["is_root"]:
        # from `/<from_slug>/` to `/<suffix>`
        return f"../{suffix}"
    # from `/<from_slug>/` to `/<to_slug>/<suffix>`
    return f"../{to_loc['slug']}/{suffix}"


def build_hreflang_tags(cur_loc: dict, page_name: str) -> str:
    lines = [f'  <link rel="canonical" href="{page_abs_url(cur_loc, page_name)}">']
    for loc in LOCALES:
        lines.append(
            f'  <link rel="alternate" hreflang="{loc["hreflang"]}" href="{page_abs_url(loc, page_name)}">'
        )
    en_loc = LOCALE_BY_SLUG["en"]
    lines.append(
        f'  <link rel="alternate" hreflang="x-default" href="{page_abs_url(en_loc, page_name)}">'
    )
    return "\n".join(lines)


def build_google_font_links(cur_loc: dict) -> str:
    # Live production CSP uses `style-src 'self' 'unsafe-inline'; font-src 'self' data:;`.
    # Rely on cross-platform native system font stacks so zero external stylesheet/font requests violate CSP.
    return ""


def build_root_autoredirect_script(page_name: str) -> str:
    suffix = "" if page_name == "index.html" else page_name
    non_root_slugs = [loc["slug"] for loc in LOCALES if not loc["is_root"]]
    slugs_json = json.dumps(non_root_slugs)
    return f"""  <script>
  (function () {{
    try {{
      var ua = navigator.userAgent || '';
      if (/bot|crawl|spider|slurp|bingpreview|mediapartners|lighthouse|HeadlessChrome|facebookexternalhit|whatsapp|telegrambot|twitterbot|discordbot|applebot|baiduspider|yandex/i.test(ua)) return;
      var VALID = {slugs_json};
      var SUFFIX = {json.dumps(suffix)};
      var params = new URLSearchParams(location.search);
      if (params.get('nolang') === '1') return;
      var ql = (params.get('lang') || '').toLowerCase();
      if (ql === 'zh' || ql === 'zh-cn') {{
        try {{ localStorage.setItem('claude-ops-lang', 'zh'); }} catch (e) {{}}
        return;
      }}
      if (VALID.indexOf(ql) !== -1) {{
        try {{ localStorage.setItem('claude-ops-lang', ql); }} catch (e) {{}}
        location.replace('./' + ql + '/' + SUFFIX + location.hash);
        return;
      }}
      var saved = null;
      try {{ saved = localStorage.getItem('claude-ops-lang'); }} catch (e) {{}}
      if (saved === 'zh') return;
      if (saved && VALID.indexOf(saved) !== -1) {{
        location.replace('./' + saved + '/' + SUFFIX + location.search + location.hash);
        return;
      }}
      if (document.referrer && location.origin && document.referrer.indexOf(location.origin) === 0) return;
      var langs = (navigator.languages && navigator.languages.length) ? navigator.languages : [navigator.language || ''];
      for (var i = 0; i < langs.length; i++) {{
        var tag = String(langs[i] || '').toLowerCase();
        if (!tag) continue;
        if (tag.indexOf('zh') === 0) {{
          if (/^zh[-_](tw|hk|mo|hant)/.test(tag)) {{
            location.replace('./zh-tw/' + SUFFIX + location.search + location.hash);
          }}
          return;
        }}
        var p = tag.split(/[-_]/)[0];
        if (p === 'in') p = 'id';
        if (VALID.indexOf(p) !== -1) {{
          location.replace('./' + p + '/' + SUFFIX + location.search + location.hash);
          return;
        }}
      }}
    }} catch (e) {{}}
  }})();
  </script>
"""


LANG_SWITCHER_CSS = """
    /* 19-Language Switcher Dropdown & Multi-Script / RTL Support */
    .lang-switcher { position: relative; display: inline-flex; align-items: center }
    .lang-btn {
      display: inline-flex; align-items: center; gap: 6px;
      font: inherit; font-size: .83rem; font-weight: 600; color: var(--text);
      padding: 6px 12px; border-radius: 999px; cursor: pointer;
      border: 1px solid var(--border); background: var(--surface); transition: .2s;
      white-space: nowrap; line-height: 1.2;
    }
    .lang-btn:hover, .lang-btn[aria-expanded="true"] {
      color: #fff; border-color: var(--primary); background: var(--primary-soft);
    }
    .lang-caret { opacity: .75; transition: transform .2s ease }
    .lang-btn[aria-expanded="true"] .lang-caret { transform: rotate(180deg) }
    .lang-menu {
      position: absolute; top: calc(100% + 8px); right: 0; z-index: 95;
      width: min(340px, 90vw); max-height: min(72vh, 430px); overflow-y: auto;
      padding: 8px; border-radius: 16px;
      background: rgba(24, 21, 18, .97); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
      border: 1px solid rgba(232, 144, 111, .28);
      box-shadow: 0 22px 54px rgba(0, 0, 0, .68);
      display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 4px;
      direction: ltr; text-align: left;
    }
    .lang-menu[hidden] { display: none !important }
    .lang-item {
      display: flex; align-items: center; justify-content: space-between; gap: 6px;
      padding: 7px 10px; border-radius: 10px; font-size: .82rem; font-weight: 500;
      color: var(--text) !important; text-decoration: none !important;
      transition: background .16s, color .16s; line-height: 1.35;
    }
    .lang-item:hover { background: rgba(255, 255, 255, .07); color: #fff !important }
    .lang-item.active {
      background: rgba(217, 119, 87, .20); color: #ffe0c2 !important; font-weight: 700;
      border: 1px solid rgba(232, 144, 111, .36);
    }
    .lang-item .lang-check { font-size: .75rem; color: var(--primary-strong); flex-shrink: 0 }
    @media (max-width: 390px) { .lang-menu { grid-template-columns: 1fr } }
    [dir="rtl"] .lang-menu { right: auto; left: 0 }
"""

INDEX_EXTRA_I18N_CSS = """
    .brand, .header-right { flex-shrink: 0 }
    .map-body { position: relative }
    .map-hud-row b { white-space: normal; min-width: 0; line-height: 1.35 }
    @media (max-width: 1180px) {
      .nav-links { gap: 2px }
      .nav-links a { padding: 6px 7px; font-size: .81rem }
    }
    @media (max-width: 1030px) {
      .nav-links { display: none }
    }
    /* RTL Directional Overrides */
    [dir="rtl"] .hero-map-wrap { text-align: right }
    [dir="rtl"] .map-stage { direction: ltr; text-align: left }
    [dir="rtl"] .map-hud { direction: rtl; text-align: right }
    [dir="rtl"] .map-hud-row b { text-align: left }
    [dir="rtl"] .enterprise-jump { margin-left: 0; margin-right: 6px }
    [dir="rtl"] .price small { margin-left: 0; margin-right: 4px }
    [dir="rtl"] .price sup { margin-right: 0; margin-left: 2px }
    [dir="rtl"] .price-orig { margin-left: 0; margin-right: 8px }
    [dir="rtl"] .addon-price sup { margin-right: 0; margin-left: 1px }
    [dir="rtl"] .addon-price small { margin-left: 0; margin-right: 2px }
    [dir="rtl"] .line-orig { margin-left: 0; margin-right: 6px }
    [dir="rtl"] .pricing-enterprise .features li { padding: 4px 25px 4px 0 }
    [dir="rtl"] .pricing-enterprise .features li::before { left: auto; right: 0 }
    [dir="rtl"] .lg::before { margin-right: 0; margin-left: 6px }
    [dir="rtl"] .nb-fill { inset: 0 0 0 auto }
    [dir="rtl"] .nb em { padding-left: 0; padding-right: 8px }
    [dir="rtl"] .contact-tg { text-align: right }
    [dir="rtl"] .foot-right { margin-left: 0; margin-right: auto; text-align: left }
    [dir="rtl"] .social { justify-content: flex-start }
    [dir="rtl"] #scroll-progress { transform-origin: 100% 50% }
    @media (max-width: 560px) {
      [dir="rtl"] .contact-tg { text-align: center }
      [dir="rtl"] .foot-right { margin-right: 0; text-align: right }
      [dir="rtl"] .social { justify-content: flex-end }
    }
"""


def build_lang_switcher_html(cur_loc: dict, lang_aria: str, page_name: str) -> str:
    items_html = []
    for loc in LOCALES:
        href = rel_link_between(cur_loc, loc, page_name)
        is_active = loc["slug"] == cur_loc["slug"]
        cls = "lang-item active" if is_active else "lang-item"
        aria_cur = ' aria-current="page"' if is_active else ""
        chk = '<span class="lang-check" aria-hidden="true">✓</span>' if is_active else ""
        items_html.append(
            f'<a class="{cls}" role="menuitem" href="{esc(href)}" hreflang="{loc["hreflang"]}" '
            f'lang="{loc["html_lang"]}" data-set-lang="{loc["slug"]}"{aria_cur}>'
            f'<span dir="{loc["dir"]}">{esc(loc["native_name"])}</span>{chk}</a>'
        )
    joined_items = "".join(items_html)
    return (
        f'<div class="lang-switcher">'
        f'<button type="button" class="lang-btn" aria-haspopup="true" aria-expanded="false" aria-label="{esc(lang_aria)}">'
        f'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" aria-hidden="true">'
        f'<circle cx="12" cy="12" r="9.5"/><path d="M2.5 12h19M12 2.5c2.7 2.6 4.2 5.9 4.2 9.5s-1.5 6.9-4.2 9.5c-2.7-2.6-4.2-5.9-4.2-9.5S9.3 5.1 12 2.5z"/></svg>'
        f'<span>{esc(cur_loc["short_label"])}</span>'
        f'<svg class="lang-caret" width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 6l4 4 4-4"/></svg>'
        f'</button>'
        f'<div class="lang-menu" role="menu" hidden>{joined_items}</div>'
        f'</div>'
    )


def build_lang_switcher_js(cur_slug: str) -> str:
    return f"""  <script>
  (function () {{
    var CUR_LANG = {json.dumps(cur_slug)};
    document.querySelectorAll('.lang-switcher').forEach(function (sw) {{
      var btn = sw.querySelector('.lang-btn');
      var menu = sw.querySelector('.lang-menu');
      if (!btn || !menu) return;
      function closeMenu(restoreFocus) {{
        btn.setAttribute('aria-expanded', 'false');
        menu.hidden = true;
        if (restoreFocus) btn.focus();
      }}
      btn.addEventListener('click', function (e) {{
        e.stopPropagation();
        var open = btn.getAttribute('aria-expanded') === 'true';
        if (open) closeMenu(false);
        else {{
          btn.setAttribute('aria-expanded', 'true');
          menu.hidden = false;
        }}
      }});
      document.addEventListener('click', function (e) {{
        if (!sw.contains(e.target)) closeMenu(false);
      }});
      document.addEventListener('keydown', function (e) {{
        if (e.key === 'Escape' && btn.getAttribute('aria-expanded') === 'true') closeMenu(true);
      }});
    }});
    document.addEventListener('click', function (e) {{
      var a = e.target.closest && e.target.closest('a[data-set-lang]');
      if (!a) return;
      var target = a.getAttribute('data-set-lang');
      var lsOk = false;
      if (target) {{
        try {{ localStorage.setItem('claude-ops-lang', target); lsOk = true; }} catch (err) {{}}
        try {{
          if (typeof gtag === 'function') gtag('event', 'language_switch', {{ from_lang: CUR_LANG, to_lang: target }});
          if (window.umami && typeof umami.track === 'function') umami.track('language_switch', {{ from_lang: CUR_LANG, to_lang: target }});
        }} catch (err) {{}}
      }}
      var baseHref = a.getAttribute('href') || '';
      if (baseHref && baseHref.indexOf('#') === -1 && baseHref.indexOf('?') === -1 && (location.search || location.hash || (!lsOk && target === 'zh'))) {{
        e.preventDefault();
        var sp = new URLSearchParams(location.search);
        sp.delete('lang');
        sp.delete('nolang');
        if (!lsOk && target === 'zh') sp.set('lang', 'zh');
        var qs = sp.toString();
        location.href = baseHref + (qs ? '?' + qs : '') + location.hash;
      }}
    }});
  }})();
  </script>"""


def build_map_ui_svg(shared: dict, d_map: dict) -> str:
    geom_all = shared["node_geom"]
    parts = []
    for code in NODE_ORDER:
        g = geom_all[code]
        nd = d_map["nodes"][code]
        pill_text = nd["pill"]
        w = round(max(64.0, 30.0 + estimate_svg_text_px(pill_text) + 10.0), 1)
        rx = round(g["ax"] - w, 1) if g["anchor"] == "right" else g["ax"]
        cx = round(rx + 8.0, 1)
        nx = round(rx + 30.0, 1)
        cls = "node-hit hq active" if g["hq"] else "node-hit"
        aura_r = "15" if g["hq"] else "11"
        ring_r = "6.2" if g["hq"] else "4.8"
        core_r = "3.0" if g["hq"] else "2.3"
        parts.append(
            f'<g class="{cls}" data-node="{code}" data-anchor="{g["anchor"]}" data-ax="{g["ax"]}" '
            f'tabindex="0" role="button" aria-label="{esc(nd["name"])}">'
            f'<polyline class="node-leader" points="{g["leader"]}"/>'
            f'<circle class="node-aura" cx="{g["x"]}" cy="{g["y"]}" r="{aura_r}"/>'
            f'<circle class="node-ring" cx="{g["x"]}" cy="{g["y"]}" r="{ring_r}"/>'
            f'<circle class="node-core" cx="{g["x"]}" cy="{g["y"]}" r="{core_r}"/>'
            f'<rect class="node-pill-bg" x="{rx}" y="{g["ry"]}" width="{w}" height="24.0"/>'
            f'<text class="node-pill-code" x="{cx}" y="{g["ty"]}">{code}</text>'
            f'<text class="node-pill-name" x="{nx}" y="{g["ty"]}">{esc(pill_text)}</text>'
            f'</g>'
        )
    return (
        '              <svg class="map-ui-svg" viewBox="0 0 1120 510" preserveAspectRatio="xMidYMid meet">\n'
        '                ' + "".join(parts) + '\n'
        '              </svg>'
    )


def render_index(loc: dict, d: dict, shared: dict, base_css: str) -> str:
    asset_prefix = "" if loc["is_root"] else "../"
    html_dir = f' dir="{loc["dir"]}"' if loc["dir"] == "rtl" else ""
    def_cur = loc["default_currency"]
    prices = shared["prices"]
    cur_data = prices[def_cur]
    sym = cur_data["sym"]
    stripe = shared["stripe_links"]

    # JSON-LD structured data
    onames = d["meta"]["offer_names"]
    ld_obj = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": "Zaokit ClaudeOps",
        "inLanguage": loc["html_lang"],
        "description": d["meta"]["ld_description"],
        "provider": {
            "@type": "Organization",
            "name": "Zaokit AI",
            "url": "https://zaokit.app",
            "address": {"@type": "PostalAddress", "addressCountry": "AU"},
        },
        "offers": [
            {"@type": "Offer", "name": onames[0], "price": str(prices["AUD"]["p"][0]), "priceCurrency": "AUD"},
            {"@type": "Offer", "name": onames[1], "price": str(prices["AUD"]["p"][1]), "priceCurrency": "AUD"},
            {"@type": "Offer", "name": onames[2], "price": str(prices["AUD"]["p"][2]), "priceCurrency": "AUD", "priceValidUntil": "2026-12-31"},
            {"@type": "Offer", "name": onames[0], "price": str(prices["USD"]["p"][0]), "priceCurrency": "USD"},
            {"@type": "Offer", "name": onames[1], "price": str(prices["USD"]["p"][1]), "priceCurrency": "USD"},
            {"@type": "Offer", "name": onames[2], "price": str(prices["USD"]["p"][2]), "priceCurrency": "USD", "priceValidUntil": "2026-12-31"},
            {"@type": "Offer", "name": onames[0], "price": str(prices["EUR"]["p"][0]), "priceCurrency": "EUR"},
            {"@type": "Offer", "name": onames[1], "price": str(prices["EUR"]["p"][1]), "priceCurrency": "EUR"},
            {"@type": "Offer", "name": onames[2], "price": str(prices["EUR"]["p"][2]), "priceCurrency": "EUR", "priceValidUntil": "2026-12-31"},
        ],
    }
    ld_json_str = json.dumps(ld_obj, ensure_ascii=False, indent=2)
    ld_indented = "\n".join("  " + line for line in ld_json_str.splitlines())

    # Font variables customized per locale script
    css_custom = base_css.replace(
        '--font: "Inter", "Noto Sans SC", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;',
        f'--font: "Inter", {loc["font_extra"]}, sans-serif;',
    ).replace(
        '--serif: "Tiempos Headline", "Source Han Serif SC", "Noto Serif SC", "Songti SC", Georgia, serif;',
        f'--serif: "Tiempos Headline", {loc["serif_extra"]}, Georgia, serif;',
    )

    hreflang_block = build_hreflang_tags(loc, "index.html")
    gfont_block = build_google_font_links(loc)
    autoredir_block = build_root_autoredirect_script("index.html") if loc["is_root"] else ""
    switcher_html = build_lang_switcher_html(loc, d["nav"]["lang_aria"], "index.html")

    # Mailto URLs
    enq_mailto = f"mailto:jason2023zhang@gmail.com?subject={quote(d['hero']['mailto_enquiry_subject'])}"
    partner_mailto = (
        f"mailto:jason2023zhang@gmail.com?subject={quote(d['map']['partner_mailto_subject'])}"
        f"&body={quote(d['map']['partner_mailto_body'])}"
    )

    # Map pills
    au_node = d["map"]["nodes"]["AU"]
    map_pills_html = "".join(
        f'<button type="button" class="map-pill{" active" if c == "AU" else ""}" data-pick-node="{c}">'
        f'<i></i><span>{esc(d["map"]["nodes"][c]["short"])}</span><code>{c}</code></button>'
        for c in NODE_ORDER
    )
    map_ui_svg = build_map_ui_svg(shared, d["map"])

    # Hero stats
    stats_html = "\n".join(
        f'          <div class="stat"><strong>{esc(st["strong"])}</strong><span>{esc(st["span"])}</span></div>'
        for st in d["hero"]["stats"]
    )

    # Pain cards (4 icons)
    why_icons = [
        '<circle cx="12" cy="12" r="9"/><path d="M5.6 5.6l12.8 12.8"/>',
        '<path d="M2 8.5a15 15 0 0120 0M5 12a10 10 0 0114 0M8.5 15.5a5 5 0 017 0"/><path d="M3 3l18 18"/>',
        '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/>',
        '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    ]
    why_cards_html = "\n".join(
        f'          <div class="card">\n'
        f'            <div class="icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{why_icons[i]}</svg></div>\n'
        f'            <h3>{esc(c["h3"])}</h3>\n'
        f'            <p>{esc(c["p"])}</p>\n'
        f'          </div>'
        for i, c in enumerate(d["why"]["cards"])
    )

    # Service cards (4 icons)
    svc_icons = [
        '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0116 0"/>',
        '<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/><path d="M9 12l2 2 4-4"/>',
        '<path d="M21 12a9 9 0 11-3-6.7L21 8"/><path d="M21 3v5h-5"/>',
        '<path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"/>',
    ]
    svc_cards_html = "\n".join(
        f'          <div class="card">\n'
        f'            <div class="icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{svc_icons[i]}</svg></div>\n'
        f'            <h3>{esc(c["h3"])}</h3>\n'
        f'            <p>{esc(c["p"])}</p>\n'
        f'          </div>'
        for i, c in enumerate(d["service"]["cards"])
    )

    # Value cards (3 icons)
    val_icons = [
        '<path d="M13 2L3 14h9l-1 8 10-12h-9z"/>',
        '<path d="M16 18l6-6-6-6M8 6l-6 6 6 6"/>',
        '<path d="M4 11a9 9 0 019 9M4 4a16 16 0 0116 16"/><circle cx="5" cy="19" r="1"/>',
    ]
    val_cards_html = "\n".join(
        f'          <div class="card value-card">\n'
        f'            <div class="icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{val_icons[i]}</svg></div>\n'
        f'            <h3>{esc(c["h3"])}</h3>\n'
        f'            <p>{esc(c["p"])}</p>\n'
        f'          </div>'
        for i, c in enumerate(d["value"]["cards"])
    )

    # Network chips & rows
    net_chips_html = "".join(f"<li>{esc(ch)}</li>" for ch in d["network"]["chips"])
    net_widths = [("39.0%", "23.0%"), ("91.2%", "60.0%"), (None, "20.2%")]
    net_rows_parts = []
    for i, r in enumerate(d["network"]["rows"]):
        wb, wa = net_widths[i]
        bars = ""
        if wb and r.get("before"):
            bars += f'<div class="nb before"><span class="nb-fill" style="--w:{wb}"></span><em>{esc(r["before"])}</em></div>'
        bars += f'<div class="nb after"><span class="nb-fill" style="--w:{wa}"></span><em>{esc(r["after"])}</em></div>'
        net_rows_parts.append(
            f'              <div class="net-row">\n'
            f'                <div class="net-node"><strong>{esc(r["country"])}</strong><span>{esc(r["via"])}</span></div>\n'
            f'                <div class="net-bars">{bars}</div>\n'
            f'              </div>'
        )
    net_rows_html = "\n".join(net_rows_parts)

    # Security cards
    sec_icons = [
        '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/>',
        '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
        '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/>',
    ]
    sec_cards_html = "\n".join(
        f'          <div class="card">\n'
        f'            <div class="icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">{sec_icons[i]}</svg></div>\n'
        f'            <h3>{esc(c["h3"])}</h3>\n'
        f'            <p>{esc(c["p"])}</p>\n'
        f'          </div>'
        for i, c in enumerate(d["security"]["cards"])
    )

    # Reviews (6 cards)
    rev_cards_parts = []
    for i, rv in enumerate(d["reviews"]["items"]):
        rev_cards_parts.append(
            f'          <article class="card review-card">\n'
            f'            <div class="review-head">\n'
            f'              <div class="review-avatar" aria-hidden="true">\n'
            f'                {shared["review_avatars"][i]}\n'
            f'              </div>\n'
            f'              <div class="review-author">\n'
            f'                <div class="review-name-row">\n'
            f'                  <span class="review-name">{esc(rv["name"])}</span>\n'
            f'                  <span class="review-badge">{esc(d["reviews"]["badge"])}</span>\n'
            f'                </div>\n'
            f'                <div class="review-role">{esc(rv["role"])}</div>\n'
            f'              </div>\n'
            f'            </div>\n'
            f'            <div class="review-stars" aria-label="{esc(d["reviews"]["stars_aria"])}">★★★★★</div>\n'
            f'            <p class="review-quote">{esc(rv["quote"])}</p>\n'
            f'            <div class="review-foot">\n'
            f'              <span>{esc(rv["source"])}</span>\n'
            f'              <span class="review-plan">{esc(rv["plan"])}</span>\n'
            f'            </div>\n'
            f'          </article>'
        )
    reviews_html = "\n\n".join(rev_cards_parts)

    # Currency switch buttons
    cur_btns_html = "\n".join(
        f'            <button type="button" data-currency="{c}" aria-pressed="{"true" if c == def_cur else "false"}">'
        f'{esc(d["pricing"]["currencies"][c]["btn"])}</button>'
        for c in CURRENCY_ORDER
    )

    def py_tpl(s: str, **vals) -> str:
        out = str(s)
        for k, v in vals.items():
            out = out.replace("{" + k + "}", str(v))
        return out

    # Solo plans (1x, 5x, 20x)
    solo_tiers = ["1x", "5x", "20x"]
    solo_mult = [1, 5, 20]
    solo_parts = []
    for i, sp in enumerate(d["pricing"]["solo"]):
        tkey = solo_tiers[i]
        is_feat = i == 1
        card_cls = "card plan featured" if is_feat else "card plan"
        btn_cls = "btn btn-primary" if is_feat else "btn btn-ghost"
        badge_html = ""
        if "badge" in sp:
            badge_html = f'\n            <span class="badge">{esc(sp["badge"])}</span>'
        elif "badge_promo" in sp:
            badge_html = f'\n            <span class="badge badge-promo">{esc(sp["badge_promo"])}</span>'

        if i == 2:
            orig_html = (
                f'<del class="price-orig" data-orig-idx="2" data-orig-20x title="{esc(d["js"]["title_reg_mo"])}">'
                f'{esc(sym)}{fmt_num(cur_data["orig20x"])}</del>'
            )
        else:
            orig_html = f'<del class="price-orig" data-orig-idx="{i}" style="display:none"></del>'

        if i == 0:
            day_val = cur_data["p"][0] / 30.0
            day_str = str(round(day_val)) if day_val >= 10 else f"{day_val:.1f}".rstrip("0").rstrip(".")
            init_solo_note = py_tpl(d["js"]["note_1x_mo"], sym=sym, day=day_str)
        elif i == 2:
            r2 = round(cur_data["p"][2] / (cur_data["p"][0] * solo_mult[2]) * 100)
            init_solo_note = py_tpl(d["js"]["note_20x_promo"], ratio=r2)
        else:
            r1 = round(cur_data["p"][i] / (cur_data["p"][0] * solo_mult[i]) * 100)
            init_solo_note = py_tpl(d["js"]["note_mult_mo"], mult=solo_mult[i], ratio=r1)

        feats_li = []
        for fi, fh in enumerate(sp["features_html"]):
            if i == 2 and fi >= 6:
                feats_li.append(f'              <li style="color: var(--primary-strong); font-weight: 600;">{fh}</li>')
            else:
                feats_li.append(f"              <li>{fh}</li>")
        feats_block = "\n".join(feats_li)
        s_href = stripe.get(f"{tkey}_{def_cur}", stripe[f"{tkey}_AUD"])
        m_href = f"mailto:jason2023zhang@gmail.com?subject={quote(sp['mailto_subject'])}"
        solo_parts.append(
            f'          <article class="{card_cls}">{badge_html}\n'
            f'            <div class="plan-tier"><b>{esc(sp["tier_b"])}</b><span>{esc(sp["tier_span"])}</span></div>\n'
            f'            <p class="plan-desc">{esc(sp["desc"])}</p>\n'
            f'            <div class="price" data-plan-idx="{i}"><sup>{esc(sym)}</sup><span class="amount">{fmt_num(cur_data["p"][i])}</span>'
            f'<small data-period>{esc(d["js"]["per_month"])}</small>{orig_html}</div>\n'
            f'            <p class="price-note" data-note-idx="{i}">{esc(init_solo_note)}</p>\n'
            f'            <ul class="features">\n{feats_block}\n            </ul>\n'
            f'            <a class="{btn_cls}" data-stripe-tier="{tkey}" href="{esc(s_href)}" target="_blank" rel="noopener">{esc(d["pricing"]["solo_subscribe"])}</a>\n'
            f'            <a class="plan-consult" href="{esc(m_href)}">{esc(d["pricing"]["solo_consult"])}</a>\n'
            f'          </article>'
        )
    solo_html = "\n\n".join(solo_parts)

    # Dedicated Line cards
    dl = d["pricing"]["dedicated_line"]
    dl_cards = []
    for i, lc in enumerate(dl["cards"]):
        lkey = "line_1x" if i == 0 else "line_5x"
        c_cls = "addon-card addon-card-featured" if i == 1 else "addon-card"
        code_cls = ' class="to"' if i == 1 else ""
        b_cls = "addon-btn addon-btn-primary" if i == 1 else "addon-btn"
        l_href = stripe.get(f"{lkey}_{def_cur}", stripe[f"{lkey}_AUD"])
        init_line_note = d["js"]["line_0_mo"] if i == 0 else d["js"]["line_1_mo"]
        dl_cards.append(
            f'            <div class="{c_cls}">\n'
            f'              <div>\n'
            f'                <div class="addon-route"><code{code_cls}>{esc(lc["code"])}</code> <span>{esc(lc["span"])}</span></div>\n'
            f'                <p class="addon-desc">{esc(lc["desc"])}</p>\n'
            f'              </div>\n'
            f'              <div class="addon-foot">\n'
            f'                <div class="line-price-wrap">\n'
            f'                  <div class="addon-price" data-line-idx="{i}">+<sup>{esc(sym)}</sup><span class="amount">{fmt_num(cur_data["line"][i])}</span>'
            f'<small data-line-period>{esc(d["js"]["per_mo_short"])}</small><del class="line-orig" data-line-orig="{i}" style="display:none"></del></div>\n'
            f'                  <span class="line-subnote" data-line-note="{i}">{esc(init_line_note)}</span>\n'
            f'                </div>\n'
            f'                <a class="{b_cls}" data-line-tier="{lkey}" href="{esc(l_href)}" target="_blank" rel="noopener">{esc(lc["btn"])}</a>\n'
            f'              </div>\n'
            f'            </div>'
        )
    dl_cards_html = "\n".join(dl_cards)

    # Enterprise Team & Business
    ent = d["pricing"]["enterprise"]
    ec_max = d["js"]["ent_copy"]["max"]
    ent_parts = []
    for kind in ("team", "biz"):
        ek = ent[kind]
        is_biz = kind == "biz"
        p_cls = "card plan plan-business" if is_biz else "card plan"
        b_cls = "badge" if is_biz else "badge badge-team"
        btn_cls = "btn btn-primary" if is_biz else "btn btn-ghost"
        init_amt = cur_data[kind][1]  # default max (idx 1)
        e_href = stripe.get(f"{kind}_max_{def_cur}", stripe[f"{kind}_max_AUD"])
        em_href = f"mailto:jason2023zhang@gmail.com?subject={quote(ek['mailto_subject'])}"
        init_ent_badge = ec_max["bizBadge"] if is_biz else ec_max["teamBadge"]
        init_ent_seat_li = ec_max["bizSeatLi"] if is_biz else ec_max["teamSeatLi"]
        init_ent_storage = ec_max["bizStorage"] if is_biz else ec_max["teamStorage"]
        init_ent_note = py_tpl(d["js"]["ent_biz_mo"] if is_biz else d["js"]["ent_team_mo"], label=ec_max["label"])

        mid_lis = []
        for idx_f, fh in enumerate(ek["features_html"]):
            if idx_f == len(ek["features_html"]) - 1:
                mid_lis.append(f'                <li style="color: var(--primary-strong); font-weight: 600;">{fh}</li>')
            else:
                mid_lis.append(f"                <li>{fh}</li>")
        mid_lis_str = "\n".join(mid_lis)
        ent_parts.append(
            f'            <article class="{p_cls}">\n'
            f'              <span class="{b_cls}" data-ent-badge="{kind}">{esc(init_ent_badge)}</span>\n'
            f'              <div class="plan-tier"><b>{"Business" if is_biz else "Team"}</b><span data-ent-sub="{kind}">{esc(ek["sub"])}</span></div>\n'
            f'              <p class="plan-desc">{esc(ek["desc"])}</p>\n'
            f'              <div class="price" data-ent-price="{kind}"><sup>{esc(sym)}</sup><span class="amount">{fmt_num(init_amt)}</span>'
            f'<small data-period>{esc(d["js"]["per_month"])}</small><del class="price-orig" data-ent-orig="{kind}" style="display:none"></del></div>\n'
            f'              <p class="price-note" data-ent-note="{kind}">{esc(init_ent_note)}</p>\n'
            f'              <ul class="features">\n'
            f'                <li data-ent-seat-li="{kind}">{init_ent_seat_li}</li>\n'
            f'{mid_lis_str}\n'
            f'                <li style="color: var(--primary-strong); font-weight: 600;" data-ent-storage-li="{kind}">{esc(init_ent_storage)}</li>\n'
            f'              </ul>\n'
            f'              <a class="{btn_cls}" data-ent-btn="{kind}" href="{esc(e_href)}" target="_blank" rel="noopener">{esc(ek["btn"])}</a>\n'
            f'              <a class="plan-consult" href="{esc(em_href)}">{esc(ek["consult"])}</a>\n'
            f'            </article>'
        )
    ent_cards_html = "\n\n".join(ent_parts)

    # Seat add-ons
    sa = d["pricing"]["seat_addons"]
    upg_keys = ["upg_pm", "upg_mu", "upg_pu"]
    sa_cards = []
    for i, uc in enumerate(sa["cards"]):
        ukey = upg_keys[i]
        u_href = stripe.get(f"{ukey}_{def_cur}", stripe[f"{ukey}_AUD"])
        sa_cards.append(
            f'              <div class="addon-card">\n'
            f'                <div>\n'
            f'                  <div class="addon-route"><code>{esc(uc["from"])}</code> <span>→</span> <code class="to">{esc(uc["to"])}</code> <span>{esc(uc["tag"])}</span></div>\n'
            f'                  <p class="addon-desc">{esc(uc["desc"])}</p>\n'
            f'                </div>\n'
            f'                <div class="addon-foot">\n'
            f'                  <div class="addon-price" data-upg-idx="{i}">+<sup>{esc(sym)}</sup><span class="amount">{fmt_num(cur_data["upg"][i])}</span>'
            f'<small data-upg-period>{esc(d["js"]["per_seat_mo"])}</small></div>\n'
            f'                  <a class="addon-btn" data-upg-tier="{ukey}" href="{esc(u_href)}" target="_blank" rel="noopener">{esc(uc["btn"])}</a>\n'
            f'                </div>\n'
            f'              </div>'
        )
    sa_cards_html = "\n".join(sa_cards)

    # Cloud Storage (4 cards)
    st = d["pricing"]["storage"]
    st_keys = ["2t", "6t", "12t", "30t"]
    st_cards = []
    for i, sc in enumerate(st["cards"]):
        skey = st_keys[i]
        is_feat = i == 1
        c_cls = "card plan featured" if is_feat else "card plan"
        b_cls = "btn btn-primary" if is_feat else "btn btn-ghost"
        b_html = f'\n              <span class="badge">{esc(sc["badge"])}</span>' if "badge" in sc else ""
        st_href = stripe.get(f"{skey}_{def_cur}", stripe[f"{skey}_AUD"])
        st_lis = "\n".join(f"                <li>{esc(fl)}</li>" for fl in sc["features"])
        st_cards.append(
            f'            <article class="{c_cls}" style="padding: 26px 22px;">{b_html}\n'
            f'              <div class="plan-tier"><b>{esc(sc["tier_b"])}</b><span>{esc(sc["tier_span"])}</span></div>\n'
            f'              <p class="plan-desc" style="min-height: 2.6em;">{esc(sc["desc"])}</p>\n'
            f'              <div class="price" data-storage-idx="{i}" style="font-size: 1.95rem; white-space: nowrap;">'
            f'<sup>{esc(sym)}</sup><span class="amount">{fmt_num(cur_data["s"][i])}</span><small>{esc(st["per_mo"])}</small></div>\n'
            f'              <p class="price-note">{esc(sc["note"])}</p>\n'
            f'              <ul class="features" style="font-size: .88rem;">\n{st_lis}\n              </ul>\n'
            f'              <a class="{b_cls}" data-stripe-tier="{skey}" href="{esc(st_href)}" target="_blank" rel="noopener">{esc(sc["btn"])}</a>\n'
            f'            </article>'
        )
    st_cards_html = "\n\n".join(st_cards)

    # Process steps
    proc_html = "\n".join(
        f'          <div class="card step">\n'
        f'            <h3>{esc(step["h3"])}</h3>\n'
        f'            <p>{esc(step["p"])}</p>\n'
        f'          </div>'
        for step in d["process"]["steps"]
    )

    # FAQ items
    faq_html = "\n".join(
        f'          <details>\n'
        f'            <summary>{esc(item["q"])}</summary>\n'
        f'            <p>{item["a_html"]}</p>\n'
        f'          </details>'
        for item in d["faq"]["items"]
    )

    # Partner chips
    p_chips_html = "\n".join(f"            <li>{esc(ch)}</li>" for ch in d["partner"]["chips"])

    # JS PRICES object with localized currency names
    js_prices = {}
    for c in CURRENCY_ORDER:
        entry = dict(prices[c])
        entry["name"] = d["pricing"]["currencies"][c]["name"]
        js_prices[c] = entry

    # JS NODES object with coordinates + localized labels
    js_nodes = {}
    for c in NODE_ORDER:
        nd = d["map"]["nodes"][c]
        g = shared["node_geom"][c]
        js_nodes[c] = {
            "name": nd["name"],
            "city": nd["city"],
            "role": nd["role"],
            "route": nd["route"],
            "x": g["x"],
            "y": g["y"],
        }

    js_i18n = {
        "perMonth": d["js"]["per_month"],
        "perYear": d["js"]["per_year"],
        "perSeatMo": d["js"]["per_seat_mo"],
        "perSeatYr": d["js"]["per_seat_yr"],
        "perMoShort": d["js"]["per_mo_short"],
        "perYrShort": d["js"]["per_yr_short"],
        "title12mo": d["js"]["title_12mo"],
        "titleRegMo": d["js"]["title_reg_mo"],
        "noteAnnual": d["js"]["note_annual"],
        "note1xMo": d["js"]["note_1x_mo"],
        "note20xPromo": d["js"]["note_20x_promo"],
        "noteMultMo": d["js"]["note_mult_mo"],
        "entTeamMo": d["js"]["ent_team_mo"],
        "entBizMo": d["js"]["ent_biz_mo"],
        "line0Mo": d["js"]["line_0_mo"],
        "line1Mo": d["js"]["line_1_mo"],
    }

    switcher_js = build_lang_switcher_js(loc["slug"])

    return f"""<!doctype html>
<html lang="{loc["html_lang"]}"{html_dir}>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(d["meta"]["title"])}</title>
  <meta name="description" content="{esc(d["meta"]["description"])}">
  <meta name="keywords" content="{esc(d["meta"]["keywords"])}">
  <meta name="author" content="Zaokit AI">
{hreflang_block}

  <meta property="og:type" content="website">
  <meta property="og:locale" content="{loc["og_locale"]}">
  <meta property="og:site_name" content="Zaokit ClaudeOps">
  <meta property="og:title" content="{esc(d["meta"]["og_title"])}">
  <meta property="og:description" content="{esc(d["meta"]["og_description"])}">
  <meta property="og:url" content="{page_abs_url(loc, "index.html")}">
  <meta property="og:image" content="{SITE_ORIGIN}/hero-card.svg">
  <meta name="theme-color" content="#141210">
  <link rel="icon" href="{asset_prefix}favicon.svg" type="image/svg+xml">
  <link rel="icon" href="{asset_prefix}favicon-32x32.png" sizes="32x32" type="image/png">
  <link rel="icon" href="{asset_prefix}favicon-16x16.png" sizes="16x16" type="image/png">
  <link rel="alternate icon" href="{asset_prefix}favicon.ico" sizes="any">
  <link rel="apple-touch-icon" href="{asset_prefix}apple-touch-icon.png">
{gfont_block}{autoredir_block}
  <script type="application/ld+json">
{ld_indented}
  </script>

  <style>
{css_custom}
{LANG_SWITCHER_CSS}
{INDEX_EXTRA_I18N_CSS}
  </style>
  <script>if(!matchMedia('(prefers-reduced-motion: reduce)').matches)document.documentElement.classList.add('motion')</script>

  <!-- Google Analytics 4 -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0GDE6TX65P"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-0GDE6TX65P');
  </script>
  <script defer src="https://cloud.umami.is/script.js" data-website-id="0731cafa-79de-46ca-bbeb-4e1bf6a04fda"></script>
</head>

<body id="top">
  <header class="site-header">
    <div class="container nav-wrap">
      <a class="brand" href="#top">
        <span class="brand-mark" aria-hidden="true">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l1.9 6.1L20 10l-6.1 1.9L12 18l-1.9-6.1L4 10l6.1-1.9z"/></svg>
        </span>
        {esc(d["nav"]["brand"])}
      </a>
      <ul class="nav-links">
        <li><a href="#why">{esc(d["nav"]["why"])}</a></li>
        <li><a href="#service">{esc(d["nav"]["service"])}</a></li>
        <li><a href="#value">{esc(d["nav"]["value"])}</a></li>
        <li><a href="#security">{esc(d["nav"]["security"])}</a></li>
        <li><a href="#reviews">{esc(d["nav"]["reviews"])}</a></li>
        <li><a href="#pricing">{esc(d["nav"]["pricing"])}</a></li>
        <li><a href="#storage">{esc(d["nav"]["storage"])}</a></li>
        <li><a href="#process">{esc(d["nav"]["process"])}</a></li>
        <li><a href="#faq">{esc(d["nav"]["faq"])}</a></li>
      </ul>
      <div class="header-right">
        {switcher_html}
      </div>
    </div>
  </header>

  <main>
    <!-- Hero -->
    <section class="hero">
      <div class="container">
        <span class="eyebrow"><span class="dot"></span>{esc(d["hero"]["eyebrow"])}</span>
        <h1>{esc(d["hero"]["h1_main"])}<span class="h1-sub"><em>{esc(d["hero"]["h1_sub"])}</em></span></h1>
        <p class="lead">
          {esc(d["hero"]["lead"])}
        </p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="#pricing">{esc(d["hero"]["cta_primary"])}</a>
          <a class="btn btn-ghost" href="{esc(enq_mailto)}">{esc(d["hero"]["cta_secondary"])}</a>
        </div>

        <div class="hero-map-wrap">
          <div class="hero-map-card" id="global-map">
            <div class="map-topbar"><div class="map-status"><span class="live-dot"></span><span>{esc(d["map"]["status_main"])}</span><em>{esc(d["map"]["status_em"])}</em></div><div class="map-meta"><span>{esc(d["map"]["meta_1"])}</span><span class="sep">·</span><span>{esc(d["map"]["meta_2"])}</span><span class="sep">·</span><span>{esc(d["map"]["meta_3"])}</span></div></div>
            <div class="map-body">
              <div class="map-stage" role="img" aria-label="{esc(d["map"]["stage_aria"])}">
{shared["map_bg_block"]}{map_ui_svg}
              </div>
              <div class="map-hud" id="map-hud" aria-live="polite"><div class="map-hud-head"><div class="map-hud-title"><span class="map-hud-code" id="hud-code">AU</span><span class="map-hud-country" id="hud-country">{esc(au_node["name"])}</span></div><span class="map-hud-online">{esc(d["map"]["hud_live"])}</span></div><div class="map-hud-city" id="hud-role">{esc(au_node["role"])}</div><div class="map-hud-rows"><div class="map-hud-row"><span>{esc(d["map"]["hud_label_city"])}</span><b id="hud-city">{esc(au_node["city"])}</b></div><div class="map-hud-row"><span>{esc(d["map"]["hud_label_hw"])}</span><b>{esc(d["map"]["hud_val_hw"])}</b></div><div class="map-hud-row"><span>{esc(d["map"]["hud_label_route"])}</span><b id="hud-route">{esc(au_node["route"])}</b></div></div></div>
            </div>
            <div class="map-pills" role="tablist" aria-label="{esc(d["map"]["pills_aria"])}">
              {map_pills_html}
            </div>
            <div class="map-partner-bar">
              <div class="map-partner-copy">
                <span class="partner-pill">{esc(d["map"]["partner_pill"])}</span>
                <span>{d["map"]["partner_copy_html"]}</span>
              </div>
              <a class="partner-cta-btn" href="{esc(partner_mailto)}">{esc(d["map"]["partner_cta"])}</a>
            </div>
          </div>
        </div>
        <div class="hero-stats">
{stats_html}
        </div>
      </div>
    </section>

    <!-- Pain points -->
    <section class="section section-alt" id="why">
      <div class="container">
        <div class="section-head">
          <p class="section-tag">{esc(d["why"]["tag"])}</p>
          <h2>{esc(d["why"]["h2"])}</h2>
          <p>{esc(d["why"]["sub"])}</p>
        </div>
        <div class="grid grid-4 pain">
{why_cards_html}
        </div>
      </div>
    </section>

    <!-- Service -->
    <section class="section" id="service">
      <div class="container">
        <div class="section-head">
          <p class="section-tag">{esc(d["service"]["tag"])}</p>
          <h2>{esc(d["service"]["h2"])}</h2>
          <p>{esc(d["service"]["sub"])}</p>
        </div>
        <div class="grid grid-4">
{svc_cards_html}
        </div>
      </div>
    </section>

    <!-- Value: beyond compute -->
    <section class="section section-alt" id="value">
      <div class="container">
        <div class="section-head">
          <p class="section-tag">{esc(d["value"]["tag"])}</p>
          <h2>{d["value"]["h2_html"]}</h2>
          <p>{esc(d["value"]["sub"])}</p>
        </div>
        <div class="grid grid-3">
{val_cards_html}
        </div>
      </div>
    </section>

    <!-- Network optimisation -->
    <section class="section net-section" id="network">
      <div class="container net-grid">
        <div class="net-copy">
          <p class="section-tag">{esc(d["network"]["tag"])}</p>
          <h2>{d["network"]["h2_html"]}</h2>
          <p>{esc(d["network"]["p"])}</p>
          <ul class="net-chips">{net_chips_html}</ul>
          <p style="margin: 14px 0 0; font-size: .86rem; color: var(--muted);">{esc(d["network"]["addon_note_prefix"])}<a href="#dedicated-line" style="color: var(--primary-strong); font-weight: 600; border-bottom: 1px dashed rgba(232, 144, 111, .5);">{esc(d["network"]["addon_note_link"])}</a>{esc(d["network"]["addon_note_suffix"])}</p>
        </div>
        <div class="card net-card" aria-label="{esc(d["network"]["card_aria"])}">
          <div class="net-legend"><span class="lg before">{esc(d["network"]["legend_before"])}</span><span class="lg after">{esc(d["network"]["legend_after"])}</span></div>
{net_rows_html}
          <p class="net-foot">{esc(d["network"]["foot"])}</p>
        </div>
      </div>
    </section>

    <!-- Security & Privacy -->
    <section class="section" id="security">
      <div class="container">
        <div class="section-head">
          <p class="section-tag">{esc(d["security"]["tag"])}</p>
          <h2>{esc(d["security"]["h2"])}</h2>
          <p>{esc(d["security"]["sub"])}</p>
        </div>
        <div class="grid grid-3">
{sec_cards_html}
        </div>
      </div>
    </section>

    <!-- User Reviews -->
    <section class="section section-alt" id="reviews">
      <div class="container">
        <div class="section-head">
          <p class="section-tag">{esc(d["reviews"]["tag"])}</p>
          <h2>{esc(d["reviews"]["h2"])}</h2>
          <p>{esc(d["reviews"]["sub"])}</p>
        </div>
        <div class="grid grid-3">
{reviews_html}
        </div>
        <p class="reviews-note">{esc(d["reviews"]["note"])}</p>
      </div>
    </section>

    <!-- Pricing -->
    <section class="section" id="pricing">
      <div class="container">
        <div class="section-head">
          <p class="section-tag">{esc(d["pricing"]["tag"])}</p>
          <h2>{esc(d["pricing"]["h2"])}</h2>
          <p>{d["pricing"]["sub_html"]}<a class="enterprise-jump" href="#dedicated-line">{esc(d["pricing"]["jump_line"])}</a><a class="enterprise-jump" href="#pricing-enterprise">{esc(d["pricing"]["jump_ent"])}</a></p>
        </div>
        <div class="pricing-controls">
          <div class="billing-switch" role="group" aria-label="{esc(d["pricing"]["billing_aria"])}">
            <button type="button" data-billing="month" aria-pressed="true">{esc(d["pricing"]["billing_month"])}</button>
            <button type="button" data-billing="year" aria-pressed="false">{esc(d["pricing"]["billing_year"])} <span class="save-badge">{esc(d["pricing"]["billing_save_badge"])}</span></button>
          </div>
          <div class="currency-switch" role="group" aria-label="{esc(d["pricing"]["currency_aria"])}">
{cur_btns_html}
          </div>
        </div>
        <div class="grid grid-3 pricing pricing-solo">
{solo_html}
        </div>

        <!-- ClaudeOps Enterprise Dedicated Line Value-Added Service -->
        <div class="seat-addons line-addons" id="dedicated-line">
          <div class="seat-addons-head">
            <h3>{esc(dl["h3_main"])} <span class="addon-pill">{esc(dl["h3_pill"])}</span></h3>
            <p>{esc(dl["sub"])}</p>
          </div>
          <div class="line-grid">
{dl_cards_html}
          </div>
        </div>

        <!-- Team & Business Plans -->
        <div class="enterprise-wrap" id="pricing-enterprise">
          <div class="tier-divider"><span>{esc(ent["divider"])}</span></div>
          <div class="enterprise-toolbar">
            <div class="seat-tier-switch" role="group" aria-label="{esc(ent["switch_aria"])}">
              <button type="button" data-seat-tier="pro" aria-pressed="false">{esc(ent["tier_pro"])}</button>
              <button type="button" data-seat-tier="max" aria-pressed="true">{esc(ent["tier_max"])} <span class="save-badge">{esc(ent["tier_max_badge"])}</span></button>
              <button type="button" data-seat-tier="ultra" aria-pressed="false">{esc(ent["tier_ultra"])}</button>
            </div>
            <p>{ent["toolbar_html"]}</p>
          </div>
          <div class="grid grid-2 pricing pricing-enterprise">
{ent_cards_html}
          </div>

          <!-- Per-Seat Self-Serve Upgrade Add-ons -->
          <div class="seat-addons">
            <div class="seat-addons-head">
              <h3>{esc(sa["h3_main"])} <span class="addon-pill">{esc(sa["h3_pill"])}</span></h3>
              <p>{esc(sa["sub"])}</p>
            </div>
            <div class="addon-grid">
{sa_cards_html}
            </div>
          </div>
        </div>

        <!-- Cloud Storage (Google Drive & iCloud) -->
        <div id="storage" style="margin-top: 64px; padding-top: 48px; border-top: 1px solid var(--border);">
          <div class="section-head" style="margin-bottom: 32px;">
            <p class="section-tag">{esc(st["tag"])}</p>
            <h2>{esc(st["h2"])}</h2>
            <p>{st["sub_html"]}</p>
          </div>
          <div class="currency-switch" role="group" aria-label="{esc(st["currency_aria"])}" style="margin: 0 auto 32px">
{cur_btns_html}
          </div>
          <div class="grid grid-4 pricing">
{st_cards_html}
          </div>
        </div>
        <div class="stripe-trust">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
          <span>{d["pricing"]["stripe_trust_html"]}</span>
        </div>
        <p class="pricing-foot">{esc(d["pricing"]["foot_before_currency"])}<span id="currency-name">{esc(d["pricing"]["currencies"][def_cur]["name"])}</span>{esc(d["pricing"]["foot_after_currency"])}<span data-promo-foot>{esc(d["pricing"]["foot_promo"])}</span>{esc(d["pricing"]["foot_legal_prefix"])}<a href="terms.html" style="color:var(--primary-strong)">{esc(d["pricing"]["foot_terms_link"])}</a>{esc(d["pricing"]["foot_legal_mid"])}<a href="refund.html" style="color:var(--primary-strong)">{esc(d["pricing"]["foot_refund_link"])}</a>{esc(d["pricing"]["foot_legal_suffix"])}</p>
      </div>
    </section>

    <!-- Process -->
    <section class="section section-alt" id="process">
      <div class="container">
        <div class="section-head">
          <p class="section-tag">{esc(d["process"]["tag"])}</p>
          <h2>{esc(d["process"]["h2"])}</h2>
        </div>
        <div class="grid grid-4 steps">
{proc_html}
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="section" id="faq">
      <div class="container">
        <div class="section-head">
          <p class="section-tag">{esc(d["faq"]["tag"])}</p>
          <h2>{esc(d["faq"]["h2"])}</h2>
        </div>
        <div class="faq">
{faq_html}
        </div>
      </div>
    </section>

    <!-- Global Partner & CTA -->
    <section class="section">
      <div class="container">
        <div class="partner-banner" id="partner">
          <span class="eyebrow"><span class="dot"></span>{esc(d["partner"]["eyebrow"])}</span>
          <h2>{d["partner"]["h2_html"]}</h2>
          <p>
            {d["partner"]["p_html"]}
          </p>
          <ul class="partner-chips">
{p_chips_html}
          </ul>
          <div class="hero-actions">
            <a class="btn btn-primary" href="{esc(partner_mailto)}">{esc(d["partner"]["btn"])}</a>
          </div>
        </div>

        <div class="cta">
          <h2>{esc(d["cta"]["h2"])}</h2>
          <p>{esc(d["cta"]["p"])}</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="#pricing">{esc(d["cta"]["btn_primary"])}</a>
            <a class="btn btn-ghost" href="{esc(enq_mailto)}">{esc(d["cta"]["btn_secondary"])}</a>
          </div>
          <div class="contact-tg">
            <a class="tg-qr" href="https://t.me/letcode2020" target="_blank" rel="noopener" aria-label="{esc(d["cta"]["tg_qr_aria"])}">
              <img src="{asset_prefix}telegram-qr.jpg" width="158" height="210" alt="{esc(d["cta"]["tg_qr_alt"])}" loading="lazy">
            </a>
            <div class="tg-text">
              <h3>{esc(d["cta"]["tg_h3"])}</h3>
              <p>{esc(d["cta"]["tg_p"])}</p>
              <a class="tg-link" href="https://t.me/letcode2020" target="_blank" rel="noopener">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M21.9 4.3 18.7 19.4c-.2 1.1-.9 1.3-1.8.8l-4.9-3.6-2.4 2.3c-.3.3-.5.5-1 .5l.3-5 9.1-8.2c.4-.4-.1-.6-.6-.2L6.2 13 1.4 11.5c-1-.3-1.1-1 .2-1.5L20.5 2.7c.9-.3 1.7.2 1.4 1.6z"/></svg>
                @letcode2020
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer>
    <div class="container foot">
      <div class="foot-brand">
        <strong>{esc(d["footer"]["brand"])}</strong>
        <span class="foot-entity">{esc(d["footer"]["entity"])}</span>
        <span>{esc(d["footer"]["contact_label"])}<a href="mailto:jason2023zhang@gmail.com">jason2023zhang@gmail.com</a> ({esc(d["footer"]["alt_label"])}<a href="mailto:support@zaokit.ai">support@zaokit.ai</a>)</span>
        <span class="foot-copy">© <span id="year"></span> Zaokit AI. {esc(d["footer"]["rights"])}</span>
      </div>
      <div class="foot-right">
        <div class="foot-col">
          <h4>{esc(d["footer"]["products_h4"])}</h4>
          <ul>
            <li><a href="https://zaokit.app" target="_blank" rel="noopener">Zaokit AIPPT</a></li>
            <li><a href="https://cowork.zaokit.app" target="_blank" rel="noopener">Zaokit Cowork</a></li>
            <li><a href="https://edu.zaokit.app" target="_blank" rel="noopener">Zaokit AI Edu</a></li>
            <li><a href="https://cc.zaokit.com/" target="_blank" rel="noopener">Zaokit CC</a></li>
            <li><a href="https://cx.zaokit.com/" target="_blank" rel="noopener">Zaokit CX</a></li>
          </ul>
        </div>
        <div class="foot-col">
          <h4>{esc(d["footer"]["follow_h4"])}</h4>
          <div class="social">
            <a href="https://discord.gg/HDjD6g5mdw" target="_blank" rel="noopener" aria-label="Discord" title="Discord"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.3 4.4A19.8 19.8 0 0 0 15.4 3l-.6 1.3a18.4 18.4 0 0 0-5.6 0L8.6 3a19.7 19.7 0 0 0-4.9 1.4C.6 9 0 13.6.3 18.1a19.9 19.9 0 0 0 6 3l1.3-2a12.9 12.9 0 0 1-2-1l.5-.4a14.2 14.2 0 0 0 12 0l.5.4-2 1 1.3 2a19.8 19.8 0 0 0 6-3c.5-5.2-.9-9.8-3.6-13.7zM8.5 15.4c-1.2 0-2.2-1.1-2.2-2.4s1-2.4 2.2-2.4 2.2 1.1 2.2 2.4-1 2.4-2.2 2.4zm7 0c-1.2 0-2.2-1.1-2.2-2.4s1-2.4 2.2-2.4 2.2 1.1 2.2 2.4-1 2.4-2.2 2.4z"/></svg></a>
            <a href="https://x.com/Zaokit_AI_Agent" target="_blank" rel="noopener" aria-label="X (Twitter)" title="X (Twitter)"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18.2 2h3.4l-7.4 8.5L23 22h-6.8l-5.3-7-6.1 7H1.4l7.9-9L1 2h7l4.8 6.4zm-1.2 18h1.9L7.1 3.9H5.1z"/></svg></a>
            <a href="https://www.youtube.com/@zaokitai" target="_blank" rel="noopener" aria-label="YouTube" title="YouTube"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.3 3.6z"/></svg></a>
            <a href="https://t.me/letcode2020" target="_blank" rel="noopener" aria-label="Telegram" title="Telegram"><svg width="17" height="17" viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3 18.7 19.4c-.2 1.1-.9 1.3-1.8.8l-4.9-3.6-2.4 2.3c-.3.3-.5.5-1 .5l.3-5 9.1-8.2c.4-.4-.1-.6-.6-.2L6.2 13 1.4 11.5c-1-.3-1.1-1 .2-1.5L20.5 2.7c.9-.3 1.7.2 1.4 1.6z"/></svg></a>
          </div>
        </div>
      </div>
    </div>
    <div class="container foot-disclaimer">
      <div class="foot-legal"><a href="terms.html">{esc(d["footer"]["terms"])}</a><a href="refund.html">{esc(d["footer"]["refund"])}</a><a href="privacy.html">{esc(d["footer"]["privacy"])}</a></div>
      {esc(d["footer"]["disclaimer"])}
    </div>
  </footer>

  <div class="toast" id="toast" role="status" aria-live="polite"></div>

{switcher_js}

  <script>
    (function () {{
      var PRICES = {json.dumps(js_prices, ensure_ascii=False)};
      var STRIPE_LINKS = {json.dumps(stripe, ensure_ascii=False)};
      var ENT_COPY = {json.dumps(d["js"]["ent_copy"], ensure_ascii=False)};
      var I18N = {json.dumps(js_i18n, ensure_ascii=False)};
      var DEFAULT_CURRENCY = {json.dumps(def_cur)};
      var TIER_IDX = {{ pro: 0, max: 1, ultra: 2 }};
      var MULT = [1, 5, 20];
      var SOLO_ANNUAL = {{ '1x': true, '5x': true, '20x': true }};
      var PROMO_ACTIVE = Date.now() < Date.parse('2027-01-01T00:00:00+11:00');
      if (!PROMO_ACTIVE) {{
        document.querySelectorAll('.badge-promo, [data-promo-foot]').forEach(function (el) {{ el.remove(); }});
      }}
      var curCode = DEFAULT_CURRENCY;
      var curBilling = 'month';
      var curSeatTier = 'max';

      function fmt(n) {{ return n.toLocaleString('en-AU'); }}
      function tpl(s, v) {{
        return String(s).replace(/\\{{(\\w+)\\}}/g, function (_, k) {{ return v[k] != null ? v[k] : ''; }});
      }}
      function renderPricing() {{
        var c = PRICES[curCode] || PRICES.AUD;
        var isYear = curBilling === 'year';
        var tIdx = TIER_IDX[curSeatTier] != null ? TIER_IDX[curSeatTier] : 1;
        var ec = ENT_COPY[curSeatTier] || ENT_COPY.max;

        document.querySelectorAll('[data-plan-idx]').forEach(function (el) {{
          var i = +el.getAttribute('data-plan-idx');
          var mo = c.p[i];
          var val = isYear ? mo * 10 : mo;
          el.querySelector('sup').textContent = c.sym;
          el.querySelector('.amount').textContent = fmt(val);
          var perEl = el.querySelector('[data-period]');
          if (perEl) perEl.textContent = isYear ? I18N.perYear : I18N.perMonth;
          var origEl = el.querySelector('[data-orig-idx]');
          if (origEl) {{
            if (isYear) {{
              origEl.textContent = c.sym + fmt(mo * 12);
              origEl.setAttribute('title', I18N.title12mo);
              origEl.style.display = 'inline';
            }} else if (i === 2 && PROMO_ACTIVE && c.orig20x) {{
              origEl.textContent = c.sym + fmt(c.orig20x);
              origEl.setAttribute('title', I18N.titleRegMo);
              origEl.style.display = 'inline';
            }} else {{
              origEl.style.display = 'none';
            }}
          }}
        }});
        document.querySelectorAll('[data-note-idx]').forEach(function (el) {{
          var i = +el.getAttribute('data-note-idx');
          var mo = c.p[i];
          el.classList.toggle('annual-note', isYear);
          if (isYear) {{
            var eqMo = mo * 10 / 12;
            var eqStr = eqMo >= 100 ? fmt(Math.round(eqMo)) : (+eqMo.toFixed(1)).toString();
            el.textContent = tpl(I18N.noteAnnual, {{ sym: c.sym, eq: eqStr, save: fmt(mo * 2) }});
          }} else if (i === 0) {{
            var day = c.p[0] / 30;
            var dayStr = (day >= 10 ? Math.round(day) : +day.toFixed(1)).toString();
            el.textContent = tpl(I18N.note1xMo, {{ sym: c.sym, day: dayStr }});
          }} else if (i === 2 && PROMO_ACTIVE) {{
            var ratio2 = Math.round(c.p[2] / (c.p[0] * MULT[2]) * 100);
            el.textContent = tpl(I18N.note20xPromo, {{ ratio: ratio2 }});
          }} else {{
            var ratio = Math.round(c.p[i] / (c.p[0] * MULT[i]) * 100);
            el.textContent = tpl(I18N.noteMultMo, {{ mult: MULT[i], ratio: ratio }});
          }}
        }});
        document.querySelectorAll('[data-stripe-tier]').forEach(function (btn) {{
          var tier = btn.getAttribute('data-stripe-tier');
          var keyPrefix = (isYear && SOLO_ANNUAL[tier]) ? (tier + '_yr') : tier;
          var link = STRIPE_LINKS[keyPrefix + '_' + curCode] || STRIPE_LINKS[keyPrefix + '_AUD'];
          if (link) btn.setAttribute('href', link);
        }});

        ['team', 'biz'].forEach(function (kind) {{
          var entMo = c[kind][tIdx];
          var entVal = isYear ? entMo * 10 : entMo;
          var priceEl = document.querySelector('[data-ent-price="' + kind + '"]');
          if (priceEl) {{
            priceEl.querySelector('sup').textContent = c.sym;
            priceEl.querySelector('.amount').textContent = fmt(entVal);
            var pPer = priceEl.querySelector('[data-period]');
            if (pPer) pPer.textContent = isYear ? I18N.perYear : I18N.perMonth;
            var origEl = priceEl.querySelector('[data-ent-orig]');
            if (origEl) {{
              if (isYear) {{
                origEl.textContent = c.sym + fmt(entMo * 12);
                origEl.setAttribute('title', I18N.title12mo);
                origEl.style.display = 'inline';
              }} else {{
                origEl.style.display = 'none';
              }}
            }}
          }}
          var badgeEl = document.querySelector('[data-ent-badge="' + kind + '"]');
          if (badgeEl) badgeEl.textContent = kind === 'team' ? ec.teamBadge : ec.bizBadge;
          var seatLi = document.querySelector('[data-ent-seat-li="' + kind + '"]');
          if (seatLi) seatLi.innerHTML = kind === 'team' ? ec.teamSeatLi : ec.bizSeatLi;
          var stLi = document.querySelector('[data-ent-storage-li="' + kind + '"]');
          if (stLi) stLi.textContent = kind === 'team' ? ec.teamStorage : ec.bizStorage;
          var noteEl = document.querySelector('[data-ent-note="' + kind + '"]');
          if (noteEl) {{
            noteEl.classList.toggle('annual-note', isYear);
            if (isYear) {{
              var eqEnt = entMo * 10 / 12;
              noteEl.textContent = tpl(I18N.noteAnnual, {{ sym: c.sym, eq: fmt(Math.round(eqEnt)), save: fmt(entMo * 2) }});
            }} else if (kind === 'team') {{
              noteEl.textContent = tpl(I18N.entTeamMo, {{ label: ec.label }});
            }} else {{
              noteEl.textContent = tpl(I18N.entBizMo, {{ label: ec.label }});
            }}
          }}
          var entBtn = document.querySelector('[data-ent-btn="' + kind + '"]');
          if (entBtn) {{
            var kPref = kind + '_' + curSeatTier + (isYear ? '_yr' : '');
            var eLink = STRIPE_LINKS[kPref + '_' + curCode] || STRIPE_LINKS[kPref + '_AUD'];
            if (eLink) entBtn.setAttribute('href', eLink);
          }}
        }});

        document.querySelectorAll('[data-upg-idx]').forEach(function (el) {{
          var i = +el.getAttribute('data-upg-idx');
          var umo = c.upg[i];
          el.querySelector('sup').textContent = c.sym;
          el.querySelector('.amount').textContent = fmt(isYear ? umo * 10 : umo);
          var uPer = el.querySelector('[data-upg-period]');
          if (uPer) uPer.textContent = isYear ? I18N.perSeatYr : I18N.perSeatMo;
        }});
        document.querySelectorAll('[data-upg-tier]').forEach(function (btn) {{
          var ut = btn.getAttribute('data-upg-tier') + (isYear ? '_yr' : '');
          var uLink = STRIPE_LINKS[ut + '_' + curCode] || STRIPE_LINKS[ut + '_AUD'];
          if (uLink) btn.setAttribute('href', uLink);
        }});

        document.querySelectorAll('[data-line-idx]').forEach(function (el) {{
          var i = +el.getAttribute('data-line-idx');
          var lmo = c.line[i];
          el.querySelector('sup').textContent = c.sym;
          el.querySelector('.amount').textContent = fmt(isYear ? lmo * 10 : lmo);
          var lPer = el.querySelector('[data-line-period]');
          if (lPer) lPer.textContent = isYear ? I18N.perYrShort : I18N.perMoShort;
          var lOrig = el.querySelector('[data-line-orig]');
          if (lOrig) {{
            if (isYear) {{
              lOrig.textContent = c.sym + fmt(lmo * 12);
              lOrig.style.display = 'inline';
            }} else {{
              lOrig.style.display = 'none';
            }}
          }}
        }});
        document.querySelectorAll('[data-line-note]').forEach(function (el) {{
          var i = +el.getAttribute('data-line-note');
          var lmo = c.line[i];
          el.classList.toggle('annual-note', isYear);
          if (isYear) {{
            var eqL = (+(lmo * 10 / 12).toFixed(1)).toString();
            el.textContent = tpl(I18N.noteAnnual, {{ sym: c.sym, eq: eqL, save: fmt(lmo * 2) }});
          }} else {{
            el.textContent = i === 0 ? I18N.line0Mo : I18N.line1Mo;
          }}
        }});
        document.querySelectorAll('[data-line-tier]').forEach(function (btn) {{
          var lt = btn.getAttribute('data-line-tier') + (isYear ? '_yr' : '');
          var lLink = STRIPE_LINKS[lt + '_' + curCode] || STRIPE_LINKS[lt + '_AUD'];
          if (lLink) btn.setAttribute('href', lLink);
        }});

        document.querySelectorAll('[data-storage-idx]').forEach(function (el) {{
          var i = +el.getAttribute('data-storage-idx');
          var sc = c.s ? c : PRICES.AUD;
          el.querySelector('sup').textContent = sc.sym;
          var v = sc.s[i];
          el.querySelector('.amount').textContent = v % 1 ? v.toFixed(2) : fmt(v);
        }});

        var curNameEl = document.getElementById('currency-name');
        if (curNameEl) curNameEl.textContent = c.name;
        document.querySelectorAll('[data-currency]').forEach(function (b) {{
          b.setAttribute('aria-pressed', b.getAttribute('data-currency') === curCode ? 'true' : 'false');
        }});
        document.querySelectorAll('[data-billing]').forEach(function (b) {{
          b.setAttribute('aria-pressed', b.getAttribute('data-billing') === curBilling ? 'true' : 'false');
        }});
        document.querySelectorAll('[data-seat-tier]').forEach(function (b) {{
          b.setAttribute('aria-pressed', b.getAttribute('data-seat-tier') === curSeatTier ? 'true' : 'false');
        }});
      }}

      function setCurrency(code) {{
        curCode = PRICES[code] ? code : DEFAULT_CURRENCY;
        renderPricing();
        try {{ localStorage.setItem('claude-ops-currency', curCode); }} catch (e) {{}}
      }}
      function setBilling(mode) {{
        curBilling = mode === 'year' ? 'year' : 'month';
        renderPricing();
        try {{ localStorage.setItem('claude-ops-billing', curBilling); }} catch (e) {{}}
      }}
      function setSeatTier(tier) {{
        curSeatTier = TIER_IDX[tier] != null ? tier : 'max';
        renderPricing();
        try {{ localStorage.setItem('claude-ops-seat-tier', curSeatTier); }} catch (e) {{}}
      }}

      document.querySelectorAll('[data-currency]').forEach(function (b) {{
        b.addEventListener('click', function () {{ setCurrency(b.getAttribute('data-currency')); }});
      }});
      document.querySelectorAll('[data-billing]').forEach(function (b) {{
        b.addEventListener('click', function () {{ setBilling(b.getAttribute('data-billing')); }});
      }});
      document.querySelectorAll('[data-seat-tier]').forEach(function (b) {{
        b.addEventListener('click', function () {{ setSeatTier(b.getAttribute('data-seat-tier')); }});
      }});

      (function initPricing() {{
        var params = new URLSearchParams(location.search);
        var bq = (params.get('billing') || '').toLowerCase();
        if (bq === 'year' || bq === 'annual') curBilling = 'year';
        else if (bq === 'month' || bq === 'monthly') curBilling = 'month';
        else {{
          try {{
            var sb = localStorage.getItem('claude-ops-billing');
            if (sb === 'year' || sb === 'month') curBilling = sb;
          }} catch (e) {{}}
        }}

        var sq = (params.get('tier') || '').toLowerCase();
        if (TIER_IDX[sq] != null) curSeatTier = sq;
        else {{
          try {{
            var st = localStorage.getItem('claude-ops-seat-tier');
            if (TIER_IDX[st] != null) curSeatTier = st;
          }} catch (e) {{}}
        }}

        var q = (params.get('currency') || '').toUpperCase();
        if (PRICES[q]) return setCurrency(q);
        var saved = null;
        try {{ saved = localStorage.getItem('claude-ops-currency'); }} catch (e) {{}}
        if (saved && PRICES[saved]) return setCurrency(saved);
        var lang = (navigator.language || '').toLowerCase();
        if (/-au$/.test(lang)) return setCurrency('AUD');
        if (/-nz$/.test(lang)) return setCurrency('NZD');
        if (/-ca$/.test(lang)) return setCurrency('CAD');
        if (/-us$/.test(lang)) return setCurrency('USD');
        if (/-sg$/.test(lang)) return setCurrency('SGD');
        if (/^(de|fr|es|it|nl|pt-pt|fi|el|ie)/.test(lang) || /-(de|fr|es|it|nl|at|be|ie|fi|pt|gr)$/.test(lang)) return setCurrency('EUR');
        setCurrency(DEFAULT_CURRENCY);
      }})();
      document.getElementById('year').textContent = new Date().getFullYear();
    }})();
  </script>

  <script>
  (function () {{
    function trackEvent(name, params) {{
      params = params || {{}};
      try {{ if (typeof gtag === 'function') gtag('event', name, params); }} catch (e) {{}}
      try {{ if (window.umami && typeof umami.track === 'function') umami.track(name, params); }} catch (e) {{}}
    }}
    function isMail(a) {{ var h = a.getAttribute('href') || ''; return h.indexOf('mailto:') === 0 || h.indexOf('/cdn-cgi/l/email-protection') === 0; }}
    function currentCurrency() {{
      var b = document.querySelector('[data-currency][aria-pressed="true"]');
      return b ? b.getAttribute('data-currency') : 'AUD';
    }}
    document.addEventListener('click', function (e) {{
      var cur = e.target.closest('[data-currency]');
      if (cur) {{ trackEvent('currency_switch', {{ currency: cur.getAttribute('data-currency') }}); return; }}
      var a = e.target.closest('a');
      if (!a) return;
      if (a.hasAttribute('data-stripe-tier') || a.hasAttribute('data-ent-btn') || a.hasAttribute('data-upg-tier') || a.hasAttribute('data-line-tier')) {{
        var stripeTier = a.getAttribute('data-stripe-tier') || a.getAttribute('data-ent-btn') || a.getAttribute('data-upg-tier') || a.getAttribute('data-line-tier');
        var checkoutParams = {{
          plan: stripeTier,
          currency: currentCurrency(),
          stripe_mode: window.__CLAUDEOPS_STRIPE_MODE__ || 'live',
          location: 'pricing'
        }};
        trackEvent('begin_checkout', checkoutParams);
        trackEvent('stripe_checkout_click', checkoutParams);
        return;
      }}
      if (a.closest('footer') && /^https?:/.test(a.getAttribute('href') || '') && (a.getAttribute('href') || '').indexOf('https://t.me/') !== 0) {{
        trackEvent('footer_outbound_click', {{ url: a.getAttribute('href') }});
        return;
      }}
      if ((a.getAttribute('href') || '').indexOf('https://t.me/') === 0) {{
        trackEvent('telegram_click', {{ location: a.classList.contains('tg-qr') ? 'qr' : 'button' }});
        trackEvent('generate_lead', {{ plan: 'general', currency: currentCurrency(), location: 'telegram' }});
        return;
      }}
      if (isMail(a)) {{
        var plan = a.closest('.plan');
        var tier = plan ? plan.querySelector('.plan-tier b').textContent.trim() : 'general';
        var loc = plan ? 'pricing' : (a.closest('.hero') ? 'hero' : (a.closest('.cta') ? 'cta' : 'other'));
        var params = {{ plan: tier, currency: currentCurrency(), location: loc }};
        trackEvent('consult_click', params);
        trackEvent('generate_lead', params);
      }} else if ((a.getAttribute('href') || '') === '#pricing') {{
        trackEvent('view_pricing_click', {{ location: a.closest('.hero') ? 'hero' : (a.closest('.cta') ? 'cta' : 'nav') }});
      }}
    }}, true);
  }})();
  </script>

  <script>
  (function () {{
    var EMAIL = 'jason2023zhang@gmail.com';
    var TPL_OK = {json.dumps(d["js"]["toast_copied"], ensure_ascii=False)};
    var TPL_FAIL = {json.dumps(d["js"]["toast_fallback"], ensure_ascii=False)};
    var toastEl = document.getElementById('toast'), timer;
    function toast(msg) {{
      if (!toastEl) return;
      toastEl.textContent = msg; toastEl.classList.add('show');
      clearTimeout(timer); timer = setTimeout(function () {{ toastEl.classList.remove('show'); }}, 3200);
    }}
    function fallbackCopy(text) {{
      var ta = document.createElement('textarea');
      ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      var ok = false; try {{ ok = document.execCommand('copy'); }} catch (e) {{}}
      document.body.removeChild(ta); return ok;
    }}
    function copyEmail(addr) {{
      var target = addr || EMAIL;
      var okMsg = TPL_OK.replace('{{email}}', target);
      var failMsg = TPL_FAIL.replace('{{email}}', target);
      var done = function () {{ toast(okMsg); }};
      var fail = function () {{ toast(fallbackCopy(target) ? okMsg : failMsg); }};
      if (navigator.clipboard && window.isSecureContext) {{
        navigator.clipboard.writeText(target).then(done, fail);
      }} else {{ fail(); }}
    }}
    document.addEventListener('click', function (e) {{
      var a = e.target.closest('a[href^="mailto:"]');
      if (a) {{
        var m = (a.getAttribute('href') || '').replace(/^mailto:/i, '').split('?')[0];
        copyEmail(m);
      }}
    }});
  }})();
  </script>
  <script>
  (function () {{
    var card = document.querySelector('.net-card');
    if (!card) return;
    if (!('IntersectionObserver' in window)) {{ card.classList.add('in'); return; }}
    var io = new IntersectionObserver(function (es) {{
      es.forEach(function (e) {{ if (e.isIntersecting) {{ card.classList.add('in'); io.disconnect(); }} }});
    }}, {{ threshold: 0.35 }});
    io.observe(card);
  }})();
  </script>
  <script>
  (function () {{
    var root = document.documentElement;
    var header = document.querySelector('.site-header');
    var navList = document.querySelector('.nav-links');
    var bar = document.createElement('div'); bar.id = 'scroll-progress'; document.body.appendChild(bar);
    var ticking = false;

    function docTop(el) {{
      var y = 0;
      while (el) {{ y += el.offsetTop || 0; el = el.offsetParent; }}
      return y;
    }}

    var navItems = [];
    var navById = {{}};
    if (navList) {{
      Array.prototype.slice.call(navList.querySelectorAll('a[href^="#"]')).forEach(function (link) {{
        var id = link.getAttribute('href').slice(1);
        var el = id ? document.getElementById(id) : null;
        if (el) {{
          var item = {{ id: id, link: link, el: el }};
          navItems.push(item);
          navById[id] = item;
        }}
      }});
    }}

    var currentNavId = null;
    var lockedNavId = null;
    var lockTargetY = 0;
    var lockExpire = 0;

    function applyNavIndicator(activeId, forceMeasure) {{
      if (!navList) return;
      if (activeId === currentNavId && !forceMeasure) return;
      currentNavId = activeId;
      var activeItem = activeId ? navById[activeId] : null;
      navItems.forEach(function (item) {{
        var on = item === activeItem;
        item.link.classList.toggle('is-active', on);
        if (on) item.link.setAttribute('aria-current', 'location');
        else item.link.removeAttribute('aria-current');
      }});
      if (activeItem) {{
        var link = activeItem.link;
        var pad = 8;
        var x = link.offsetLeft + pad;
        var w = Math.max(16, link.offsetWidth - pad * 2);
        navList.style.setProperty('--ind-x', x + 'px');
        navList.style.setProperty('--ind-w', w + 'px');
        navList.style.setProperty('--ind-o', '1');
      }} else {{
        navList.style.setProperty('--ind-o', '0');
      }}
    }}

    function computeActiveNavId(scrollTop, maxScroll) {{
      if (!navItems.length) return null;
      if (lockedNavId) {{
        if (Date.now() <= lockExpire && Math.abs(scrollTop - lockTargetY) > 8) {{
          return lockedNavId;
        }}
        if (maxScroll > 0 && lockTargetY >= maxScroll - 4 && scrollTop >= maxScroll - 8) {{
          return lockedNavId;
        }}
        lockedNavId = null;
      }}
      if (maxScroll > 0 && scrollTop >= maxScroll - 20) {{
        return navItems[navItems.length - 1].id;
      }}
      var headerH = header ? header.offsetHeight : 68;
      var probeY = scrollTop + headerH + Math.min(140, Math.round(innerHeight * 0.2));
      var chosen = null;
      for (var i = 0; i < navItems.length; i++) {{
        if (docTop(navItems[i].el) <= probeY) chosen = navItems[i].id;
      }}
      return chosen;
    }}

    function clearNavLock() {{ lockedNavId = null; }}
    addEventListener('wheel', clearNavLock, {{ passive: true }});
    addEventListener('touchmove', clearNavLock, {{ passive: true }});

    function onScroll() {{
      var scrollTop = root.scrollTop;
      var max = root.scrollHeight - root.clientHeight;
      var activeId = computeActiveNavId(scrollTop, max);
      bar.style.transform = 'scaleX(' + (max > 0 ? scrollTop / max : 0) + ')';
      if (header) header.classList.toggle('scrolled', scrollTop > 12);
      applyNavIndicator(activeId, false);
      ticking = false;
    }}
    addEventListener('scroll', function () {{ if (!ticking) {{ ticking = true; requestAnimationFrame(onScroll); }} }}, {{ passive: true }});
    addEventListener('resize', function () {{
      var max = root.scrollHeight - root.clientHeight;
      applyNavIndicator(computeActiveNavId(root.scrollTop, max), true);
    }}, {{ passive: true }});
    if (document.fonts && document.fonts.ready) {{
      document.fonts.ready.then(function () {{ applyNavIndicator(currentNavId, true); }});
    }}
    onScroll();

    function clearReveal(container) {{
      if (!container) return;
      if (container.classList && container.classList.contains('mo-reveal')) {{
        container.classList.remove('mo-reveal', 'mo-in');
        container.style.transitionDelay = '';
      }}
      container.querySelectorAll('.mo-reveal').forEach(function (el) {{
        el.classList.remove('mo-reveal', 'mo-in');
        el.style.transitionDelay = '';
      }});
    }}

    document.querySelectorAll('a[href="#top"]').forEach(function (el) {{
      el.addEventListener('click', function (e) {{
        e.preventDefault();
        lockedNavId = null;
        window.scrollTo({{ top: 0, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth' }});
        if (location.hash) history.replaceState(null, '', location.pathname + location.search);
      }});
    }});

    function scrollToPricing(smooth) {{
      var sec = document.getElementById('pricing');
      if (!sec) return 0;
      clearReveal(sec);
      var headerH = header ? header.offsetHeight : 68;
      var headEl = sec.querySelector('.section-head') || sec;
      var gridEl = sec.querySelector('.pricing-solo') || sec.querySelector('.pricing');
      var idealTop = docTop(headEl) - headerH - 12;
      var targetY = idealTop;
      if (gridEl) {{
        var plans = Array.prototype.slice.call(gridEl.querySelectorAll('.plan'));
        if (plans.length) {{
          var checkPlans = innerWidth <= 960
            ? [plans.reduce(function (a, b) {{ return docTop(a) <= docTop(b) ? a : b; }})]
            : plans;
          var maxBtnBottom = 0;
          checkPlans.forEach(function (p) {{
            var btn = p.querySelector('.btn');
            if (btn) maxBtnBottom = Math.max(maxBtnBottom, docTop(btn) + btn.offsetHeight);
          }});
          if (maxBtnBottom > 0) {{
            var neededBottom = maxBtnBottom + 16;
            if (neededBottom - idealTop > innerHeight) {{
              targetY = neededBottom - innerHeight;
            }}
          }}
        }}
      }}
      var maxScroll = Math.max(0, root.scrollHeight - root.clientHeight);
      var destY = Math.max(0, Math.min(targetY, maxScroll));
      window.scrollTo({{
        top: destY,
        behavior: smooth && !matchMedia('(prefers-reduced-motion: reduce)').matches ? 'smooth' : 'instant'
      }});
      return destY;
    }}

    function scrollToSection(id, smooth) {{
      if (id === 'pricing') return scrollToPricing(smooth);
      var sec = document.getElementById(id);
      if (!sec) return null;
      clearReveal(sec);
      var headerH = header ? header.offsetHeight : 68;
      var rawY;
      if (id === 'storage') {{
        rawY = docTop(sec) - headerH - 4;
      }} else if (id === 'pricing-enterprise' || id === 'dedicated-line') {{
        rawY = docTop(sec) - headerH - 16;
      }} else {{
        var headEl = sec.querySelector('.section-head');
        rawY = headEl ? (docTop(headEl) - headerH - 28) : (docTop(sec) - headerH - 16);
      }}
      var maxScroll = Math.max(0, root.scrollHeight - root.clientHeight);
      var destY = Math.max(0, Math.min(rawY, maxScroll));
      window.scrollTo({{
        top: destY,
        behavior: smooth && !matchMedia('(prefers-reduced-motion: reduce)').matches ? 'smooth' : 'instant'
      }});
      return destY;
    }}

    document.querySelectorAll('a[href^="#"]').forEach(function (el) {{
      var href = el.getAttribute('href');
      if (!href || href === '#' || href === '#top') return;
      var id = href.slice(1);
      if (!document.getElementById(id)) return;
      el.addEventListener('click', function (e) {{
        e.preventDefault();
        history.replaceState(null, '', '#' + id);
        var destY = scrollToSection(id, true);
        var spyId = navById[id] ? id : ((id === 'pricing-enterprise' || id === 'dedicated-line') && navById.pricing ? 'pricing' : null);
        if (spyId && destY !== null) {{
          lockedNavId = spyId;
          lockTargetY = destY;
          lockExpire = Date.now() + 1800;
          applyNavIndicator(spyId, true);
        }}
      }});
    }});

    if (location.hash && location.hash.length > 1) {{
      var initId = decodeURIComponent(location.hash.slice(1));
      if (initId !== 'top' && document.getElementById(initId)) {{
        requestAnimationFrame(function () {{
          scrollToSection(initId, false);
          onScroll();
        }});
      }}
    }}

    if (matchMedia('(hover: hover)').matches) {{
      document.addEventListener('pointermove', function (e) {{
        var c = e.target.closest && e.target.closest('.card');
        if (!c) return;
        var r = c.getBoundingClientRect();
        c.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        c.style.setProperty('--my', (e.clientY - r.top) + 'px');
      }}, {{ passive: true }});
    }}

    document.addEventListener('click', function (e) {{
      if (!e.target.closest('[data-currency], [data-billing], [data-seat-tier]')) return;
      document.querySelectorAll('.price .amount, .addon-price .amount').forEach(function (el) {{
        el.classList.remove('pop'); void el.offsetWidth; el.classList.add('pop');
      }});
    }});

    if (!root.classList.contains('motion') || !('IntersectionObserver' in window)) return;
    var targets = document.querySelectorAll('main .section-head, main .card, main .faq details, main .cta, main .stripe-trust, main .currency-switch, main .pricing-controls, main .tier-divider, main .enterprise-toolbar, main .seat-addons');
    targets.forEach(function (el) {{
      var sibs = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
      el.classList.add('mo-reveal');
      el.style.transitionDelay = (Math.min(sibs, 5) * 70) + 'ms';
    }});
    var io = new IntersectionObserver(function (entries) {{
      entries.forEach(function (en) {{
        if (!en.isIntersecting) return;
        var el = en.target; io.unobserve(el);
        el.classList.add('mo-in');
        setTimeout(function () {{ el.classList.remove('mo-reveal', 'mo-in'); el.style.transitionDelay = ''; }}, 1300);
      }});
    }}, {{ threshold: 0.12, rootMargin: '0px 0px -6% 0px' }});
    targets.forEach(function (el) {{ io.observe(el); }});
  }})();
  </script>

  <script>
  (function () {{
    var card = document.getElementById('global-map');
    var canvas = document.getElementById('map-photon-canvas');
    if (!card || !canvas) return;
    var ctx = canvas.getContext('2d');
    var NODES = {json.dumps(js_nodes, ensure_ascii=False)};
    var ORDER = ["AU", "US", "SG", "MY", "ID", "JP", "KH", "NZ", "CA"];
    var ARCS = {json.dumps(shared["arcs"], ensure_ascii=False)};
    var W = 1120, H = 510;
    var activeId = 'AU';
    var userPinnedUntil = 0;
    var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

    function fitMapPills() {{
      card.querySelectorAll('.node-hit[data-anchor]').forEach(function (g) {{
        var nameEl = g.querySelector('.node-pill-name');
        var codeEl = g.querySelector('.node-pill-code');
        var rectEl = g.querySelector('.node-pill-bg');
        if (!nameEl || !codeEl || !rectEl || typeof nameEl.getComputedTextLength !== 'function') return;
        var tw = nameEl.getComputedTextLength();
        if (!tw || tw < 8) return;
        var w = Math.max(64, Math.ceil(30 + tw + 11));
        var ax = parseFloat(g.getAttribute('data-ax') || '0');
        var rx = g.getAttribute('data-anchor') === 'right' ? (ax - w) : ax;
        rectEl.setAttribute('x', rx.toFixed(1));
        rectEl.setAttribute('width', w.toFixed(1));
        codeEl.setAttribute('x', (rx + 8).toFixed(1));
        nameEl.setAttribute('x', (rx + 30).toFixed(1));
      }});
    }}
    fitMapPills();
    if (document.fonts && document.fonts.ready) {{
      document.fonts.ready.then(fitMapPills);
    }}

    var hudCode = document.getElementById('hud-code');
    var hudCountry = document.getElementById('hud-country');
    var hudRole = document.getElementById('hud-role');
    var hudCity = document.getElementById('hud-city');
    var hudRoute = document.getElementById('hud-route');

    var ripples = [];
    function spawnRipple(id, strong) {{
      var n = NODES[id];
      if (!n) return;
      ripples.push({{ x: n.x, y: n.y, r: 4, maxR: strong ? 34 : 22, a: strong ? 0.85 : 0.55 }});
    }}

    var packets = [];
    ARCS.forEach(function (arc, idx) {{
      var count = arc.pri ? 2 : 1;
      for (var k = 0; k < count; k++) {{
        packets.push({{
          idx: idx,
          t: (idx * 0.17 + k * 0.5) % 1,
          dir: k % 2 === 0 ? 1 : -1,
          speed: (arc.pri ? 0.0036 : 0.0026) + (idx % 3) * 0.0004,
          burst: false
        }});
      }}
    }});

    function setActive(id, fromUser) {{
      if (!NODES[id]) return;
      activeId = id;
      if (fromUser) userPinnedUntil = Date.now() + 9000;
      var info = NODES[id];
      if (hudCode) hudCode.textContent = id;
      if (hudCountry) hudCountry.textContent = info.name;
      if (hudRole) hudRole.textContent = info.role;
      if (hudCity) hudCity.textContent = info.city;
      if (hudRoute) hudRoute.textContent = info.route;

      card.querySelectorAll('.map-country').forEach(function (el) {{
        el.classList.toggle('active', el.getAttribute('data-country') === id);
      }});
      card.querySelectorAll('.node-hit').forEach(function (el) {{
        el.classList.toggle('active', el.getAttribute('data-node') === id);
      }});
      card.querySelectorAll('.map-pill').forEach(function (el) {{
        el.classList.toggle('active', el.getAttribute('data-pick-node') === id);
      }});
      card.querySelectorAll('.map-arc-core').forEach(function (el) {{
        var hot = el.getAttribute('data-from') === id || el.getAttribute('data-to') === id;
        el.classList.toggle('hot', hot);
      }});

      if (!reduced) {{
        spawnRipple(id, true);
        ARCS.forEach(function (arc, idx) {{
          if (arc.a === id || arc.b === id) {{
            packets.push({{
              idx: idx,
              t: arc.a === id ? 0.01 : 0.99,
              dir: arc.a === id ? 1 : -1,
              speed: 0.011,
              burst: true
            }});
          }}
        }});
      }}
    }}

    card.addEventListener('pointerover', function (e) {{
      var t = e.target.closest('[data-node], [data-country], [data-pick-node]');
      if (!t) return;
      var id = t.getAttribute('data-node') || t.getAttribute('data-country') || t.getAttribute('data-pick-node');
      if (id && id !== activeId) setActive(id, true);
    }});
    card.addEventListener('click', function (e) {{
      var t = e.target.closest('[data-node], [data-country], [data-pick-node]');
      if (!t) return;
      var id = t.getAttribute('data-node') || t.getAttribute('data-country') || t.getAttribute('data-pick-node');
      if (id) setActive(id, true);
    }});
    card.addEventListener('keydown', function (e) {{
      if (e.key !== 'Enter' && e.key !== ' ') return;
      var t = e.target.closest('[data-node]');
      if (!t) return;
      e.preventDefault();
      setActive(t.getAttribute('data-node'), true);
    }});

    if (!reduced) {{
      setInterval(function () {{
        if (Date.now() < userPinnedUntil || document.hidden) return;
        var next = ORDER[(ORDER.indexOf(activeId) + 1) % ORDER.length];
        setActive(next, false);
      }}, 3600);
    }}

    function qPt(arc, t) {{
      var u = 1 - t;
      return {{
        x: u * u * arc.x1 + 2 * u * t * arc.cx + t * t * arc.x2,
        y: u * u * arc.y1 + 2 * u * t * arc.cy + t * t * arc.y2
      }};
    }}

    function resizeCanvas() {{
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var rect = canvas.getBoundingClientRect();
      var cw = Math.max(1, Math.round(rect.width * dpr));
      var ch = Math.max(1, Math.round(rect.height * dpr));
      if (canvas.width !== cw || canvas.height !== ch) {{
        canvas.width = cw;
        canvas.height = ch;
      }}
      ctx.setTransform(cw / W, 0, 0, ch / H, 0, 0);
    }}
    resizeCanvas();
    addEventListener('resize', resizeCanvas, {{ passive: true }});

    var visible = true;
    if ('IntersectionObserver' in window) {{
      new IntersectionObserver(function (es) {{
        visible = es[0].isIntersecting;
      }}, {{ threshold: 0.05 }}).observe(card);
    }}

    function frame() {{
      if (visible && !document.hidden) {{
        resizeCanvas();
        ctx.clearRect(0, 0, W, H);

        for (var r = ripples.length - 1; r >= 0; r--) {{
          var rp = ripples[r];
          rp.r += 0.65;
          rp.a *= 0.955;
          if (rp.r >= rp.maxR || rp.a < 0.03) {{
            ripples.splice(r, 1);
            continue;
          }}
          ctx.beginPath();
          ctx.arc(rp.x, rp.y, rp.r, 0, Math.PI * 2);
          ctx.strokeStyle = 'rgba(255, 216, 181, ' + rp.a.toFixed(3) + ')';
          ctx.lineWidth = 1.4;
          ctx.stroke();
        }}

        for (var i = packets.length - 1; i >= 0; i--) {{
          var pk = packets[i];
          var arc = ARCS[pk.idx];
          var isHot = arc.a === activeId || arc.b === activeId || pk.burst;
          pk.t += pk.dir * pk.speed * (isHot && !pk.burst ? 1.35 : 1);

          if (pk.t >= 1 || pk.t <= 0) {{
            var dest = pk.t >= 1 ? arc.b : arc.a;
            if (isHot) spawnRipple(dest, false);
            if (pk.burst) {{
              packets.splice(i, 1);
              continue;
            }}
            pk.t = pk.t >= 1 ? 0 : 1;
          }}

          var tailLen = pk.burst ? 0.14 : (isHot ? 0.11 : 0.075);
          var steps = 10;
          for (var s = steps; s >= 1; s--) {{
            var t0 = Math.max(0, Math.min(1, pk.t - pk.dir * tailLen * (s / steps)));
            var t1 = Math.max(0, Math.min(1, pk.t - pk.dir * tailLen * ((s - 1) / steps)));
            var p0 = qPt(arc, t0), p1 = qPt(arc, t1);
            var frac = 1 - s / (steps + 1);
            ctx.beginPath();
            ctx.moveTo(p0.x, p0.y);
            ctx.lineTo(p1.x, p1.y);
            ctx.strokeStyle = isHot
              ? 'rgba(255, 226, 196, ' + (frac * 0.88).toFixed(3) + ')'
              : 'rgba(232, 144, 111, ' + (frac * 0.48).toFixed(3) + ')';
            ctx.lineWidth = (isHot ? 2.8 : 1.7) * frac + 0.5;
            ctx.lineCap = 'round';
            ctx.stroke();
          }}
          var head = qPt(arc, pk.t);
          ctx.beginPath();
          ctx.arc(head.x, head.y, isHot ? 2.7 : 1.8, 0, Math.PI * 2);
          ctx.fillStyle = isHot ? '#ffffff' : '#ffd8b5';
          ctx.fill();
        }}
      }}
      if (!reduced) requestAnimationFrame(frame);
    }}
    if (!reduced) requestAnimationFrame(frame);
  }})();
  </script>
</body>

</html>
"""


def render_legal(loc: dict, d: dict, doc_key: str) -> str:
    page_name = f"{doc_key}.html"
    asset_prefix = "" if loc["is_root"] else "../"
    html_dir = f' dir="{loc["dir"]}"' if loc["dir"] == "rtl" else ""
    doc = d[doc_key]
    hreflang_block = build_hreflang_tags(loc, page_name)
    gfont_block = build_google_font_links(loc)
    autoredir_block = build_root_autoredirect_script(page_name) if loc["is_root"] else ""
    switcher_html = build_lang_switcher_html(loc, d["nav"]["lang_aria"], page_name)
    switcher_js = build_lang_switcher_js(loc["slug"])

    cur_terms = ' aria-current="page"' if doc_key == "terms" else ""
    cur_refund = ' aria-current="page"' if doc_key == "refund" else ""
    cur_privacy = ' aria-current="page"' if doc_key == "privacy" else ""

    sections_html = "\n\n".join(
        f'<h2>{esc(sec["h2"])}</h2>\n{sec["body_html"]}'
        for sec in doc["sections"]
    )

    return f"""<!doctype html>
<html lang="{loc["html_lang"]}"{html_dir}>

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(doc["title"])}</title>
  <meta name="description" content="{esc(doc["description"])}">
{hreflang_block}
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{loc["og_locale"]}">
  <meta property="og:site_name" content="Zaokit ClaudeOps">
  <meta property="og:title" content="{esc(doc["title"])}">
  <meta property="og:description" content="{esc(doc["description"])}">
  <meta property="og:url" content="{page_abs_url(loc, page_name)}">
  <link rel="icon" href="{asset_prefix}favicon.svg" type="image/svg+xml">
  <meta name="theme-color" content="#141210">
{gfont_block}{autoredir_block}  <style>
    :root {{ --bg:#141210; --text:#ece6dd; --muted:#a39a8e; --primary:#d97757; --primary-strong:#e8906f; --primary-soft:rgba(217,119,87,.14);
      --cream:#f5efe6; --border:rgba(255,255,255,.08); --surface:rgba(255,255,255,.035);
      --font:"Inter",{loc["font_extra"]},sans-serif;
      --serif:"Tiempos Headline",{loc["serif_extra"]},Georgia,serif; }}
    * {{ box-sizing:border-box }}
    body {{ margin:0; background:var(--bg); color:var(--text); font-family:var(--font); line-height:1.8; -webkit-font-smoothing:antialiased }}
    a {{ color:var(--primary-strong); text-decoration:none }} a:hover {{ text-decoration:underline }}
    .container {{ width:min(820px,92vw); margin:0 auto }}
    .site-header {{ position:sticky; top:0; z-index:30; backdrop-filter:blur(16px); background:rgba(20,18,16,.88); border-bottom:1px solid var(--border) }}
    .nav {{ display:flex; align-items:center; justify-content:space-between; gap:16px; min-height:64px; flex-wrap:wrap; padding:8px 0 }}
    .brand {{ color:#fff; font-weight:700 }}
    .nav-links {{ display:flex; align-items:center; gap:16px; flex-wrap:wrap; font-size:.88rem }}
    .nav-links a {{ color:var(--muted) }} .nav-links a[aria-current="page"] {{ color:var(--primary-strong); font-weight:600 }}
    .doc {{ padding:56px 0 40px }}
    .doc h1 {{ font-family:var(--serif); color:var(--cream); font-size:clamp(1.8rem,4vw,2.4rem); margin:0 0 8px }}
    .meta {{ color:var(--muted); font-size:.88rem; margin:0 0 28px }}
    .lead {{ background:var(--surface); border:1px solid var(--border); border-left:3px solid var(--primary); border-radius:12px; padding:16px 20px; color:var(--text); font-size:.94rem }}
    .doc h2 {{ color:#fff; font-size:1.12rem; margin:36px 0 10px; padding-top:20px; border-top:1px solid var(--border) }}
    .doc p, .doc li {{ font-size:.95rem; color:var(--text) }}
    .doc ul, .doc ol {{ padding-left:1.3em }} .doc li {{ margin:6px 0 }}
    .doc strong {{ color:var(--cream) }}
    footer {{ border-top:1px solid var(--border); padding:28px 0 40px; color:var(--muted); font-size:.82rem }}
    footer .links {{ display:flex; gap:16px; flex-wrap:wrap; margin-bottom:8px }}
    footer .links a {{ color:var(--muted) }}
    [dir="rtl"] .lead {{ border-left:1px solid var(--border); border-right:3px solid var(--primary) }}
    [dir="rtl"] .doc ul, [dir="rtl"] .doc ol {{ padding-left:0; padding-right:1.3em }}
{LANG_SWITCHER_CSS}
  </style>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-0GDE6TX65P"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-0GDE6TX65P');
  </script>
  <script defer src="https://cloud.umami.is/script.js" data-website-id="0731cafa-79de-46ca-bbeb-4e1bf6a04fda"></script>
</head>

<body>
  <header class="site-header">
    <div class="container nav">
      <a class="brand" href="./">Zaokit ClaudeOps</a>
      <nav class="nav-links"><a href="terms.html"{cur_terms}>{esc(d["footer"]["terms"])}</a><a href="refund.html"{cur_refund}>{esc(d["footer"]["refund"])}</a><a href="privacy.html"{cur_privacy}>{esc(d["footer"]["privacy"])}</a>{switcher_html}</nav>
    </div>
  </header>

  <main class="container doc">
    <h1>{esc(doc["h1"])}</h1>
    <p class="meta">{esc(doc["meta"])}</p>

<p class="lead">{doc["lead_html"]}</p>

{sections_html}

  </main>

  <footer>
    <div class="container">
      <div class="links"><a href="./">{esc(d["legal_common"]["back_home"])}</a><a href="terms.html"{cur_terms}>{esc(d["footer"]["terms"])}</a><a href="refund.html"{cur_refund}>{esc(d["footer"]["refund"])}</a><a href="privacy.html"{cur_privacy}>{esc(d["footer"]["privacy"])}</a></div>
      <div>{esc(d["legal_common"]["footer_copy"])}</div>
    </div>
  </footer>
{switcher_js}
</body>

</html>
"""


def extract_base_css() -> str:
    # Cache clean base CSS into _i18n/base.css on first run so rebuilds stay idempotent
    css_cache = os.path.join(I18N_DIR, "base.css")
    if os.path.exists(css_cache):
        with open(css_cache, "r", encoding="utf-8") as f:
            return f.read()
    with open(os.path.join(ROOT, "en/index.html"), "r", encoding="utf-8") as f:
        en_html = f.read()
    s = en_html.index("<style>") + len("<style>\n")
    e = en_html.index("</style>")
    css = en_html[s:e].rstrip()
    with open(css_cache, "w", encoding="utf-8") as f:
        f.write(css)
    return css


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", help="Comma-separated locale slugs to build (default: all 19)")
    args = parser.parse_args()

    with open(os.path.join(I18N_DIR, "shared.json"), "r", encoding="utf-8") as f:
        shared = json.load(f)
    base_css = extract_base_css()

    target_slugs = [s.strip() for s in args.only.split(",")] if args.only else [l["slug"] for l in LOCALES]
    built_files = 0

    for slug in target_slugs:
        if slug not in LOCALE_BY_SLUG:
            print(f"ERROR: Unknown locale slug {slug}", file=sys.stderr)
            sys.exit(1)
        loc = LOCALE_BY_SLUG[slug]
        json_path = os.path.join(LOCALES_DIR, f"{slug}.json")
        if not os.path.exists(json_path):
            print(f"ERROR: Missing locale dictionary {json_path}", file=sys.stderr)
            sys.exit(1)
        with open(json_path, "r", encoding="utf-8") as f:
            d = json.load(f)

        out_dir = ROOT if loc["is_root"] else os.path.join(ROOT, slug)
        os.makedirs(out_dir, exist_ok=True)

        idx_html = render_index(loc, d, shared, base_css)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(idx_html)
        built_files += 1

        for doc_key in ("privacy", "terms", "refund"):
            l_html = render_legal(loc, d, doc_key)
            with open(os.path.join(out_dir, f"{doc_key}.html"), "w", encoding="utf-8") as f:
                f.write(l_html)
            built_files += 1

    print(f"Built {built_files} HTML files across {len(target_slugs)} locale(s): {', '.join(target_slugs)}")


if __name__ == "__main__":
    main()

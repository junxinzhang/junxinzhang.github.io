#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Comprehensive validator for Zaokit ClaudeOps i18n JSON dictionaries & generated static HTML files.
"""
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser

ROOT = "/Users/jason/workspace/junxinzhang.github.io/projects/claude-ops"
I18N_DIR = os.path.join(ROOT, "_i18n")
LOCALES_DIR = os.path.join(I18N_DIR, "locales")

sys.path.insert(0, I18N_DIR)
import build as build_mod  # noqa: E402

FORBIDDEN_RE = re.compile(r"(微信|wechat)", re.IGNORECASE)
PLACEHOLDER_RE = re.compile(r"\{(\w+)\}")
UNREPLACED_VISIBLE_RE = re.compile(r"\{(sym|eq|save|day|ratio|mult|label|email)\}")


class BalanceChecker(HTMLParser):
    VOID_TAGS = {"br", "hr", "img", "input", "meta", "link"}

    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        if tag not in self.VOID_TAGS:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.VOID_TAGS:
            return
        if not self.stack or self.stack[-1] != tag:
            self.errors.append(f"Mismatched closing </{tag}> (stack={self.stack})")
        else:
            self.stack.pop()

    def close(self):
        super().close()
        if self.stack:
            self.errors.append(f"Unclosed tags: {self.stack}")


def check_html_fragment(frag: str, path: str, errs: list):
    p = BalanceChecker()
    p.feed(frag)
    p.close()
    for e in p.errors:
        errs.append(f"{path}: {e}")


def compare_schema(ref, cur, path: str, slug: str, errs: list):
    if type(ref) is not type(cur):
        errs.append(f"[{slug}] {path}: expected {type(ref).__name__}, got {type(cur).__name__}")
        return
    if isinstance(ref, dict):
        ref_keys = set(ref.keys())
        cur_keys = set(cur.keys())
        # network.rows[2].before is None in ref; allow None vs None
        missing = ref_keys - cur_keys
        extra = cur_keys - ref_keys
        if missing:
            errs.append(f"[{slug}] {path}: missing keys {sorted(missing)}")
        if extra:
            errs.append(f"[{slug}] {path}: unexpected keys {sorted(extra)}")
        for k in sorted(ref_keys & cur_keys):
            sub_path = f"{path}.{k}" if path else k
            if ref[k] is None and cur[k] is None:
                continue
            compare_schema(ref[k], cur[k], sub_path, slug, errs)
    elif isinstance(ref, list):
        if len(ref) != len(cur):
            errs.append(f"[{slug}] {path}: expected list len {len(ref)}, got {len(cur)}")
            return
        for idx, (r_item, c_item) in enumerate(zip(ref, cur)):
            compare_schema(r_item, c_item, f"{path}[{idx}]", slug, errs)
    elif isinstance(ref, str):
        if not cur.strip() and ref.strip():
            errs.append(f"[{slug}] {path}: empty string")
        m_forb = FORBIDDEN_RE.search(cur)
        if m_forb:
            errs.append(f"[{slug}] {path}: contains forbidden term '{m_forb.group(0)}'")
        if path.startswith("js."):
            ref_ph = set(PLACEHOLDER_RE.findall(ref))
            cur_ph = set(PLACEHOLDER_RE.findall(cur))
            if ref_ph != cur_ph:
                errs.append(f"[{slug}] {path}: placeholder mismatch: expected {sorted(ref_ph)}, got {sorted(cur_ph)}")
        if path.endswith("_html") or path.endswith("SeatLi") or path.endswith(".features_html[0]") or ".features_html[" in path:
            check_html_fragment(cur, f"[{slug}] {path}", errs)


def extract_head_payment_baseline():
    repo = "/Users/jason/workspace/junxinzhang.github.io"
    head_html = subprocess.check_output(
        ["git", "-C", repo, "show", "HEAD:projects/claude-ops/index.html"]
    ).decode("utf-8")
    m_sl = re.search(r"var STRIPE_LINKS = (\{.*?\});", head_html, re.DOTALL)
    m_pr = re.search(r"var PRICES = (\{.*?\});\s*var STRIPE_LINKS", head_html, re.DOTALL)
    assert m_sl and m_pr, "Could not extract STRIPE_LINKS / PRICES from HEAD"
    js_eval = (
        f"const PRICES = {m_pr.group(1)};\n"
        f"const STRIPE_LINKS = {m_sl.group(1)};\n"
        "console.log(JSON.stringify({PRICES, STRIPE_LINKS}));"
    )
    out = subprocess.check_output(["node", "-e", js_eval]).decode("utf-8")
    return json.loads(out)


def verify_html_files(slugs: list, errs: list):
    all_js_snippets = []
    baseline = extract_head_payment_baseline()
    head_links = baseline["STRIPE_LINKS"]
    head_prices = baseline["PRICES"]

    for slug in slugs:
        loc = build_mod.LOCALE_BY_SLUG[slug]
        base_dir = ROOT if loc["is_root"] else os.path.join(ROOT, slug)
        for page_name in ("index.html", "privacy.html", "terms.html", "refund.html"):
            fpath = os.path.join(base_dir, page_name)
            rel_label = os.path.relpath(fpath, ROOT)
            if not os.path.exists(fpath) or os.path.getsize(fpath) == 0:
                errs.append(f"[HTML] Missing or empty file: {rel_label}")
                continue
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            # 0. Production CSP compliance (style-src 'self' 'unsafe-inline'; script-src 'self' 'unsafe-inline' googletagmanager umami)
            ext_styles = re.findall(r'<link[^>]+rel="stylesheet"[^>]+href="(https?:[^"]+)"', content)
            if ext_styles:
                errs.append(f"[CSP] {rel_label}: external stylesheet violates CSP: {ext_styles}")
            ext_scripts = re.findall(r'<script[^>]+src="(https?:[^"]+)"', content)
            for sc_url in ext_scripts:
                if not (sc_url.startswith("https://www.googletagmanager.com/") or sc_url.startswith("https://cloud.umami.is/")):
                    errs.append(f"[CSP] {rel_label}: unauthorized external script src: {sc_url}")

            # 1. html lang & dir
            expected_html_open = (
                f'<html lang="{loc["html_lang"]}" dir="rtl">'
                if loc["dir"] == "rtl"
                else f'<html lang="{loc["html_lang"]}">'
            )
            if expected_html_open not in content:
                errs.append(f"[HTML] {rel_label}: missing {expected_html_open}")

            # 2. canonical + 20 hreflangs
            exp_canon = f'<link rel="canonical" href="{build_mod.page_abs_url(loc, page_name)}">'
            if exp_canon not in content:
                errs.append(f"[HTML] {rel_label}: missing canonical {exp_canon}")
            hreflangs = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)">', content)
            if len(hreflangs) != 20:
                errs.append(f"[HTML] {rel_label}: expected 20 hreflang tags, got {len(hreflangs)}")

            # 3. lang-switcher items & relative href resolution
            items = re.findall(r'<a class="lang-item([^"]*)"[^>]*href="([^"]+)"[^>]*data-set-lang="([^"]+)"', content)
            if len(items) != 19:
                errs.append(f"[HTML] {rel_label}: expected 19 .lang-item links, got {len(items)}")
            active_slugs = [s for cls_sfx, _, s in items if "active" in cls_sfx]
            if active_slugs != [slug]:
                errs.append(f"[HTML] {rel_label}: expected active lang [{slug}], got {active_slugs}")
            for _, href, target_slug in items:
                resolved = os.path.normpath(os.path.join(base_dir, href))
                if href.endswith("/") or href == "./" or href == "../":
                    target_index = os.path.join(resolved, "index.html")
                    # Only check existence if target_slug is in slugs being verified
                    if target_slug in slugs and not os.path.exists(target_index):
                        errs.append(f"[HTML] {rel_label}: broken switcher dir link {href} -> {target_index}")
                else:
                    if target_slug in slugs and not os.path.exists(resolved):
                        errs.append(f"[HTML] {rel_label}: broken switcher file link {href} -> {resolved}")

            # 4. JSON-LD on index.html
            if page_name == "index.html":
                m_ld = re.search(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', content, re.DOTALL)
                if not m_ld:
                    errs.append(f"[HTML] {rel_label}: missing JSON-LD script")
                else:
                    try:
                        ld = json.loads(m_ld.group(1))
                        if ld.get("inLanguage") != loc["html_lang"]:
                            errs.append(f"[HTML] {rel_label}: JSON-LD inLanguage mismatch")
                    except Exception as ex:
                        errs.append(f"[HTML] {rel_label}: invalid JSON-LD: {ex}")

                # Check static assets exist
                for asset_m in re.findall(r'(?:href|src)="((?:\.\./)?(?:favicon[^"#?]+|apple-touch-icon\.png|telegram-qr\.jpg))"', content):
                    res_asset = os.path.normpath(os.path.join(base_dir, asset_m))
                    if not os.path.exists(res_asset):
                        errs.append(f"[HTML] {rel_label}: missing asset {asset_m} -> {res_asset}")

                # 4b. Payment & Stripe Checkout 100% Parity Check against HEAD
                m_sl = re.search(r"var STRIPE_LINKS = (\{.*?\});", content)
                m_pr = re.search(r"var PRICES = (\{.*?\});", content)
                if not m_sl or not m_pr:
                    errs.append(f"[PAY] {rel_label}: missing PRICES or STRIPE_LINKS in JS")
                else:
                    cur_links = json.loads(m_sl.group(1))
                    cur_prices = json.loads(m_pr.group(1))
                    if cur_links != head_links:
                        errs.append(f"[PAY] {rel_label}: STRIPE_LINKS differs from HEAD! (len {len(cur_links)} vs {len(head_links)})")
                    for ccode, h_entry in head_prices.items():
                        c_entry = cur_prices.get(ccode, {})
                        for nk in ("sym", "p", "orig20x", "line", "team", "biz", "upg", "s"):
                            if c_entry.get(nk) != h_entry.get(nk):
                                errs.append(f"[PAY] {rel_label}: PRICES[{ccode}][{nk}] mismatch ({c_entry.get(nk)} != {h_entry.get(nk)})")
                    def_cur = loc["default_currency"]
                    expected_btn_links = [
                        ("data-stripe-tier", "1x", head_links[f"1x_{def_cur}"]),
                        ("data-stripe-tier", "5x", head_links[f"5x_{def_cur}"]),
                        ("data-stripe-tier", "20x", head_links[f"20x_{def_cur}"]),
                        ("data-line-tier", "line_1x", head_links[f"line_1x_{def_cur}"]),
                        ("data-line-tier", "line_5x", head_links[f"line_5x_{def_cur}"]),
                        ("data-ent-btn", "team", f"/api/airwallex/checkout?plan=team_max_{def_cur}&amp;locale={slug}"),
                        ("data-ent-btn", "biz", f"/api/airwallex/checkout?plan=biz_max_{def_cur}&amp;locale={slug}"),
                        ("data-upg-tier", "upg_pm", f"/api/airwallex/checkout?plan=upg_pm_{def_cur}&amp;locale={slug}"),
                        ("data-stripe-tier", "2t", head_links[f"2t_{def_cur}"]),
                        ("data-stripe-tier", "6t", head_links[f"6t_{def_cur}"]),
                        ("data-stripe-tier", "12t", head_links[f"12t_{def_cur}"]),
                        ("data-stripe-tier", "30t", head_links[f"30t_{def_cur}"]),
                    ]
                    for attr_name, attr_val, exp_url in expected_btn_links:
                        pat = rf'{attr_name}="{re.escape(attr_val)}"\s+href="([^"]+)"'
                        m_btn = re.search(pat, content)
                        if not m_btn or m_btn.group(1) != exp_url:
                            errs.append(f"[PAY] {rel_label}: button {attr_name}={attr_val} href={m_btn.group(1) if m_btn else None} != {exp_url}")

            # 5. Inline JS extraction & unreplaced placeholder check
            no_scripts = re.sub(r"<script\b[^>]*>.*?</script>", "", content, flags=re.DOTALL)
            no_styles = re.sub(r"<style\b[^>]*>.*?</style>", "", no_scripts, flags=re.DOTALL)
            m_unrep = UNREPLACED_VISIBLE_RE.search(no_styles)
            if m_unrep:
                errs.append(f"[HTML] {rel_label}: unreplaced placeholder {m_unrep.group(0)} in visible HTML")

            for m_sc in re.finditer(r"<script([^>]*)>(.*?)</script>", content, flags=re.DOTALL):
                attrs, body = m_sc.group(1), m_sc.group(2)
                if "application/ld+json" in attrs or "src=" in attrs:
                    continue
                if body.strip():
                    all_js_snippets.append((rel_label, body))

    # Batch-check all inline JS blocks using node --check in one combined syntax check per locale or file
    if all_js_snippets:
        combined_lines = []
        for label, code in all_js_snippets:
            combined_lines.append(f"// === {label} ===\n(function(){{\n{code}\n}})();\n")
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8", delete=False) as tf:
            tf.write("\n".join(combined_lines))
            tmp_js = tf.name
        try:
            proc = subprocess.run(["node", "--check", tmp_js], capture_output=True, text=True)
            if proc.returncode != 0:
                errs.append(f"[JS] node --check failed:\n{proc.stderr[:1200]}")
        finally:
            if os.path.exists(tmp_js):
                os.remove(tmp_js)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--available", action="store_true", help="Validate only currently present locale JSON files")
    parser.add_argument("--check-html", action="store_true", help="Also verify generated HTML files for target locales")
    args = parser.parse_args()

    with open(os.path.join(LOCALES_DIR, "en.json"), "r", encoding="utf-8") as f:
        en_ref = json.load(f)

    all_slugs = [l["slug"] for l in build_mod.LOCALES]
    if args.available:
        slugs = [s for s in all_slugs if os.path.exists(os.path.join(LOCALES_DIR, f"{s}.json"))]
    else:
        slugs = all_slugs

    errs = []
    for slug in slugs:
        jpath = os.path.join(LOCALES_DIR, f"{slug}.json")
        if not os.path.exists(jpath):
            errs.append(f"Missing locale JSON: {slug}.json")
            continue
        try:
            with open(jpath, "r", encoding="utf-8") as f:
                cur = json.load(f)
        except Exception as ex:
            errs.append(f"[{slug}] JSON parse error: {ex}")
            continue
        compare_schema(en_ref, cur, "", slug, errs)
        au_pill = cur.get("map", {}).get("nodes", {}).get("AU", {}).get("pill", "")
        if "★" not in au_pill:
            errs.append(f"[{slug}] map.nodes.AU.pill missing '★': {au_pill!r}")

    if args.check_html:
        verify_html_files(slugs, errs)

    if errs:
        print(f"VALIDATION FAILED ({len(errs)} error(s)) across {len(slugs)} locale(s):")
        for e in errs[:60]:
            print("  -", e)
        sys.exit(1)
    else:
        print(f"VALIDATION PASSED: {len(slugs)} locale(s) ({', '.join(slugs)}) — 0 errors!")


if __name__ == "__main__":
    main()

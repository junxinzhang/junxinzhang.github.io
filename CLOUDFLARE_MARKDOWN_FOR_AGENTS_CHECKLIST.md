# Cloudflare Markdown for Agents Checklist

Last updated: 2026-02-14

This checklist is for enabling and validating Cloudflare "Markdown for Agents" on `junxinzhang.com`.

## 1) Pre-checks

- Domain DNS is proxied by Cloudflare (orange cloud enabled).
- Zone is active in Cloudflare dashboard.
- Plan eligibility is met (Cloudflare announced Beta availability for Pro/Business/Enterprise, including SSL for SaaS).
- Existing origin keeps serving normal HTML correctly.

## 2) Enable in Cloudflare Dashboard

- Open Cloudflare Dashboard.
- Select zone: `junxinzhang.com`.
- Navigate to the Markdown for Agents feature (search "Markdown for Agents" in dashboard search if the path is not obvious).
- Enable the feature for the zone.
- Save and publish.

## 3) Verify with cURL

```bash
# 1) Baseline response should be HTML
curl -sSI https://junxinzhang.com/ | sed -n '1,40p'

# 2) Request markdown with Accept negotiation
curl -sSI https://junxinzhang.com/ -H 'Accept: text/markdown' | sed -n '1,60p'

# 3) Inspect body (should look like markdown instead of full HTML)
curl -s https://junxinzhang.com/ -H 'Accept: text/markdown' | head -n 80
```

Expected:
- Step 1 returns `content-type: text/html` (or similar HTML type).
- Step 2 should return markdown-oriented content type (feature-dependent header format may vary by beta version).
- Step 3 body should be markdown content, not raw HTML markup.

## 4) Test one article URL

```bash
curl -sSI "https://junxinzhang.com/ai-agent-skill-mcp-beginner-guide/" -H 'Accept: text/markdown' | sed -n '1,60p'
curl -s "https://junxinzhang.com/ai-agent-skill-mcp-beginner-guide/" -H 'Accept: text/markdown' | head -n 80
```

## 5) Cache and edge checks

- Purge Cloudflare cache (single URL and then full purge if needed).
- Re-test from two different networks/regions if possible.
- Confirm no unexpected impact to normal browser requests.

## 6) Rollback (if needed)

- Disable the Markdown for Agents feature in dashboard.
- Purge cache.
- Re-run baseline `curl -I` checks to confirm HTML-only behavior is restored.

## 7) Keep fallback endpoints

Even with Cloudflare markdown enabled, keep these stable endpoints:
- `https://junxinzhang.com/llms.txt`
- `https://junxinzhang.com/llms-full.txt`
- `https://junxinzhang.com/sitemap.xml`
- `https://junxinzhang.com/feed.xml`

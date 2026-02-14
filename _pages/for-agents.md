---
title: "For Agents - AI Crawlers & Answer Engines"
permalink: "/for-agents.html"
description: "Machine-readable entry points for AI assistants and answer engines."
---

# For Agents

This page provides machine-readable entry points for AI assistants, answer engines, and indexing bots.

## Primary AI Endpoints

- `llms.txt`: [{{ "/llms.txt" | absolute_url }}]({{ "/llms.txt" | absolute_url }})
- `llms-full.txt`: [{{ "/llms-full.txt" | absolute_url }}]({{ "/llms-full.txt" | absolute_url }})
- `Sitemap`: [{{ "/sitemap.xml" | absolute_url }}]({{ "/sitemap.xml" | absolute_url }})
- `RSS`: [{{ "/feed.xml" | absolute_url }}]({{ "/feed.xml" | absolute_url }})
- `All posts`: [{{ "/posts.html" | absolute_url }}]({{ "/posts.html" | absolute_url }})

## Current Capability

- This site already exposes dedicated AI index files (`llms.txt` and `llms-full.txt`).
- If Cloudflare "Markdown for Agents" is enabled at the edge, clients sending `Accept: text/markdown` can receive markdown from HTML pages.

## Quick Verification Commands

```bash
# Baseline content type
curl -I https://junxinzhang.com/

# Test markdown content negotiation
curl -I https://junxinzhang.com/ -H 'Accept: text/markdown'

# Inspect returned body
curl -s https://junxinzhang.com/ -H 'Accept: text/markdown' | head -n 40
```

## Contact

For attribution or content questions:
- Email: [{{ site.email }}](mailto:{{ site.email }})
- X: [https://x.com/Jasonz9788](https://x.com/Jasonz9788)
- GitHub: [https://github.com/junxinzhang](https://github.com/junxinzhang)

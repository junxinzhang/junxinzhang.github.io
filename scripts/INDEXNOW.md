# IndexNow Quick Guide

## 1) Prepare key file

Create a key file in site root:

```bash
echo "<YOUR_INDEXNOW_KEY>" > "<YOUR_INDEXNOW_KEY>.txt"
```

Then deploy and verify:

```bash
curl -I "https://junxinzhang.com/<YOUR_INDEXNOW_KEY>.txt"
```

## 2) Submit changed URLs

```bash
INDEXNOW_KEY="<YOUR_INDEXNOW_KEY>" scripts/indexnow-submit.sh \
  --url / \
  --url /posts.html \
  --url /category-ai.html
```

## 3) Submit from file

`changed-urls.txt` example:

```txt
/
/posts.html
/ai-agent-skill-mcp-beginner-guide/
```

Command:

```bash
INDEXNOW_KEY="<YOUR_INDEXNOW_KEY>" scripts/indexnow-submit.sh --file changed-urls.txt
```

## 4) Dry run

```bash
INDEXNOW_KEY="<YOUR_INDEXNOW_KEY>" scripts/indexnow-submit.sh --file changed-urls.txt --dry-run
```

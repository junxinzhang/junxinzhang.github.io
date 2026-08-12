# AGENTS.md

## Cursor Cloud specific instructions

This repo is a **Jekyll 4.3 static blog** ("Just Jason"). Ruby 3.2 and Bundler are
already installed in the VM image, and gems are installed into the repo-local
`vendor/bundle` (configured via `.bundle/config`, `path = vendor/bundle`). The
startup update script runs `bundle install`, so on a fresh session dependencies are
ready without extra steps.

### Running / building

- Dev server: `bundle exec jekyll serve --host 0.0.0.0 --port 4000` (serves at
  `http://localhost:4000/`, auto-regenerates on file changes).
- One-off build: `bundle exec jekyll build` (output goes to `_site/`).
- Production build (mirrors CI in `.github/workflows/jekyll.yml`):
  `JEKYLL_ENV=production bundle exec jekyll build`.

### Non-obvious notes

- There is no separate lint/test suite. `bundle exec jekyll build` is the effective
  "does it compile" check — a clean build with no Liquid/YAML errors is the signal
  that changes are valid.
- `Gemfile.lock` and `.bundle/` are git-ignored, so bundler config and resolved
  versions live only in the VM (they persist in the snapshot, not in git).
- CI uses Ruby 3.1 via `ruby/setup-ruby`, but the VM uses the Ubuntu-packaged
  Ruby 3.2; Jekyll 4.3 builds identically on both.
- The `docker-compose.yml` (`jekyll/jekyll:latest`) is an alternative way to serve
  locally; the native `bundle exec jekyll serve` flow above is preferred in the VM.
- The `scripts/` directory contains auxiliary Python/Node/shell tooling for images
  and publishing; it is excluded from the Jekyll build and not needed to run the site.

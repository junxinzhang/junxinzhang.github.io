source "https://rubygems.org"

# Jekyll version - locked for stability
gem "jekyll", "~> 4.3"

# Windows specific
gem 'wdm', '>= 0.1.0' if Gem.win_platform?

# Jekyll Plugins
group :jekyll_plugins do
    gem 'jekyll-feed'
    gem 'jekyll-sitemap'
    gem 'jekyll-paginate'
    gem 'jekyll-seo-tag'
    gem 'jekyll-gist'
    # Keep CI on the known-good Sass line used by this site.
    gem 'jekyll-sass-converter', '~> 3.0.0'
    gem 'sass-embedded', '~> 1.58.3'
end

# Development dependencies
group :development do
    gem 'webrick'  # Required for Ruby 3.0+
end

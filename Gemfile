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
    # Pin to 3.0.x: 3.1.0 pulls sass-embedded 1.100.0 which uses JSON::Fragment
    # (json >= 2.9.0 only), incompatible with Ruby 3.1.x bundled json 2.6.x
    gem 'jekyll-sass-converter', '~> 3.0.0'
end

# Development dependencies
group :development do
    gem 'webrick'  # Required for Ruby 3.0+
end
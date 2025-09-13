# cruftex.net - Hugo Site

This is the Hugo version of the cruftex.net blog, migrated from Hexo.

## Migration Summary

- **Original**: Hexo static site generator
- **New**: Hugo static site generator
- **Theme**: Terminal theme by panr
- **Content**: 10 blog posts + About page
- **Assets**: All images and static files migrated

## Structure

```
cruftex-hugo/
├── content/
│   ├── posts/          # Blog posts (migrated from Hexo)
│   └── about.md        # About page
├── static/
│   └── image/          # Static images
├── themes/
│   └── terminal/       # Terminal theme (git submodule)
├── hugo.toml           # Hugo configuration
└── build.sh           # Build script
```

## Development

### Prerequisites
- Hugo v0.119.0 or later
- Git (for theme submodule)

### Local Development
```bash
# Serve locally
hugo server --bind 0.0.0.0 --port 12000

# Build for production
./build.sh
# or
hugo --minify
```

### Configuration
Main configuration is in `hugo.toml`:
- Site metadata (title, description, author)
- Permalinks matching original Hexo structure
- Menu configuration
- Theme settings

## Migration Notes

- All 10 posts successfully migrated with proper front matter
- Dates preserved in ISO format
- Tags converted from Hexo format to Hugo format
- Static images and assets copied to Hugo structure
- Permalinks configured to match original URLs: `/:year/:month/:day/:title.html`
- About page migrated and accessible via menu

## Theme

Using the Terminal theme which provides:
- Clean, minimalist design
- Responsive layout
- Syntax highlighting
- Tag support
- Navigation menu

## Deployment

The site can be deployed to any static hosting service:
- GitHub Pages
- Netlify
- Vercel
- AWS S3
- Or any web server

Build the site with `hugo --minify` and deploy the `public/` directory.
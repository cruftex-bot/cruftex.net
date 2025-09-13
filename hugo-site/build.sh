#!/bin/bash
# Build script for cruftex.net Hugo site

echo "Building Hugo site..."
hugo --minify

echo "Build complete! Site generated in public/ directory"
echo "To serve locally: hugo server --bind 0.0.0.0 --port 12000"
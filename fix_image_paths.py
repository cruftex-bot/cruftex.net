#!/usr/bin/env python3

import os
import re
import shutil

def fix_image_paths():
    """Fix image paths in Hugo posts by removing CMS/ and G1/ prefixes and moving images to correct locations."""
    
    content_dir = "/workspace/project/cruftex.net/hugo-site/content/posts"
    
    # Process each markdown file
    for filename in os.listdir(content_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(content_dir, filename)
            post_dir = os.path.join(content_dir, filename[:-3])  # Remove .md extension
            
            print(f"Processing {filename}...")
            
            # Read the file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find all image references with CMS/ or G1/ prefixes
            cms_pattern = r'!\[([^\]]*)\]\(CMS/([^)]+)\)'
            g1_pattern = r'!\[([^\]]*)\]\(G1/([^)]+)\)'
            
            # Replace CMS/ references
            def replace_cms(match):
                alt_text = match.group(1)
                image_name = match.group(2)
                return f'![{alt_text}]({image_name})'
            
            def replace_g1(match):
                alt_text = match.group(1)
                image_name = match.group(2)
                return f'![{alt_text}]({image_name})'
            
            # Apply replacements
            original_content = content
            content = re.sub(cms_pattern, replace_cms, content)
            content = re.sub(g1_pattern, replace_g1, content)
            
            # Also fix links to CMS/ and G1/ files
            content = re.sub(r'\[([^\]]*)\]\(CMS/([^)]+)\)', r'[\1](\2)', content)
            content = re.sub(r'\[([^\]]*)\]\(G1/([^)]+)\)', r'[\1](\2)', content)
            
            # Write back if changed
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Updated {filename}")
            
            # Move images from CMS/ and G1/ subdirectories to the post directory
            if os.path.exists(post_dir):
                cms_dir = os.path.join(post_dir, 'CMS')
                g1_dir = os.path.join(post_dir, 'G1')
                
                # Move files from CMS/ directory
                if os.path.exists(cms_dir):
                    for img_file in os.listdir(cms_dir):
                        src = os.path.join(cms_dir, img_file)
                        dst = os.path.join(post_dir, img_file)
                        if os.path.isfile(src):
                            shutil.move(src, dst)
                            print(f"  Moved {img_file} from CMS/ to post directory")
                    # Remove empty CMS directory
                    try:
                        os.rmdir(cms_dir)
                    except OSError:
                        pass
                
                # Move files from G1/ directory
                if os.path.exists(g1_dir):
                    for img_file in os.listdir(g1_dir):
                        src = os.path.join(g1_dir, img_file)
                        dst = os.path.join(post_dir, img_file)
                        if os.path.isfile(src):
                            # Handle potential name conflicts
                            if os.path.exists(dst):
                                base, ext = os.path.splitext(img_file)
                                dst = os.path.join(post_dir, f"{base}-g1{ext}")
                            shutil.move(src, dst)
                            print(f"  Moved {img_file} from G1/ to post directory")
                    # Remove empty G1 directory
                    try:
                        os.rmdir(g1_dir)
                    except OSError:
                        pass

if __name__ == "__main__":
    fix_image_paths()
    print("Image path fixing complete!")
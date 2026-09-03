import os
import re

def build_frontend():
    for root, dirs, files in os.walk('.'):
        for file in files:
            filepath = os.path.join(root, file)
            
            # HTML ফাইল প্রসেসিং
            if file.endswith('.html'):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Absolute থেকে Relative Path-এ রূপান্তর
                content = re.sub(r'href="/(?!/)', 'href="./', content)
                content = re.sub(r'src="/(?!/)', 'src="./', content)
                
                # স্বয়ংক্রিয়ভাবে theme.css ইনজেক্ট করা
                if 'theme.css' not in content:
                    theme_link = '  <link rel="stylesheet" href="./theme.css">\n</head>'
                    content = content.replace('</head>', theme_link)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed HTML & Injected Theme: {filepath}")
                    
            # CSS ফাইল প্রসেসিং
            elif file.endswith('.css'):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # CSS এর ভেতরের url() ফিক্স করা
                content = re.sub(r'url\([\'"]?/(?!/)', "url('./", content)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed CSS: {filepath}")

if __name__ == "__main__":
    print("Starting frontend-only build...")
    build_frontend()
    print("Build completed!")

import re

def check_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    scripts = re.findall(r'<script(?! src)[^>]*>(.*?)</script>', html, flags=re.DOTALL)
    print(f'[{filename}] Found {len(scripts)} inline scripts.')
    for s in scripts:
        print('--- SCRIPT ---')
        print(s.strip()[:200] + '...' if len(s) > 200 else s.strip())

    handlers = re.findall(r'\b(on[a-z]+)=[\"\']', html, flags=re.IGNORECASE)
    print(f'[{filename}] Found inline handlers: {set(handlers)}')
    
    styles = re.findall(r'\bstyle=[\"\']', html, flags=re.IGNORECASE)
    print(f'[{filename}] Found {len(styles)} inline styles.')

check_file('index.html')
check_file('coming-soon.html')

import os
import re

files_to_scan = []
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for f in files:
        if f.endswith(('.html', '.js', '.css', '.json')):
            files_to_scan.append(os.path.join(root, f))

patterns = {
    'innerHTML': r'innerHTML',
    'outerHTML': r'outerHTML',
    'insertAdjacentHTML': r'insertAdjacentHTML',
    'eval': r'eval\(',
    'new Function': r'new Function\(',
    'window.location': r'window\.location',
    'location.href': r'location\.href',
    'location.assign': r'location\.assign',
    'location.replace': r'location\.replace',
    'window.open': r'window\.open',
    'document.write': r'document\.write',
    'setTimeout_string': r'setTimeout\([\"\']',
    'setInterval_string': r'setInterval\([\"\']',
    'target_blank': r'target=[\"\']_blank[\"\']',
    'script_src': r'<script[^>]+src=[\"\']([^\"\']+)[\"\']',
    'iframe': r'<iframe',
    'form_action': r'<form[^>]+action=[\"\']([^\"\']+)[\"\']',
    'localStorage': r'localStorage\.',
    'sessionStorage': r'sessionStorage\.'
}

results = {k: [] for k in patterns}

for filepath in files_to_scan:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            for key, pattern in patterns.items():
                matches = re.finditer(pattern, content, flags=re.IGNORECASE)
                for match in matches:
                    if key in ['script_src', 'form_action']:
                        val = match.group(1)
                        results[key].append(f'{filepath}: {val}')
                    else:
                        start = max(0, match.start() - 30)
                        end = min(len(content), match.end() + 30)
                        context = content[start:end].replace('\n', ' ').strip()
                        results[key].append(f'{filepath}: ...{context}...')
    except Exception as e:
        pass

for k, v in results.items():
    if v:
        print(f'\n--- {k.upper()} ---')
        for item in set(v):
            print(item)

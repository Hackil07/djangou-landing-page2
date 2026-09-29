import re
import os

def extract_scripts(html_file, js_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all inline scripts that are not JSON-LD
    # regex matches <script> ... </script> without src and type="application/ld+json"
    
    scripts = []
    
    def repl(match):
        attrs = match.group(1)
        content = match.group(2)
        if 'application/ld+json' in attrs:
            return match.group(0) # Keep JSON-LD
        if 'src=' in attrs:
            return match.group(0) # Keep external scripts
        
        scripts.append(content)
        return '' # Remove inline script

    new_html = re.sub(r'<script([^>]*)>(.*?)</script>', repl, html, flags=re.DOTALL | re.IGNORECASE)
    
    if scripts:
        with open(js_file, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(scripts))
        
        # Add the external script tag right before </body>
        new_html = new_html.replace('</body>', f'<script src="{js_file}"></script>\n</body>')
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f'Extracted scripts to {js_file} from {html_file}')
    else:
        print(f'No extractable scripts found in {html_file}')

extract_scripts('index.html', 'main.js')
extract_scripts('coming-soon.html', 'coming-soon.js')

# Remove inline handler in coming-soon.html: onclick="closeModal()"
with open('coming-soon.html', 'r', encoding='utf-8') as f:
    cs_html = f.read()

if 'onclick="closeModal()"' in cs_html:
    cs_html = cs_html.replace('onclick="closeModal()"', 'id="btn-close-modal"')
    with open('coming-soon.html', 'w', encoding='utf-8') as f:
        f.write(cs_html)
    
    # Add event listener to coming-soon.js
    with open('coming-soon.js', 'a', encoding='utf-8') as f:
        f.write('\ndocument.getElementById("btn-close-modal").addEventListener("click", closeModal);\n')
    print('Removed onclick handler from coming-soon.html')

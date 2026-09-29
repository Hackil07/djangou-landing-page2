import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update OG Image tags for WhatsApp compatibility
og_tags_addition = '''<meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="675">
    <meta property="og:image:type" content="image/jpeg">'''
    
# Find where og:image is and append the width/height/type tags right after it
html = re.sub(
    r'(<meta property="og:image" content="https://djangou-landing-page2\.vercel\.app/og-image\.jpg">)',
    r'\1\n    ' + og_tags_addition,
    html
)

# 2. Update Favicon tags for Google Search (replace logo.jpg with favicon.ico / logo.png)
html = re.sub(r'<link rel="icon" type="image/jpeg" href="logo\.jpg">', '<link rel="icon" type="image/x-icon" href="favicon.ico">\n    <link rel="icon" type="image/png" href="logo.png">', html)
html = re.sub(r'<link rel="shortcut icon" type="image/jpeg" href="logo\.jpg">', '<link rel="shortcut icon" type="image/x-icon" href="favicon.ico">', html)
html = re.sub(r'<link rel="apple-touch-icon" href="logo\.jpg">', '<link rel="apple-touch-icon" href="logo.png">', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html tags for SEO/WhatsApp")

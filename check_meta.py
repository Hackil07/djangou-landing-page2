import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('OG IMAGE:', re.search(r'<meta property=\"og:image\"[^>]*>', html))
print('CANONICAL:', re.search(r'<link rel=\"canonical\"[^>]*>', html))

# Let's also check the footer for where to insert the legal pages link
footer_match = re.search(r'<footer[^>]*>.*?</footer>', html, flags=re.DOTALL | re.IGNORECASE)
if footer_match:
    print('FOOTER FOUND')

import re

with open('coming-soon.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(
    r'(<p class=\"privacy-notice\"[^>]*>.*?<\/p>)',
    r'\1\n            <p style="text-align: center; margin-top: 0.5rem;"><a href="legal.html#confidentialite" style="font-size: 0.75rem; color: var(--color-primary); text-decoration: none;">Politique de confidentialité</a></p>',
    html
)

with open('coming-soon.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated coming-soon.html')

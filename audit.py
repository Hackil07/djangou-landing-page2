import re
from bs4 import BeautifulSoup

with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

print("--- NAVIGATION LINKS ---")
navs = soup.find_all('nav')
for nav in navs:
    for link in nav.find_all('a'):
        href = link.get('href', '')
        text = link.get_text(strip=True)
        if href.startswith('#') or href.startswith('/'):
            print(f"{text} -> {href}")

print("\n--- SECTIONS & HEADINGS ---")
sections = soup.find_all('section')
for sec in sections:
    sec_id = sec.get('id', 'NO-ID')
    print(f"\nSection ID: {sec_id}")
    for h in sec.find_all(['h2', 'h3']):
        print(f"  Heading ({h.name}): {h.get_text(strip=True)}")

print("\n--- FOOTER LINKS ---")
footer = soup.find('footer')
if footer:
    for link in footer.find_all('a'):
        href = link.get('href', '')
        text = link.get_text(strip=True)
        if href.startswith('#') or href.startswith('/'):
            print(f"{text} -> {href}")


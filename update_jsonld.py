import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_json = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Djangou",
      "applicationCategory": "EducationalApplication",
      "operatingSystem": "Web",
      "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "XOF"
      }
    }
    </script>'''

new_json = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "Djangou",
      "applicationCategory": "EducationalApplication",
      "operatingSystem": "Web",
      "offers": [
        {
          "@type": "Offer",
          "name": "Start",
          "price": "1500",
          "priceCurrency": "XOF"
        },
        {
          "@type": "Offer",
          "name": "Premium",
          "price": "3000",
          "priceCurrency": "XOF"
        }
      ]
    }
    </script>'''

if old_json in html:
    html = html.replace(old_json, new_json)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("JSON-LD successfully updated!")
else:
    print("Could not find the exact old JSON-LD string.")

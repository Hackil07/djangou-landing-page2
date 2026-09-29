import json
with open('vercel.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

csp_idx = next(i for i, h in enumerate(data['headers'][0]['headers']) if h['key'] == 'Content-Security-Policy')
data['headers'][0]['headers'][csp_idx]['value'] = "default-src 'none'; script-src 'self' https://cdn.jsdelivr.net; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' data:; connect-src 'self' https://api.emailjs.com https://formspree.io; frame-ancestors 'none'; base-uri 'self'; form-action 'self' https://formspree.io;"

with open('vercel.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

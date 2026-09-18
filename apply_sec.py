import re

# 1. Add SRI to EmailJS in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sri = 'sha384-SALc35EccAf6RzGw4iNsyj7kTPr33K7RoGzYu+7heZhT8s0GZouafRiCg1qy44AS'
old_script = '<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>'
new_script = f'<script type="text/javascript" src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js" integrity="{sri}" crossorigin="anonymous"></script>'

html = html.replace(old_script, new_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Added SRI to index.html')

# 2. Update coming-soon.html redirect UI
with open('coming-soon.html', 'r', encoding='utf-8') as f:
    cs_html = f.read()

old_redirect = "document.querySelector('.countdown').innerHTML = `<h2 style=\"grid-column: 1 / -1;\">${window.i18n.t('cs.js.redirect')}</h2>`;"
new_redirect = """document.querySelector('.countdown').innerHTML = `
                    <div style="grid-column: 1 / -1; display: flex; flex-direction: column; align-items: center; justify-content: center; animation: slideUp 0.5s ease;">
                        <svg class="modal-icon" style="width: 50px; height: 50px; margin-bottom: 1rem; color: var(--color-primary);" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
                            <polyline points="22 4 12 14.01 9 11.01"></polyline>
                        </svg>
                        <h2>Redirection sécurisée vers l'espace officiel...</h2>
                    </div>
                `;"""

cs_html = cs_html.replace(old_redirect, new_redirect)

with open('coming-soon.html', 'w', encoding='utf-8') as f:
    f.write(cs_html)
print('Updated coming-soon.html redirect UI')

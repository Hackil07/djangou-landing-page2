import re

# 1. Create legal.html
legal_html = """<!DOCTYPE html>
<html lang="fr" dir="ltr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DJANGOU - Mentions Légales et Politique de Confidentialité</title>
    <meta name="robots" content="noindex, nofollow">
    <meta name="theme-color" content="#6d28d9">
    <style>
        :root {
            --color-primary: #6d28d9;
            --color-bg: #f8fafc;
            --color-text: #0f172a;
            --color-text-muted: #64748b;
            --color-card: #ffffff;
            --font-main: system-ui, -apple-system, sans-serif;
        }
        [data-theme="dark"] {
            --color-bg: #0f172a;
            --color-text: #f8fafc;
            --color-text-muted: #94a3b8;
            --color-card: #1e293b;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: var(--font-main); background-color: var(--color-bg); color: var(--color-text); line-height: 1.6; }
        .container { max-width: 800px; margin: 0 auto; padding: 4rem 2rem; }
        .logo { height: 40px; margin-bottom: 2rem; border-radius: 8px; }
        h1 { font-size: 2.5rem; margin-bottom: 2rem; color: var(--color-text); }
        h2 { font-size: 1.5rem; margin-top: 2.5rem; margin-bottom: 1rem; color: var(--color-primary); }
        h3 { font-size: 1.2rem; margin-top: 1.5rem; margin-bottom: 0.5rem; }
        p { margin-bottom: 1rem; color: var(--color-text-muted); }
        ul { margin-bottom: 1rem; margin-left: 2rem; color: var(--color-text-muted); }
        .btn-back { display: inline-flex; align-items: center; padding: 0.8rem 1.5rem; border-radius: 50px; background: transparent; color: var(--color-text); border: 2px solid var(--color-text-muted); text-decoration: none; font-weight: 600; margin-bottom: 2rem; transition: all 0.2s ease; }
        .btn-back:hover { background: var(--color-text); color: var(--color-bg); }
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" class="btn-back">← Retour à l'accueil</a>
        
        <h1>Mentions Légales & Confidentialité</h1>

        <section id="mentions-legales">
            <h2>1. Mentions Légales</h2>
            <p><strong>Éditeur du site :</strong> DJANGOU EdTech</p>
            <p><strong>Contact :</strong> djangousupportpro@gmail.com</p>
            <p><strong>Hébergement :</strong> Vercel Inc., 340 S Lemon Ave #4133, Walnut, CA 91789, USA.</p>
            <p><strong>Propriété intellectuelle :</strong> L'ensemble de ce site relève de la législation sur le droit d'auteur et la propriété intellectuelle. Tous les droits de reproduction sont réservés.</p>
        </section>

        <section id="confidentialite">
            <h2>2. Politique de Confidentialité (RGPD)</h2>
            
            <h3>Collecte des données</h3>
            <p>Dans le cadre de son fonctionnement et de la liste d'attente, DJANGOU est susceptible de collecter les données suivantes :</p>
            <ul>
                <li>Nom complet</li>
                <li>Adresse e-mail</li>
                <li>Profil (Enseignant, Directeur, etc.)</li>
                <li>Taille de l'établissement (optionnel)</li>
            </ul>

            <h3>Finalité du traitement</h3>
            <p>Les informations recueillies sont exclusivement destinées à la planification du lancement de l'application DJANGOU et à vous informer de la disponibilité de nos services. <strong>Vos données ne sont jamais vendues ou partagées avec des tiers à des fins commerciales.</strong></p>

            <h3>Conservation et Sécurité</h3>
            <p>Vos données sont conservées de manière sécurisée et ne seront gardées que le temps nécessaire aux finalités pour lesquelles elles ont été collectées. Notre architecture utilise des protocoles sécurisés (HTTPS, CSP) pour empêcher tout accès non autorisé.</p>

            <h3>Vos droits</h3>
            <p>Conformément aux réglementations en vigueur (notamment le RGPD), vous disposez d'un droit d'accès, de rectification, de portabilité et de suppression de vos données personnelles. Vous pouvez exercer ce droit en nous contactant à l'adresse suivante : <strong>djangousupportpro@gmail.com</strong>.</p>

            <h3>Cookies</h3>
            <p>DJANGOU n'utilise que des cookies/stockages locaux strictement nécessaires au fonctionnement du site (ex: mémorisation de la langue et du thème). Aucun cookie de traçage publicitaire intrusif n'est utilisé sans votre consentement explicite.</p>
        </section>

    </div>
</body>
</html>
"""

with open('legal.html', 'w', encoding='utf-8') as f:
    f.write(legal_html)

print("Created legal.html")

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace dummy links in the legal footer section
html = re.sub(
    r'<a href=\"https://djangou-landing-page2\.vercel\.app\" data-i18n=\"idx\.footer\.priv\">',
    r'<a href="legal.html#confidentialite" data-i18n="idx.footer.priv">',
    html
)

html = re.sub(
    r'<a href=\"https://djangou-landing-page2\.vercel\.app\" data-i18n=\"idx\.footer\.term\">',
    r'<a href="legal.html#mentions-legales" data-i18n="idx.footer.term">',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html")

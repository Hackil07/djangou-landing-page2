import os

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    # Testimonials
    '''<span class="eyebrow">Ils nous font confiance</span>''': '''<span class="eyebrow" data-i18n="idx.test.eyebrow">Ils nous font confiance</span>''',
    '''<h2>Adopté par des établissements innovants</h2>''': '''<h2 data-i18n="idx.test.h2">Adopté par des établissements innovants</h2>''',
    '''<p>Découvrez prochainement les retours d'expérience des écoles partenaires qui ont transformé leur gestion administrative avec DJANGOU.</p>''': '''<p data-i18n="idx.test.desc">Découvrez prochainement les retours d'expérience des écoles partenaires qui ont transformé leur gestion administrative avec DJANGOU.</p>''',
    '''<p style="color: var(--color-text-muted); font-style: italic; margin-bottom: 1.5rem;">« Emplacement réservé pour le futur témoignage d'un directeur d'établissement détaillant le temps gagné chaque trimestre. »</p>''': '''<p style="color: var(--color-text-muted); font-style: italic; margin-bottom: 1.5rem;" data-i18n="idx.test.1.p">« Emplacement réservé pour le futur témoignage d'un directeur d'établissement détaillant le temps gagné chaque trimestre. »</p>''',
    '''<h4 style="font-size: 1rem;">Directeur, Établissement Partenaire</h4>''': '''<h4 style="font-size: 1rem;" data-i18n="idx.test.1.h4">Directeur, Établissement Partenaire</h4>''',
    '''<p style="color: var(--color-text-muted); font-style: italic; margin-bottom: 1.5rem;">« Emplacement réservé pour l'avis d'un enseignant sur l'efficacité de la dictée vocale et la facilité de prise en main. »</p>''': '''<p style="color: var(--color-text-muted); font-style: italic; margin-bottom: 1.5rem;" data-i18n="idx.test.2.p">« Emplacement réservé pour l'avis d'un enseignant sur l'efficacité de la dictée vocale et la facilité de prise en main. »</p>''',
    '''<h4 style="font-size: 1rem;">Enseignant Principal</h4>''': '''<h4 style="font-size: 1rem;" data-i18n="idx.test.2.h4">Enseignant Principal</h4>''',

    # Contact
    '''<span class="eyebrow">Contactez-nous</span>''': '''<span class="eyebrow" data-i18n="idx.contact.eyebrow">Contactez-nous</span>''',
    '''<h2>Une question ? Parlons-en.</h2>''': '''<h2 data-i18n="idx.contact.h2">Une question ? Parlons-en.</h2>''',
    '''<p>Notre équipe est disponible pour répondre à toutes vos questions sur DJANGOU.</p>''': '''<p data-i18n="idx.contact.desc">Notre équipe est disponible pour répondre à toutes vos questions sur DJANGOU.</p>''',
    '''<h4>Disponibilité</h4>''': '''<h4 data-i18n="idx.contact.disp.h4">Disponibilité</h4>''',
    '''<p>Lun – Ven, 8h – 18h (WAT)</p>''': '''<p data-i18n="idx.contact.disp.p">Lun – Ven, 8h – 18h (WAT)</p>''',
    '''Réponse généralement sous 24h''': '''<span data-i18n="idx.contact.badge">Réponse généralement sous 24h</span>''',
    '''<label for="contact-name">Nom complet <span aria-hidden="true">*</span></label>''': '''<label for="contact-name"><span data-i18n="idx.contact.form.name">Nom complet</span> <span aria-hidden="true">*</span></label>''',
    '''placeholder="Ex : Moussa Diallo"''': '''placeholder="Ex : Moussa Diallo" data-i18n-placeholder="idx.contact.form.name_ph"''',
    '''<span class="field-error" id="error-name">Veuillez entrer votre nom (min. 2 caractères).</span>''': '''<span class="field-error" id="error-name" data-i18n="idx.contact.form.name_err">Veuillez entrer votre nom (min. 2 caractères).</span>''',
    '''<label for="contact-email">Adresse e-mail <span aria-hidden="true">*</span></label>''': '''<label for="contact-email"><span data-i18n="idx.contact.form.email">Adresse e-mail</span> <span aria-hidden="true">*</span></label>''',
    '''placeholder="Ex : moussa@ecole.sn"''': '''placeholder="Ex : moussa@ecole.sn" data-i18n-placeholder="idx.contact.form.email_ph"''',
    '''<span class="field-error" id="error-email">Veuillez entrer une adresse e-mail valide.</span>''': '''<span class="field-error" id="error-email" data-i18n="idx.contact.form.email_err">Veuillez entrer une adresse e-mail valide.</span>''',
    '''<label for="contact-subject">Sujet</label>''': '''<label for="contact-subject" data-i18n="idx.contact.form.subject">Sujet</label>''',
    '''placeholder="Ex : Question sur les bulletins"''': '''placeholder="Ex : Question sur les bulletins" data-i18n-placeholder="idx.contact.form.subject_ph"''',
    '''<label for="contact-message">Message <span aria-hidden="true">*</span></label>''': '''<label for="contact-message"><span data-i18n="idx.contact.form.message">Message</span> <span aria-hidden="true">*</span></label>''',
    '''placeholder="Décrivez votre question ou besoin..."''': '''placeholder="Décrivez votre question ou besoin..." data-i18n-placeholder="idx.contact.form.message_ph"''',
    '''<span class="field-error" id="error-message">Veuillez entrer un message (min. 10 caractères).</span>''': '''<span class="field-error" id="error-message" data-i18n="idx.contact.form.message_err">Veuillez entrer un message (min. 10 caractères).</span>''',
    '''<span class="btn-text">Envoyer le message</span>''': '''<span class="btn-text" data-i18n="idx.contact.form.submit">Envoyer le message</span>''',
    '''Message envoyé avec succès ! Nous vous répondrons sous 24h.''': '''<span data-i18n="idx.contact.form.success">Message envoyé avec succès ! Nous vous répondrons sous 24h.</span>''',
    '''Une erreur s'est produite. Veuillez réessayer ou nous écrire directement à djangousupportpro@gmail.com.''': '''<span data-i18n="idx.contact.form.error">Une erreur s'est produite. Veuillez réessayer ou nous écrire directement à djangousupportpro@gmail.com.</span>''',
    
    # CTA Final
    '''<h2>Moins de saisie. Plus de temps pour enseigner.</h2>''': '''<h2 data-i18n="idx.cta.h2">Moins de saisie. Plus de temps pour enseigner.</h2>''',
    '''<p>Rejoignez les enseignants et directeurs qui modernisent leur gestion scolaire.</p>''': '''<p data-i18n="idx.cta.desc">Rejoignez les enseignants et directeurs qui modernisent leur gestion scolaire.</p>''',
    '''<a href="coming-soon.html" class="btn btn-white">Découvrir DJANGOU</a>''': '''<a href="coming-soon.html" class="btn btn-white" data-i18n="idx.cta.btn">Découvrir DJANGOU</a>''',

    # Footer
    '''<p style="margin-top: 1rem; max-width: 300px;">La plateforme EdTech de gestion scolaire conçue pour fonctionner avec ou sans connexion internet.</p>''': '''<p style="margin-top: 1rem; max-width: 300px;" data-i18n="idx.footer.desc">La plateforme EdTech de gestion scolaire conçue pour fonctionner avec ou sans connexion internet.</p>''',
    '''<h3 class="footer-heading">Produit</h3>''': '''<h3 class="footer-heading" data-i18n="idx.footer.prod">Produit</h3>''',
    '''<a href="#fonctionnalites">Fonctionnalités</a>''': '''<a href="#fonctionnalites" data-i18n="idx.nav.feat">Fonctionnalités</a>''',
    '''<a href="#offline">Mode Hors-ligne</a>''': '''<a href="#offline" data-i18n="idx.footer.offline">Mode Hors-ligne</a>''',
    '''<a href="#ia">Intelligence IA</a>''': '''<a href="#ia" data-i18n="idx.footer.ia">Intelligence IA</a>''',
    '''<a href="#securite">Sécurité</a>''': '''<a href="#securite" data-i18n="idx.footer.sec">Sécurité</a>''',
    '''<h3 class="footer-heading">Ressources</h3>''': '''<h3 class="footer-heading" data-i18n="idx.footer.res">Ressources</h3>''',
    '''<a href="#faq">Questions fréquentes (FAQ)</a>''': '''<a href="#faq" data-i18n="idx.footer.faq">Questions fréquentes (FAQ)</a>''',
    '''<a href="coming-soon.html">Connexion</a>''': '''<a href="coming-soon.html" data-i18n="idx.footer.login">Connexion</a>''',
    '''<a href="coming-soon.html">Inscription</a>''': '''<a href="coming-soon.html" data-i18n="idx.footer.signup">Inscription</a>''',
    '''<h3 class="footer-heading">Légal</h3>''': '''<h3 class="footer-heading" data-i18n="idx.footer.leg">Légal</h3>''',
    '''<a href="https://djangou-landing-page2.vercel.app">Confidentialité</a>''': '''<a href="https://djangou-landing-page2.vercel.app" data-i18n="idx.footer.priv">Confidentialité</a>''',
    '''<a href="https://djangou-landing-page2.vercel.app">Conditions d'utilisation</a>''': '''<a href="https://djangou-landing-page2.vercel.app" data-i18n="idx.footer.term">Conditions d'utilisation</a>''',
    '''<p>&copy; 2026 DJANGOU. Tous droits réservés.</p>''': '''<p data-i18n="idx.footer.copy">&copy; 2026 DJANGOU. Tous droits réservés.</p>''',
    '''<p>Propulsé par l'innovation EdTech.</p>''': '''<p data-i18n="idx.footer.prop">Propulsé par l'innovation EdTech.</p>''',

    # Scripts strings
    '''const textToType = "même sans connexion.";''': '''const textToType = window.i18n ? window.i18n.t('idx.js.typewriter') : "même sans connexion.";''',
    
    # RGPD
    '''<strong>Votre vie privée est importante.</strong> Nous utilisons uniquement les cookies nécessaires au bon fonctionnement de la plateforme (comme le thème sombre).''': '''<span data-i18n="idx.rgpd.text"><strong>Votre vie privée est importante.</strong> Nous utilisons uniquement les cookies nécessaires au bon fonctionnement de la plateforme (comme le thème sombre).</span>''',
    '''<button id="rgpd-decline" class="rgpd-btn rgpd-decline">Continuer sans accepter</button>''': '''<button id="rgpd-decline" class="rgpd-btn rgpd-decline" data-i18n="idx.rgpd.decline">Continuer sans accepter</button>''',
    '''<button id="rgpd-accept" class="rgpd-btn rgpd-accept">J'accepte</button>''': '''<button id="rgpd-accept" class="rgpd-btn rgpd-accept" data-i18n="idx.rgpd.accept">J'accepte</button>''',
    
    # Global injectors
    '</head>': '<script src="i18n-dictionary.js"></script>\n    <script src="i18n.js"></script>\n</head>',
    '<button id="theme-toggle"': '<select class="lang-selector" style="background: transparent; color: var(--color-text-main); border: 1px solid var(--color-border); border-radius: 4px; padding: 0.2rem; cursor: pointer; font-family: inherit;"><option value="fr">FR</option><option value="en">EN</option></select>\n                        <button id="theme-toggle"'
}

for k, v in replacements.items():
    content = content.replace(k, v)

# Update Typewriter to listen to language changes
content = content.replace('''setTimeout(typeWriter, 1000); // Initial delay
            }''', '''setTimeout(typeWriter, 1000); // Initial delay
                window.addEventListener('languageChanged', (e) => {
                    const newText = window.i18n.t('idx.js.typewriter');
                    typeWriterEl.innerHTML = `<span class="text-gradient">${newText}</span>`;
                });
            }''')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html part 3 modified")

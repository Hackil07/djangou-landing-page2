import os

file_path = "coming-soon.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    '<title>DJANGOU - Bientôt Disponible</title>': '<title data-i18n="cs.title">DJANGOU - Bientôt Disponible</title>',
    '''<h1>L'application est <span class="highlight">bientôt là.</span></h1>''': '''<h1><span data-i18n="cs.h1_1">L'application est </span><span class="highlight" data-i18n="cs.h1_2">bientôt là.</span></h1>''',
    '''<p>L'équipe DJANGOU prépare le déploiement officiel de l'application. La révolution EdTech commence dans :</p>''': '''<p data-i18n="cs.desc">L'équipe DJANGOU prépare le déploiement officiel de l'application. La révolution EdTech commence dans :</p>''',
    '''<div class="time-label">Jours</div>''': '''<div class="time-label" data-i18n="cs.days">Jours</div>''',
    '''<div class="time-label">Heures</div>''': '''<div class="time-label" data-i18n="cs.hours">Heures</div>''',
    '''<div class="time-label">Minutes</div>''': '''<div class="time-label" data-i18n="cs.minutes">Minutes</div>''',
    '''<div class="time-label">Secondes</div>''': '''<div class="time-label" data-i18n="cs.seconds">Secondes</div>''',
    '''<h2>Rejoignez la liste d'attente</h2>''': '''<h2 data-i18n="cs.waitlist.title">Rejoignez la liste d'attente</h2>''',
    '''<p class="waitlist-desc">Soyez le premier averti lors du lancement officiel et aidez-nous à dimensionner l'application pour votre arrivée.</p>''': '''<p class="waitlist-desc" data-i18n="cs.waitlist.desc">Soyez le premier averti lors du lancement officiel et aidez-nous à dimensionner l'application pour votre arrivée.</p>''',
    '''placeholder="Votre nom complet"''': '''placeholder="Votre nom complet" data-i18n-placeholder="cs.placeholder.name"''',
    '''placeholder="Votre adresse e-mail"''': '''placeholder="Votre adresse e-mail" data-i18n-placeholder="cs.placeholder.email"''',
    '''<option value="" disabled selected>Quel est votre profil ?</option>''': '''<option value="" disabled selected data-i18n="cs.role.default">Quel est votre profil ?</option>''',
    '''<option value="Directeur/Fondateur">Directeur / Fondateur d'établissement</option>''': '''<option value="Directeur/Fondateur" data-i18n="cs.role.dir">Directeur / Fondateur d'établissement</option>''',
    '''<option value="Enseignant">Enseignant / Professeur</option>''': '''<option value="Enseignant" data-i18n="cs.role.prof">Enseignant / Professeur</option>''',
    '''<option value="Personnel Administratif">Personnel Administratif</option>''': '''<option value="Personnel Administratif" data-i18n="cs.role.admin">Personnel Administratif</option>''',
    '''<option value="Parent/Élève">Parent d'élève / Élève</option>''': '''<option value="Parent/Élève" data-i18n="cs.role.parent">Parent d'élève / Élève</option>''',
    '''<option value="Autre">Autre</option>''': '''<option value="Autre" data-i18n="cs.role.other">Autre</option>''',
    '''<option value="" disabled selected>Taille de l'établissement (Optionnel)</option>''': '''<option value="" disabled selected data-i18n="cs.size.default">Taille de l'établissement (Optionnel)</option>''',
    '''<option value="Moins de 100">Moins de 100 élèves</option>''': '''<option value="Moins de 100" data-i18n="cs.size.100">Moins de 100 élèves</option>''',
    '''<option value="100 à 500">De 100 à 500 élèves</option>''': '''<option value="100 à 500" data-i18n="cs.size.100_500">De 100 à 500 élèves</option>''',
    '''<option value="Plus de 500">Plus de 500 élèves</option>''': '''<option value="Plus de 500" data-i18n="cs.size.500">Plus de 500 élèves</option>''',
    '''<option value="Je ne sais pas/Non applicable">Je ne sais pas / Non applicable</option>''': '''<option value="Je ne sais pas/Non applicable" data-i18n="cs.size.na">Je ne sais pas / Non applicable</option>''',
    '''<button type="submit" class="btn-submit">M'avertir du lancement</button>''': '''<button type="submit" class="btn-submit" data-i18n="cs.btn.submit">M'avertir du lancement</button>''',
    '''<p class="privacy-notice">Vos données serviront uniquement pour la planification du lancement.</p>''': '''<p class="privacy-notice" data-i18n="cs.privacy">Vos données serviront uniquement pour la planification du lancement.</p>''',
    '''<a href="index.html" class="btn-back">← Retour à l'accueil</a>''': '''<a href="index.html" class="btn-back" data-i18n="cs.back">← Retour à l'accueil</a>''',
    '''<h3>Merci pour votre temps et intérêt pour notre projet !</h3>''': '''<h3 data-i18n="cs.modal.title">Merci pour votre temps et intérêt pour notre projet !</h3>''',
    '''<p>Votre inscription à la liste d'attente a bien été prise en compte. Nous vous contacterons dès le lancement officiel de DJANGOU.</p>''': '''<p data-i18n="cs.modal.desc">Votre inscription à la liste d'attente a bien été prise en compte. Nous vous contacterons dès le lancement officiel de DJANGOU.</p>''',
    '''<button class="btn-close-modal" onclick="closeModal()">Fermer</button>''': '''<button class="btn-close-modal" onclick="closeModal()" data-i18n="cs.modal.close">Fermer</button>''',
    
    # Scripts replacements
    "submitBtn.innerText = 'Envoi en cours...';": "submitBtn.innerText = window.i18n.t('cs.js.sending');",
    'alert("Une erreur s\'est produite. Veuillez réessayer.");': "alert(window.i18n.t('cs.js.error'));",
    'alert("Erreur de connexion. Veuillez vérifier votre internet.");': "alert(window.i18n.t('cs.js.conn_error'));",
    '''innerHTML = '<h2 style="grid-column: 1 / -1;">Déploiement en cours... Redirection...</h2>';''': '''innerHTML = `<h2 style="grid-column: 1 / -1;">${window.i18n.t('cs.js.redirect')}</h2>`;''',
    
    # Inject scripts at the end of head
    '</head>': '<script src="i18n-dictionary.js"></script>\n    <script src="i18n.js"></script>\n</head>',
    
    # Inject language switcher in coming soon page at the top right
    '<div class="container">': '<div class="lang-switch-container" style="position: absolute; top: 1rem; right: 1rem; z-index: 50;"><select class="lang-selector" style="background: var(--color-card); color: var(--color-text); border: 1px solid var(--color-text-muted); padding: 5px; border-radius: 4px;"><option value="fr">FR</option><option value="en">EN</option></select></div>\n    <div class="container">'
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("coming-soon.html modified")

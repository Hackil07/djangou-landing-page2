import os

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    # Head / Meta
    '''<title>DJANGOU - Logiciel de gestion scolaire</title>''': '''<title data-i18n="idx.title">DJANGOU - Logiciel de gestion scolaire</title>''',
    
    # Navbar
    '''<a href="#fonctionnalites">Fonctionnalités</a>''': '''<a href="#fonctionnalites" data-i18n="idx.nav.feat">Fonctionnalités</a>''',
    '''<a href="#offline">Hors-ligne</a>''': '''<a href="#offline" data-i18n="idx.nav.offline">Hors-ligne</a>''',
    '''<a href="#faq">FAQ</a>''': '''<a href="#faq" data-i18n="idx.nav.faq">FAQ</a>''',
    '''<a href="#contact">Contact</a>''': '''<a href="#contact" data-i18n="idx.nav.contact">Contact</a>''',
    '''aria-label="Basculer le thème"''': '''aria-label="Basculer le thème" data-i18n-aria="idx.aria.theme"''',
    '''<a href="coming-soon.html" class="btn btn-primary">Accéder à DJANGOU</a>''': '''<a href="coming-soon.html" class="btn btn-primary" data-i18n="idx.nav.cta">Accéder à DJANGOU</a>''',
    
    # Hero
    '''<span class="eyebrow">La plateforme EdTech adaptée à votre réalité</span>''': '''<span class="eyebrow" data-i18n="idx.hero.eyebrow">La plateforme EdTech adaptée à votre réalité</span>''',
    '''<span class="visually-hidden">Logiciel de gestion scolaire intelligent et hors-ligne.</span>''': '''<span class="visually-hidden" data-i18n="idx.hero.hidden">Logiciel de gestion scolaire intelligent et hors-ligne.</span>''',
    '''<p>DJANGOU automatise la saisie des notes, la correction et la génération des bulletins scolaires. Une application performante pensée pour les enseignants et directeurs qui veulent gagner du temps.</p>''': '''<p data-i18n="idx.hero.desc">DJANGOU automatise la saisie des notes, la correction et la génération des bulletins scolaires. Une application performante pensée pour les enseignants et directeurs qui veulent gagner du temps.</p>''',
    '''<a href="coming-soon.html" class="btn btn-primary">Découvrir DJANGOU</a>''': '''<a href="coming-soon.html" class="btn btn-primary" data-i18n="idx.hero.cta1">Découvrir DJANGOU</a>''',
    '''<a href="#fonctionnalites" class="btn btn-secondary">Voir le fonctionnement</a>''': '''<a href="#fonctionnalites" class="btn btn-secondary" data-i18n="idx.hero.cta2">Voir le fonctionnement</a>''',
    '''IA en temps réel''': '''<span data-i18n="idx.hero.chip1">IA en temps réel</span>''',
    '''100% Hors-ligne''': '''<span data-i18n="idx.hero.chip2">100% Hors-ligne</span>''',
    
    # Features
    '''<h2>Moins de saisie manuelle. Plus de temps pour enseigner.</h2>''': '''<h2 data-i18n="idx.feat.h2">Moins de saisie manuelle. Plus de temps pour enseigner.</h2>''',
    '''<p>Découvrez comment nos fonctionnalités repensent le travail administratif scolaire pour éliminer les tâches répétitives et chronophages.</p>''': '''<p data-i18n="idx.feat.desc">Découvrez comment nos fonctionnalités repensent le travail administratif scolaire pour éliminer les tâches répétitives et chronophages.</p>''',
    '''<h3>Offline-First</h3>''': '''<h3 data-i18n="idx.feat.1.h3">Offline-First</h3>''',
    '''<p>Continuez à travailler normalement même lorsque la connexion internet est coupée. Synchronisation automatique au retour du réseau.</p>''': '''<p data-i18n="idx.feat.1.p">Continuez à travailler normalement même lorsque la connexion internet est coupée. Synchronisation automatique au retour du réseau.</p>''',
    '''<h3>Dictée Vocale Intelligente</h3>''': '''<h3 data-i18n="idx.feat.2.h3">Dictée Vocale Intelligente</h3>''',
    '''<p>Énoncez vos notes à voix haute. L'IA les comprend et remplit automatiquement le tableau des élèves depuis votre téléphone.</p>''': '''<p data-i18n="idx.feat.2.p">Énoncez vos notes à voix haute. L'IA les comprend et remplit automatiquement le tableau des élèves depuis votre téléphone.</p>''',
    '''<h3>Scan et OCR par IA</h3>''': '''<h3 data-i18n="idx.feat.3.h3">Scan et OCR par IA</h3>''',
    '''<p>Photographiez les documents ou copies compatibles. L'IA extrait automatiquement les informations pour réduire la saisie manuelle.</p>''': '''<p data-i18n="idx.feat.3.p">Photographiez les documents ou copies compatibles. L'IA extrait automatiquement les informations pour réduire la saisie manuelle.</p>''',
    '''<h3>Barèmes Automatisés</h3>''': '''<h3 data-i18n="idx.feat.4.h3">Barèmes Automatisés</h3>''',
    '''<p>L'IA vous assiste pour structurer des critères de correction, facilitant le calcul automatique et rapide des moyennes globales.</p>''': '''<p data-i18n="idx.feat.4.p">L'IA vous assiste pour structurer des critères de correction, facilitant le calcul automatique et rapide des moyennes globales.</p>''',
    '''<h3>Bulletins PDF en masse</h3>''': '''<h3 data-i18n="idx.feat.5.h3">Bulletins PDF en masse</h3>''',
    '''<p>Générez instantanément des bulletins scolaires professionnels au format PDF pour l'ensemble d'une classe en un seul clic.</p>''': '''<p data-i18n="idx.feat.5.p">Générez instantanément des bulletins scolaires professionnels au format PDF pour l'ensemble d'une classe en un seul clic.</p>''',
    '''<h3>Procès-Verbaux Excel</h3>''': '''<h3 data-i18n="idx.feat.6.h3">Procès-Verbaux Excel</h3>''',
    '''<p>Exportez facilement les relevés complets et procès-verbaux au format Excel pour les réunions d'administration.</p>''': '''<p data-i18n="idx.feat.6.p">Exportez facilement les relevés complets et procès-verbaux au format Excel pour les réunions d'administration.</p>''',
    
    # IA Section
    '''<span class="eyebrow">Intelligence Artificielle</span>''': '''<span class="eyebrow" data-i18n="idx.ia.eyebrow">Intelligence Artificielle</span>''',
    '''<h2>Dictée vocale : l'IA au service de votre productivité.</h2>''': '''<h2 data-i18n="idx.ia.h2">Dictée vocale : l'IA au service de votre productivité.</h2>''',
    '''<p>Saisissez vos notes beaucoup plus rapidement, même depuis un smartphone. Activez le micro, énoncez la note de l'élève, et DJANGOU s'occupe de l'associer à la bonne ligne dans votre classeur numérique.</p>''': '''<p data-i18n="idx.ia.desc">Saisissez vos notes beaucoup plus rapidement, même depuis un smartphone. Activez le micro, énoncez la note de l'élève, et DJANGOU s'occupe de l'associer à la bonne ligne dans votre classeur numérique.</p>''',
    '''<span>Réduit le risque d'erreur de saisie manuelle.</span>''': '''<span data-i18n="idx.ia.li1">Réduit le risque d'erreur de saisie manuelle.</span>''',
    '''<span>Extrêmement pratique depuis un écran de smartphone.</span>''': '''<span data-i18n="idx.ia.li2">Extrêmement pratique depuis un écran de smartphone.</span>''',
    '''« Martin, 15 sur 20 »''': '''<span data-i18n="idx.ia.demo.voice">« Martin, 15 sur 20 »</span>''',
    '''<th>Élève</th>''': '''<th data-i18n="idx.ia.th1">Élève</th>''',
    '''<th>Devoir 1</th>''': '''<th data-i18n="idx.ia.th2">Devoir 1</th>''',
    '''<th>Statut</th>''': '''<th data-i18n="idx.ia.th3">Statut</th>''',
    '''<td><span style="color: var(--color-text-muted);">Saisi</span></td>''': '''<td><span style="color: var(--color-text-muted);" data-i18n="idx.ia.td.saisi">Saisi</span></td>''',
    '''<td><span class="highlight-text">Ajouté par voix</span></td>''': '''<td><span class="highlight-text" data-i18n="idx.ia.td.voice">Ajouté par voix</span></td>''',
    '''<td><span style="color: var(--color-text-muted);">En attente</span></td>''': '''<td><span style="color: var(--color-text-muted);" data-i18n="idx.ia.td.waiting">En attente</span></td>''',
    
    # OCR Section
    '''<span class="eyebrow">Vision par Ordinateur</span>''': '''<span class="eyebrow" data-i18n="idx.ocr.eyebrow">Vision par Ordinateur</span>''',
    '''<h2>Scan et OCR : Digitalisez en un clic.</h2>''': '''<h2 data-i18n="idx.ocr.h2">Scan et OCR : Digitalisez en un clic.</h2>''',
    '''<p>Photographiez les documents ou copies compatibles. L'IA extrait automatiquement les informations pour réduire la saisie manuelle. Un gain de temps inestimable pour le traitement des fiches papier.</p>''': '''<p data-i18n="idx.ocr.desc">Photographiez les documents ou copies compatibles. L'IA extrait automatiquement les informations pour réduire la saisie manuelle. Un gain de temps inestimable pour le traitement des fiches papier.</p>''',
    '''<span>Fini la double saisie des listes d'élèves.</span>''': '''<span data-i18n="idx.ocr.li1">Fini la double saisie des listes d'élèves.</span>''',
    '''<span>Reconnaissance d'écriture optimisée.</span>''': '''<span data-i18n="idx.ocr.li2">Reconnaissance d'écriture optimisée.</span>''',
    '''Extraction réussie''': '''<span data-i18n="idx.ocr.success">Extraction réussie</span>''',
    
    # Offline Section
    '''<span class="eyebrow">Résilience réseau</span>''': '''<span class="eyebrow" data-i18n="idx.off.eyebrow">Résilience réseau</span>''',
    '''<h2>L'approche Offline-First.</h2>''': '''<h2 data-i18n="idx.off.h2">L'approche Offline-First.</h2>''',
    '''<p>Dans les environnements où la connexion est lente, instable ou coûteuse, DJANGOU garantit la continuité de votre travail. Vos données récentes sont stockées localement.</p>''': '''<p data-i18n="idx.off.desc">Dans les environnements où la connexion est lente, instable ou coûteuse, DJANGOU garantit la continuité de votre travail. Vos données récentes sont stockées localement.</p>''',
    '''<span>Hors-ligne</span>''': '''<span data-i18n="idx.off.badge1">Hors-ligne</span>''',
    '''<span>Reconnecté</span>''': '''<span data-i18n="idx.off.badge2">Reconnecté</span>''',
    '''<h4>1. Vous travaillez</h4>''': '''<h4 data-i18n="idx.off.step1">1. Vous travaillez</h4>''',
    '''<p style="font-size: 0.875rem; color: var(--color-text-muted); margin-top: 0.5rem;">Vous saisissez les notes normalement.</p>''': '''<p style="font-size: 0.875rem; color: var(--color-text-muted); margin-top: 0.5rem;" data-i18n="idx.off.step1_p">Vous saisissez les notes normalement.</p>''',
    '''<h4>2. Coupure réseau</h4>''': '''<h4 data-i18n="idx.off.step2">2. Coupure réseau</h4>''',
    '''<p style="font-size: 0.875rem; color: var(--color-text-muted); margin-top: 0.5rem;">L'application continue de fonctionner.</p>''': '''<p style="font-size: 0.875rem; color: var(--color-text-muted); margin-top: 0.5rem;" data-i18n="idx.off.step2_p">L'application continue de fonctionner.</p>''',
    '''<h4>3. Synchronisation</h4>''': '''<h4 data-i18n="idx.off.step3">3. Synchronisation</h4>''',
    '''<p style="font-size: 0.875rem; color: var(--color-text-muted); margin-top: 0.5rem;">Retour en ligne : envoi automatique au serveur.</p>''': '''<p style="font-size: 0.875rem; color: var(--color-text-muted); margin-top: 0.5rem;" data-i18n="idx.off.step3_p">Retour en ligne : envoi automatique au serveur.</p>'''
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html part 1 modified")

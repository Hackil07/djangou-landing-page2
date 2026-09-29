import os

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    # Qui section
    '''<h2>Une plateforme, deux usages complémentaires.</h2>''': '''<h2 data-i18n="idx.qui.h2">Une plateforme, deux usages complémentaires.</h2>''',
    '''<h3>Pour les enseignants</h3>''': '''<h3 data-i18n="idx.qui.ens.h3">Pour les enseignants</h3>''',
    '''<p style="color: var(--color-text-muted); margin-bottom: 1.5rem;">Fini les calculs manuels interminables et la double saisie papier-ordinateur.</p>''': '''<p style="color: var(--color-text-muted); margin-bottom: 1.5rem;" data-i18n="idx.qui.ens.p">Fini les calculs manuels interminables et la double saisie papier-ordinateur.</p>''',
    '''Moins de saisie grâce à la voix''': '''<span data-i18n="idx.qui.ens.l1">Moins de saisie grâce à la voix</span>''',
    '''Calcul automatique des moyennes''': '''<span data-i18n="idx.qui.ens.l2">Calcul automatique des moyennes</span>''',
    '''Travail possible depuis le téléphone''': '''<span data-i18n="idx.qui.ens.l3">Travail possible depuis le téléphone</span>''',
    
    '''<h3>Pour l'administration</h3>''': '''<h3 data-i18n="idx.qui.adm.h3">Pour l'administration</h3>''',
    '''<p style="color: var(--color-text-muted); margin-bottom: 1.5rem;">Centralisez les données de l'établissement et générez les documents officiels instantanément.</p>''': '''<p style="color: var(--color-text-muted); margin-bottom: 1.5rem;" data-i18n="idx.qui.adm.p">Centralisez les données de l'établissement et générez les documents officiels instantanément.</p>''',
    '''Vue globale sur les classes''': '''<span data-i18n="idx.qui.adm.l1">Vue globale sur les classes</span>''',
    '''Génération de bulletins PDF''': '''<span data-i18n="idx.qui.adm.l2">Génération de bulletins PDF</span>''',
    '''Export de Procès-Verbaux Excel''': '''<span data-i18n="idx.qui.adm.l3">Export de Procès-Verbaux Excel</span>''',

    # Security Section
    '''<span class="eyebrow">Sécurité & Confiance</span>''': '''<span class="eyebrow" data-i18n="idx.sec.eyebrow">Sécurité & Confiance</span>''',
    '''<h2>Une architecture pensée pour la protection de vos données scolaires.</h2>''': '''<h2 data-i18n="idx.sec.h2">Une architecture pensée pour la protection de vos données scolaires.</h2>''',
    '''<h3>Infrastructure Cloudflare</h3>''': '''<h3 data-i18n="idx.sec.1.h3">Infrastructure Cloudflare</h3>''',
    '''<p style="color: var(--color-text-muted); font-size: 0.9375rem;">Protection active du réseau contre les attaques courantes et surveillance continue.</p>''': '''<p style="color: var(--color-text-muted); font-size: 0.9375rem;" data-i18n="idx.sec.1.p">Protection active du réseau contre les attaques courantes et surveillance continue.</p>''',
    '''<h3>Authentification Moderne</h3>''': '''<h3 data-i18n="idx.sec.2.h3">Authentification Moderne</h3>''',
    '''<p style="color: var(--color-text-muted); font-size: 0.9375rem;">Intégration de technologies sécurisées telles que les Passkeys pour protéger les comptes.</p>''': '''<p style="color: var(--color-text-muted); font-size: 0.9375rem;" data-i18n="idx.sec.2.p">Intégration de technologies sécurisées telles que les Passkeys pour protéger les comptes.</p>''',
    '''<h3>Synchronisation Sécurisée</h3>''': '''<h3 data-i18n="idx.sec.3.h3">Synchronisation Sécurisée</h3>''',
    '''<p style="color: var(--color-text-muted); font-size: 0.9375rem;">Transfert maîtrisé des données de l'application hors-ligne vers nos serveurs centraux.</p>''': '''<p style="color: var(--color-text-muted); font-size: 0.9375rem;" data-i18n="idx.sec.3.p">Transfert maîtrisé des données de l'application hors-ligne vers nos serveurs centraux.</p>''',

    # Stats Section
    '''<div class="stat-label">Enseignants actifs</div>''': '''<div class="stat-label" data-i18n="idx.stat.1">Enseignants actifs</div>''',
    '''<div class="stat-label">Établissements partenaires</div>''': '''<div class="stat-label" data-i18n="idx.stat.2">Établissements partenaires</div>''',
    '''<div class="stat-label">Taux de satisfaction</div>''': '''<div class="stat-label" data-i18n="idx.stat.3">Taux de satisfaction</div>''',
    '''<div class="stat-label">Temps gagné sur la saisie</div>''': '''<div class="stat-label" data-i18n="idx.stat.4">Temps gagné sur la saisie</div>''',

    # Compare Section
    '''<span class="eyebrow">Transformation</span>''': '''<span class="eyebrow" data-i18n="idx.comp.eyebrow">Transformation</span>''',
    '''<h2>Avant vs Après DJANGOU</h2>''': '''<h2 data-i18n="idx.comp.h2">Avant vs Après DJANGOU</h2>''',
    '''<p>Voyez concrètement ce que DJANGOU change dans votre quotidien d'enseignant.</p>''': '''<p data-i18n="idx.comp.p">Voyez concrètement ce que DJANGOU change dans votre quotidien d'enseignant.</p>''',
    '''Sans DJANGOU''': '''<span data-i18n="idx.comp.sans">Sans DJANGOU</span>''',
    '''<li>Saisie manuelle note par note sur papier</li>''': '''<li data-i18n="idx.comp.sans.1">Saisie manuelle note par note sur papier</li>''',
    '''<li>Calcul des moyennes à la main ou sous Excel</li>''': '''<li data-i18n="idx.comp.sans.2">Calcul des moyennes à la main ou sous Excel</li>''',
    '''<li>Bulletins créés un par un en heures</li>''': '''<li data-i18n="idx.comp.sans.3">Bulletins créés un par un en heures</li>''',
    '''<li>Perte de travail si la connexion coupe</li>''': '''<li data-i18n="idx.comp.sans.4">Perte de travail si la connexion coupe</li>''',
    '''<li>Documents éparpillés sur plusieurs fichiers</li>''': '''<li data-i18n="idx.comp.sans.5">Documents éparpillés sur plusieurs fichiers</li>''',
    '''<li>Risque d'erreurs de calcul fréquent</li>''': '''<li data-i18n="idx.comp.sans.6">Risque d'erreurs de calcul fréquent</li>''',
    
    '''Avec DJANGOU''': '''<span data-i18n="idx.comp.avec">Avec DJANGOU</span>''',
    '''<li>Notes saisies à la voix en quelques secondes</li>''': '''<li data-i18n="idx.comp.avec.1">Notes saisies à la voix en quelques secondes</li>''',
    '''<li>Calculs automatiques et instantanés</li>''': '''<li data-i18n="idx.comp.avec.2">Calculs automatiques et instantanés</li>''',
    '''<li>Bulletins PDF générés en un clic</li>''': '''<li data-i18n="idx.comp.avec.3">Bulletins PDF générés en un clic</li>''',
    '''<li>Travail continu même hors connexion</li>''': '''<li data-i18n="idx.comp.avec.4">Travail continu même hors connexion</li>''',
    '''<li>Tout centralisé sur une seule plateforme</li>''': '''<li data-i18n="idx.comp.avec.5">Tout centralisé sur une seule plateforme</li>''',
    '''<li>Aucune erreur de calcul possible</li>''': '''<li data-i18n="idx.comp.avec.6">Aucune erreur de calcul possible</li>''',

    # FAQ Section
    '''<h2>Questions fréquentes</h2>''': '''<h2 data-i18n="idx.faq.h2">Questions fréquentes</h2>''',
    '''<p>Tout ce que vous devez savoir pour bien comprendre le fonctionnement de DJANGOU.</p>''': '''<p data-i18n="idx.faq.desc">Tout ce que vous devez savoir pour bien comprendre le fonctionnement de DJANGOU.</p>''',
    '''Qu'est-ce que DJANGOU ?''': '''<span data-i18n="idx.faq.1.q">Qu'est-ce que DJANGOU ?</span>''',
    '''<p>DJANGOU est une plateforme technologique dédiée au monde éducatif (EdTech). Elle est conçue pour aider les enseignants, directeurs et personnels administratifs à gérer plus rapidement et plus efficacement les élèves, les notes, les évaluations et la génération de bulletins.</p>''': '''<p data-i18n="idx.faq.1.a">DJANGOU est une plateforme technologique dédiée au monde éducatif (EdTech). Elle est conçue pour aider les enseignants, directeurs et personnels administratifs à gérer plus rapidement et plus efficacement les élèves, les notes, les évaluations et la génération de bulletins.</p>''',
    '''DJANGOU fonctionne-t-il sans Internet ?''': '''<span data-i18n="idx.faq.2.q">DJANGOU fonctionne-t-il sans Internet ?</span>''',
    '''<p>Oui. DJANGOU repose sur une architecture "Offline-First". Cela signifie que l'application est pensée pour continuer à fonctionner de manière transparente lors de coupures réseau. Les données saisies sont stockées localement sur votre appareil puis synchronisées en arrière-plan lorsque la connexion revient.</p>''': '''<p data-i18n="idx.faq.2.a">Oui. DJANGOU repose sur une architecture "Offline-First". Cela signifie que l'application est pensée pour continuer à fonctionner de manière transparente lors de coupures réseau. Les données saisies sont stockées localement sur votre appareil puis synchronisées en arrière-plan lorsque la connexion revient.</p>''',
    '''Comment fonctionne la saisie vocale ?''': '''<span data-i18n="idx.faq.3.q">Comment fonctionne la saisie vocale ?</span>''',
    '''<p>L'application utilise l'Intelligence Artificielle pour analyser votre voix. En prononçant simplement "Martin, 15 sur 20", le système identifie l'élève et la note correspondante, puis remplit le tableau automatiquement, réduisant ainsi la saisie manuelle.</p>''': '''<p data-i18n="idx.faq.3.a">L'application utilise l'Intelligence Artificielle pour analyser votre voix. En prononçant simplement "Martin, 15 sur 20", le système identifie l'élève et la note correspondante, puis remplit le tableau automatiquement, réduisant ainsi la saisie manuelle.</p>''',
    '''Comment fonctionne le scan par IA ?''': '''<span data-i18n="idx.faq.4.q">Comment fonctionne le scan par IA ?</span>''',
    '''<p>En prenant en photo des documents ou copies compatibles, notre technologie d'OCR (Reconnaissance Optique de Caractères) assistée par IA extrait les textes et les chiffres pertinents pour les transformer en données numériques exploitables par la plateforme.</p>''': '''<p data-i18n="idx.faq.4.a">En prenant en photo des documents ou copies compatibles, notre technologie d'OCR (Reconnaissance Optique de Caractères) assistée par IA extrait les textes et les chiffres pertinents pour les transformer en données numériques exploitables par la plateforme.</p>''',
    '''DJANGOU peut-il générer des bulletins ?''': '''<span data-i18n="idx.faq.5.q">DJANGOU peut-il générer des bulletins ?</span>''',
    '''<p>Oui. Une fois les notes et barèmes enregistrés, le personnel autorisé peut générer automatiquement des bulletins scolaires au format PDF, prêts à être imprimés ou envoyés, ainsi que des procès-verbaux globaux au format Excel.</p>''': '''<p data-i18n="idx.faq.5.a">Oui. Une fois les notes et barèmes enregistrés, le personnel autorisé peut générer automatiquement des bulletins scolaires au format PDF, prêts à être imprimés ou envoyés, ainsi que des procès-verbaux globaux au format Excel.</p>''',
    '''Peut-on utiliser DJANGOU sur téléphone ?''': '''<span data-i18n="idx.faq.6.q">Peut-on utiliser DJANGOU sur téléphone ?</span>''',
    '''<p>Absolument. En tant que PWA (Progressive Web App), DJANGOU est optimisée pour s'adapter parfaitement aux écrans tactiles des smartphones, même ceux d'entrée de gamme, offrant une expérience fluide sans nécessiter de téléchargement lourd.</p>''': '''<p data-i18n="idx.faq.6.a">Absolument. En tant que PWA (Progressive Web App), DJANGOU est optimisée pour s'adapter parfaitement aux écrans tactiles des smartphones, même ceux d'entrée de gamme, offrant une expérience fluide sans nécessiter de téléchargement lourd.</p>''',
    '''DJANGOU est-il adapté aux établissements scolaires ?''': '''<span data-i18n="idx.faq.7.q">DJANGOU est-il adapté aux établissements scolaires ?</span>''',
    '''<p>Oui, DJANGOU est pensé autant pour les enseignants individuels que pour l'administration globale d'un établissement. Les directeurs bénéficient d'outils de centralisation et de suivi des données scolaires.</p>''': '''<p data-i18n="idx.faq.7.a">Oui, DJANGOU est pensé autant pour les enseignants individuels que pour l'administration globale d'un établissement. Les directeurs bénéficient d'outils de centralisation et de suivi des données scolaires.</p>''',
    '''Comment commencer avec DJANGOU ?''': '''<span data-i18n="idx.faq.8.q">Comment commencer avec DJANGOU ?</span>''',
    '''<p>Cliquez simplement sur l'un des boutons "Accéder à DJANGOU" sur cette page. Vous serez redirigé vers l'application principale où vous pourrez créer votre compte et configurer vos classes.</p>''': '''<p data-i18n="idx.faq.8.a">Cliquez simplement sur l'un des boutons "Accéder à DJANGOU" sur cette page. Vous serez redirigé vers l'application principale où vous pourrez créer votre compte et configurer vos classes.</p>'''
}

for k, v in replacements.items():
    content = content.replace(k, v)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("index.html part 2 modified")

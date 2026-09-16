import re

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

css_to_add = """
        /* PRICING SECTION */
        .pricing-section {
            padding: 4rem 0;
            background: var(--color-bg-main);
        }
        .pricing-header {
            text-align: center;
            margin-bottom: 3rem;
        }
        .pricing-header h2 {
            font-size: 2.5rem;
            color: var(--color-primary-dark);
            margin-bottom: 1rem;
        }
        .pricing-header p {
            color: var(--color-text-muted);
            max-width: 600px;
            margin: 0 auto 1.5rem auto;
            font-size: 1.1rem;
        }
        .pricing-hook {
            display: block;
            color: var(--color-primary);
            font-size: 1.25rem;
            font-weight: 600;
            margin-top: 0.5rem;
            font-style: italic;
        }
        .billing-toggle {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 1rem;
            margin-bottom: 3rem;
        }
        .toggle-switch {
            position: relative;
            display: inline-block;
            width: 60px;
            height: 34px;
        }
        .toggle-switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }
        .toggle-slider {
            position: absolute;
            cursor: pointer;
            top: 0; left: 0; right: 0; bottom: 0;
            background-color: var(--color-border);
            transition: .4s;
            border-radius: 34px;
        }
        .toggle-slider:before {
            position: absolute;
            content: "";
            height: 26px;
            width: 26px;
            left: 4px;
            bottom: 4px;
            background-color: white;
            transition: .4s;
            border-radius: 50%;
        }
        input:checked + .toggle-slider {
            background-color: var(--color-primary);
        }
        input:checked + .toggle-slider:before {
            transform: translateX(26px);
        }
        .toggle-label {
            font-weight: 600;
            color: var(--color-text-main);
            cursor: pointer;
            transition: color 0.3s;
        }
        .toggle-label.active {
            color: var(--color-primary);
        }
        .save-badge {
            background: rgba(16, 185, 129, 0.1);
            color: #10b981;
            padding: 0.25rem 0.5rem;
            border-radius: 12px;
            font-size: 0.75rem;
            font-weight: bold;
            margin-left: 0.5rem;
        }
        
        .pricing-cards {
            display: flex;
            gap: 2rem;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 3rem;
        }
        .pricing-card {
            background: var(--color-bg-card);
            border-radius: var(--radius-lg);
            border: 1px solid var(--color-border);
            padding: 2.5rem 2rem;
            width: 100%;
            max-width: 380px;
            box-shadow: var(--shadow-sm);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            position: relative;
            display: flex;
            flex-direction: column;
        }
        .pricing-card:hover {
            transform: translateY(-5px);
            box-shadow: var(--shadow-md);
        }
        .pricing-card.start {
            border-top: 4px solid #10b981;
        }
        .pricing-card.premium {
            border: 2px solid var(--color-primary);
            box-shadow: 0 0 20px rgba(109, 40, 217, 0.1);
            transform: scale(1.02);
        }
        .pricing-card.premium:hover {
            transform: scale(1.02) translateY(-5px);
            box-shadow: 0 0 25px rgba(109, 40, 217, 0.2);
        }
        .premium-badge {
            position: absolute;
            top: -15px;
            right: 20px;
            background: var(--color-primary);
            color: white;
            padding: 0.25rem 1rem;
            border-radius: 20px;
            font-size: 0.875rem;
            font-weight: bold;
            box-shadow: 0 4px 6px rgba(109, 40, 217, 0.3);
            display: flex;
            align-items: center;
            gap: 0.25rem;
        }
        .plan-name {
            font-size: 1.75rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .plan-name.start { color: #10b981; }
        .plan-name.premium { color: var(--color-primary); }
        .plan-desc {
            color: var(--color-text-muted);
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
            min-height: 40px;
        }
        .plan-price-wrap {
            display: flex;
            align-items: baseline;
            gap: 0.5rem;
            margin-bottom: 0.25rem;
            flex-wrap: wrap;
        }
        .plan-price {
            font-size: 2.25rem;
            font-weight: 800;
            color: var(--color-text-main);
        }
        .plan-currency {
            font-size: 1rem;
            color: var(--color-text-muted);
            font-weight: 600;
        }
        .plan-period {
            font-size: 1rem;
            color: var(--color-text-muted);
        }
        .plan-promo-note {
            font-size: 0.85rem;
            color: var(--color-primary);
            background: rgba(109, 40, 217, 0.1);
            padding: 4px 8px;
            border-radius: 4px;
            display: inline-block;
            margin-bottom: 1.5rem;
            font-weight: 600;
        }
        .plan-price-original {
            text-decoration: line-through;
            color: var(--color-text-muted);
            font-size: 1.1rem;
            margin-right: 0.25rem;
        }
        
        .plan-features {
            list-style: none;
            padding: 0;
            margin: 0 0 2rem 0;
            flex-grow: 1;
        }
        .plan-features li {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            margin-bottom: 1rem;
            font-size: 0.9rem;
            color: var(--color-text-main);
        }
        .plan-features li svg {
            color: #10b981;
            flex-shrink: 0;
            width: 18px;
            height: 18px;
        }
        .plan-footer-note {
            font-size: 0.85rem;
            color: var(--color-text-muted);
            text-align: center;
            margin-bottom: 1.5rem;
            padding: 0.75rem;
            background: var(--color-bg-alt);
            border-radius: var(--radius-md);
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .btn-plan {
            width: 100%;
            padding: 1rem;
            border-radius: var(--radius-md);
            font-weight: 600;
            text-align: center;
            cursor: pointer;
            transition: all 0.2s;
            border: none;
            font-size: 1rem;
        }
        .btn-plan.start {
            background: rgba(16, 185, 129, 0.1);
            color: #10b981;
            border: 1px solid #10b981;
        }
        .btn-plan.start:hover {
            background: #10b981;
            color: white;
        }
        .btn-plan.premium {
            background: var(--color-primary);
            color: white;
            box-shadow: 0 4px 12px rgba(109, 40, 217, 0.3);
        }
        .btn-plan.premium:hover {
            background: var(--color-primary-dark);
            transform: translateY(-2px);
        }
        
        .premium-advantages {
            background: var(--color-bg-card);
            border-radius: var(--radius-lg);
            border: 1px solid var(--color-border);
            padding: 2.5rem;
            margin: 0 auto 3rem auto;
            max-width: 800px;
            box-shadow: var(--shadow-sm);
        }
        .premium-advantages h3 {
            color: var(--color-primary-dark);
            font-size: 1.5rem;
            margin-bottom: 1.5rem;
            text-align: center;
        }
        .adv-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 1rem;
        }
        .adv-item {
            display: flex;
            align-items: flex-start;
            gap: 0.5rem;
            font-size: 0.95rem;
            color: var(--color-text-main);
        }
        .adv-item svg {
            color: #10b981;
            flex-shrink: 0;
            margin-top: 2px;
            width: 18px;
            height: 18px;
        }
        
        .packs-section {
            background: var(--color-bg-alt);
            padding: 3rem 2rem;
            border-radius: var(--radius-lg);
            max-width: 1000px;
            margin: 0 auto;
            position: relative;
        }
        .packs-header {
            text-align: center;
            margin-bottom: 2.5rem;
        }
        .packs-header h3 {
            font-size: 1.75rem;
            margin-bottom: 0.5rem;
        }
        .packs-header p {
            color: var(--color-text-muted);
        }
        .packs-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: var(--color-primary);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: bold;
            margin-top: 1rem;
        }
        .packs-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1.5rem;
        }
        .pack-card {
            background: var(--color-bg-card);
            border: 1px solid var(--color-border);
            border-radius: var(--radius-md);
            padding: 1.5rem;
            text-align: center;
            transition: transform 0.2s;
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        .pack-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-sm);
        }
        .pack-qty {
            font-size: 1.25rem;
            font-weight: bold;
            color: var(--color-text-main);
            margin-bottom: 0.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        }
        .pack-qty svg {
            color: var(--color-primary);
            width: 20px;
            height: 20px;
        }
        .pack-price-std {
            font-size: 0.95rem;
            color: var(--color-text-muted);
        }
        .pack-price-prem {
            font-size: 1.1rem;
            font-weight: bold;
            color: var(--color-primary);
            background: rgba(109, 40, 217, 0.05);
            padding: 0.5rem;
            border-radius: 4px;
            margin-top: 0.5rem;
        }
        
        /* MODAL PROMO */
        .promo-modal-overlay {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(4px);
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
        }
        .promo-modal-overlay.active {
            opacity: 1;
            visibility: visible;
        }
        .promo-modal {
            background: var(--color-bg-main);
            border-radius: var(--radius-lg);
            padding: 2.5rem;
            max-width: 450px;
            width: 90%;
            position: relative;
            transform: translateY(20px);
            transition: all 0.3s ease;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
            text-align: center;
            border: 2px solid var(--color-primary);
        }
        .promo-modal-overlay.active .promo-modal {
            transform: translateY(0);
        }
        .promo-close {
            position: absolute;
            top: 15px;
            right: 15px;
            background: transparent;
            border: none;
            color: var(--color-text-muted);
            cursor: pointer;
            padding: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .promo-close:hover {
            color: var(--color-text-main);
        }
        .promo-gift {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        .promo-title {
            color: var(--color-primary-dark);
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        .promo-desc {
            color: var(--color-text-muted);
            margin-bottom: 1.5rem;
            font-size: 1.05rem;
        }
        .promo-prices {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 2rem;
            background: var(--color-bg-alt);
            padding: 1.5rem 1rem;
            border-radius: var(--radius-md);
        }
        .promo-price-item {
            text-align: center;
            flex: 1;
        }
        .promo-price-item strong {
            display: block;
            color: var(--color-text-main);
            margin-bottom: 0.5rem;
            font-size: 1.1rem;
        }
        .promo-price-item .old-price {
            text-decoration: line-through;
            color: var(--color-text-muted);
            font-size: 0.95rem;
            display: block;
        }
        .promo-price-item .new-price {
            color: var(--color-primary);
            font-size: 1.35rem;
            font-weight: bold;
            display: block;
        }
        .promo-actions {
            display: flex;
            gap: 1rem;
            justify-content: center;
        }
        .promo-actions .btn {
            flex: 1;
        }
        
        @media (max-width: 768px) {
            .pricing-card.premium {
                transform: none;
            }
            .pricing-card.premium:hover {
                transform: translateY(-5px);
            }
            .promo-prices {
                flex-direction: column;
                gap: 1rem;
            }
            .promo-actions {
                flex-direction: column;
            }
        }
"""

content = content.replace("    </style>", css_to_add + "\n    </style>")

html_to_add = """
        <!-- TARIFICATION -->
        <section id="tarifs" class="pricing-section">
            <div class="container">
                <div class="pricing-header reveal">
                    <h2>Nos abonnements</h2>
                    <p>Des solutions adaptées à vos besoins, pour une gestion simple, efficace et intelligente de vos épreuves.</p>
                    <span class="pricing-hook">Plus de possibilités, plus de réussite !</span>
                </div>

                <div class="billing-toggle reveal">
                    <span class="toggle-label active" id="label-mensuel">Mensuel</span>
                    <label class="toggle-switch">
                        <input type="checkbox" id="billing-switch">
                        <span class="toggle-slider"></span>
                    </label>
                    <span class="toggle-label" id="label-trimestre">3 mois <span class="save-badge">Économisez</span></span>
                </div>

                <div class="pricing-cards reveal">
                    <!-- START -->
                    <div class="pricing-card start">
                        <div class="plan-name start">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                            Start
                        </div>
                        <p class="plan-desc">Idéal pour bien démarrer</p>
                        
                        <!-- Prix Mensuel -->
                        <div class="price-mensuel">
                            <div class="plan-price-wrap">
                                <span class="plan-price-original">2 000 FCFA</span>
                                <span class="plan-price">1 500</span>
                                <span class="plan-currency">FCFA</span>
                                <span class="plan-period">/ mois</span>
                            </div>
                            <span class="plan-promo-note">Offre de lancement – 3 premiers mois</span>
                        </div>

                        <!-- Prix 3 Mois (Caché par défaut) -->
                        <div class="price-trimestre" style="display: none;">
                            <div class="plan-price-wrap" style="margin-bottom: 1.5rem;">
                                <span class="plan-price">4 000</span>
                                <span class="plan-currency">FCFA</span>
                                <span class="plan-period">/ 3 mois</span>
                            </div>
                        </div>

                        <ul class="plan-features">
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> <span class="feat-copies">150 copies IA / mois</span></li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 2 salles / classes</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 80 élèves par salle</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 5 épreuves actives</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> <span class="feat-trans">1 h de transcription vocale / mois</span></li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 2 backups / restaurations</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> <span class="feat-hist">Historique : 3 mois</span></li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Statistiques : Essentielles</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Export : PDF</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Priorité de traitement : Standard</li>
                        </ul>
                        
                        <div class="plan-footer-note" id="start-note">
                            Le Start vous offre l’essentiel pour évaluer efficacement vos élèves.
                        </div>
                        
                        <button class="btn-plan start">Choisir Start</button>
                    </div>

                    <!-- PREMIUM -->
                    <div class="pricing-card premium">
                        <div class="premium-badge">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                            Populaire
                        </div>
                        <div class="plan-name premium">
                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12h4l2-9 4 18 4-13 4 9h4"></path></svg>
                            Premium
                        </div>
                        <p class="plan-desc">Plus de puissance, plus de liberté</p>
                        
                        <!-- Prix Mensuel -->
                        <div class="price-mensuel">
                            <div class="plan-price-wrap">
                                <span class="plan-price-original">3 500 FCFA</span>
                                <span class="plan-price">3 000</span>
                                <span class="plan-currency">FCFA</span>
                                <span class="plan-period">/ mois</span>
                            </div>
                            <span class="plan-promo-note">Offre de lancement – 3 premiers mois</span>
                        </div>

                        <!-- Prix 3 Mois (Caché par défaut) -->
                        <div class="price-trimestre" style="display: none;">
                            <div class="plan-price-wrap" style="margin-bottom: 1.5rem;">
                                <span class="plan-price">8 000</span>
                                <span class="plan-currency">FCFA</span>
                                <span class="plan-period">/ 3 mois</span>
                            </div>
                        </div>

                        <ul class="plan-features">
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> <span class="feat-copies">250 copies IA / mois</span></li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 5 salles / classes</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 80 élèves par salle</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 15 épreuves actives</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> <span class="feat-trans">2 h de transcription vocale / mois</span></li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> 10 backups / restaurations</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> <span class="feat-hist">Historique : 12 mois</span></li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Statistiques : Avancées</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Export : PDF + Excel/CSV</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> Priorité de traitement : Prioritaire</li>
                            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg> <strong>-30 % sur les packs de copies</strong></li>
                        </ul>
                        
                        <div class="plan-footer-note" id="premium-note">
                            Le Premium, c'est plus de capacités et 30 % de réduction sur les packs de copies.
                        </div>
                        
                        <button class="btn-plan premium">Choisir Premium</button>
                    </div>
                </div>

                <!-- POURQUOI PREMIUM -->
                <div class="premium-advantages reveal">
                    <h3>Pourquoi choisir le Premium ?</h3>
                    <div class="adv-grid">
                        <div class="adv-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <span>+100 copies supplémentaires</span>
                        </div>
                        <div class="adv-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <span>+3 salles (soit jusqu'à 240 élèves en plus)</span>
                        </div>
                        <div class="adv-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <span>+1 h de transcription</span>
                        </div>
                        <div class="adv-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <span>Beaucoup plus de sauvegardes et restaurations</span>
                        </div>
                        <div class="adv-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <span>Historique plus long</span>
                        </div>
                        <div class="adv-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <span>Statistiques avancées & Export Excel</span>
                        </div>
                        <div class="adv-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <span>Priorité de traitement</span>
                        </div>
                        <div class="adv-item">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                            <strong>Et surtout : -30 % sur les packs de copies !</strong>
                        </div>
                    </div>
                </div>

                <!-- PACKS DE COPIES -->
                <div class="packs-section reveal">
                    <div class="packs-header">
                        <h3>Packs de copies IA</h3>
                        <p>Besoin de plus de copies ? Achetez des packs selon vos besoins.</p>
                        <div class="packs-badge">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                            Le Premium bénéficie de 30 % de réduction sur tous les packs !
                        </div>
                    </div>
                    
                    <div class="packs-grid">
                        <div class="pack-card">
                            <div class="pack-qty">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                                10 copies
                            </div>
                            <div class="pack-price-std">Standard : 500 FCFA</div>
                            <div class="pack-price-prem">Premium : 350 FCFA</div>
                        </div>
                        <div class="pack-card">
                            <div class="pack-qty">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                                20 copies
                            </div>
                            <div class="pack-price-std">Standard : 900 FCFA</div>
                            <div class="pack-price-prem">Premium : 630 FCFA</div>
                        </div>
                        <div class="pack-card">
                            <div class="pack-qty">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                                30 copies
                            </div>
                            <div class="pack-price-std">Standard : 1 200 FCFA</div>
                            <div class="pack-price-prem">Premium : 840 FCFA</div>
                        </div>
                        <div class="pack-card">
                            <div class="pack-qty">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                                50 copies
                            </div>
                            <div class="pack-price-std">Standard : 1 800 FCFA</div>
                            <div class="pack-price-prem">Premium : 1 260 FCFA</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- MODAL OFFRE DE LANCEMENT -->
        <div class="promo-modal-overlay" id="promo-modal" role="dialog" aria-modal="true" aria-labelledby="promo-title">
            <div class="promo-modal">
                <button class="promo-close" id="promo-close" aria-label="Fermer">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                </button>
                <div class="promo-gift">🎁</div>
                <h2 class="promo-title" id="promo-title">OFFRE DE LANCEMENT</h2>
                <p class="promo-desc">Profitez de nos tarifs de lancement ! Pendant vos 3 premiers mois, économisez 500 FCFA sur les abonnements mensuels.</p>
                
                <div class="promo-prices">
                    <div class="promo-price-item">
                        <strong>Start</strong>
                        <span class="old-price">2 000 FCFA</span>
                        <span class="new-price">1 500 FCFA/mois</span>
                    </div>
                    <div class="promo-price-item">
                        <strong>Premium</strong>
                        <span class="old-price">3 500 FCFA</span>
                        <span class="new-price">3 000 FCFA/mois</span>
                    </div>
                </div>
                
                <div class="promo-actions">
                    <button class="btn btn-primary" id="promo-cta">Voir les abonnements</button>
                    <button class="btn btn-secondary" id="promo-close-btn">Fermer</button>
                </div>
            </div>
        </div>
"""

content = content.replace('        <section id="faq">', html_to_add + '\n        <section id="faq">')


js_to_add = """
            // LOGIQUE TARIFICATION & MODAL PROMO
            const billingSwitch = document.getElementById('billing-switch');
            const labelMensuel = document.getElementById('label-mensuel');
            const labelTrimestre = document.getElementById('label-trimestre');
            const pricesMensuel = document.querySelectorAll('.price-mensuel');
            const pricesTrimestre = document.querySelectorAll('.price-trimestre');
            const startNote = document.getElementById('start-note');
            const premiumNote = document.getElementById('premium-note');
            const featCopies = document.querySelectorAll('.feat-copies');
            const featTrans = document.querySelectorAll('.feat-trans');

            if (billingSwitch) {
                billingSwitch.addEventListener('change', function() {
                    const isTrimestre = this.checked;
                    
                    if (isTrimestre) {
                        labelMensuel.classList.remove('active');
                        labelTrimestre.classList.add('active');
                        pricesMensuel.forEach(p => p.style.display = 'none');
                        pricesTrimestre.forEach(p => p.style.display = 'block');
                        
                        startNote.innerHTML = 'Économisez 500 FCFA par rapport au paiement mensuel sur 3 mois.';
                        premiumNote.innerHTML = 'Économisez 1 000 FCFA par rapport au paiement mensuel sur 3 mois.';
                        
                        featCopies[0].innerHTML = '450 copies IA / 3 mois';
                        featCopies[1].innerHTML = '750 copies IA / 3 mois';
                        featTrans[0].innerHTML = '1 h de transcription vocale / mois';
                        featTrans[1].innerHTML = '2 h de transcription vocale / mois';
                    } else {
                        labelTrimestre.classList.remove('active');
                        labelMensuel.classList.add('active');
                        pricesTrimestre.forEach(p => p.style.display = 'none');
                        pricesMensuel.forEach(p => p.style.display = 'block');
                        
                        startNote.innerHTML = 'Le Start vous offre l’essentiel pour évaluer efficacement vos élèves.';
                        premiumNote.innerHTML = 'Le Premium, c\\'est plus de capacités et 30 % de réduction sur les packs de copies.';
                        
                        featCopies[0].innerHTML = '150 copies IA / mois';
                        featCopies[1].innerHTML = '250 copies IA / mois';
                        featTrans[0].innerHTML = '1 h de transcription vocale / mois';
                        featTrans[1].innerHTML = '2 h de transcription vocale / mois';
                    }
                });
            }

            // GESTION DU MODAL AVEC INTERSECTION OBSERVER
            const promoModal = document.getElementById('promo-modal');
            const pricingSection = document.getElementById('tarifs');
            const btnClosePromo = document.getElementById('promo-close');
            const btnClosePromoBtn = document.getElementById('promo-close-btn');
            const btnCtaPromo = document.getElementById('promo-cta');
            
            function closePromoModal() {
                promoModal.classList.remove('active');
                document.body.style.overflow = '';
            }

            if (promoModal && pricingSection) {
                const hasSeenModal = sessionStorage.getItem('djangou_promo_seen');
                
                if (!hasSeenModal) {
                    const observer = new IntersectionObserver((entries) => {
                        entries.forEach(entry => {
                            if (entry.isIntersecting) {
                                // Afficher le modal
                                promoModal.classList.add('active');
                                document.body.style.overflow = 'hidden'; // Empêcher le scroll
                                sessionStorage.setItem('djangou_promo_seen', 'true');
                                observer.disconnect(); // Ne déclencher qu'une fois
                            }
                        });
                    }, { threshold: 0.3 }); // Déclenche quand 30% de la section tarifs est visible
                    
                    observer.observe(pricingSection);
                }

                // Fermeture
                btnClosePromo.addEventListener('click', closePromoModal);
                btnClosePromoBtn.addEventListener('click', closePromoModal);
                
                // Clic sur "Voir les abonnements"
                btnCtaPromo.addEventListener('click', () => {
                    closePromoModal();
                    pricingSection.scrollIntoView({ behavior: 'smooth' });
                });

                // Fermeture sur clic en dehors
                promoModal.addEventListener('click', (e) => {
                    if (e.target === promoModal) {
                        closePromoModal();
                    }
                });
                
                // Fermeture avec Echap
                document.addEventListener('keydown', (e) => {
                    if (e.key === 'Escape' && promoModal.classList.contains('active')) {
                        closePromoModal();
                    }
                });
            }
"""

content = content.replace('            // 3D Tilt Effect', js_to_add + '\n            // 3D Tilt Effect')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

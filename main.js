
        document.addEventListener('DOMContentLoaded', function() {
            // Mobile Menu Toggle
            const menuToggle = document.getElementById('mobile-menu-toggle');
            const mainMenu = document.getElementById('main-menu');
            
            if (menuToggle && mainMenu) {
                menuToggle.addEventListener('click', function() {
                    const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
                    menuToggle.setAttribute('aria-expanded', !isExpanded);
                    mainMenu.classList.toggle('is-open');
                });
            }

            // Close mobile menu on link click
            const navLinks = mainMenu.querySelectorAll('a');
            navLinks.forEach(link => {
                link.addEventListener('click', () => {
                    if (window.innerWidth <= 768) {
                        menuToggle.setAttribute('aria-expanded', 'false');
                        mainMenu.classList.remove('is-open');
                    }
                });
            });




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
                        premiumNote.innerHTML = 'Le Premium, c\'est plus de capacités et 30 % de réduction sur les packs de copies.';
                        
                        featCopies[0].innerHTML = '150 copies IA / mois';
                        featCopies[1].innerHTML = '250 copies IA / mois';
                        featTrans[0].innerHTML = '1 h de transcription vocale / mois';
                        featTrans[1].innerHTML = '2 h de transcription vocale / mois';
                    }
                });
            }

            // GESTION DU MODAL AVEC INTERSECTION OBSERVER
            const promoModal = document.getElementById('promo-modal');
            const pricingSection = document.getElementById('abonnements');
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

            // 3D Tilt Effect (Optimisé pour perfs & fallback CSS)
            const tiltCards = document.querySelectorAll('.feature-card');
            
            tiltCards.forEach(card => {
                let rect = card.getBoundingClientRect();
                let isHovered = false;
                
                // Mettre à jour les dimensions en cas de redimensionnement
                window.addEventListener('resize', () => { if(isHovered) rect = card.getBoundingClientRect(); }, {passive: true});
                
                card.addEventListener('mouseenter', () => {
                    isHovered = true;
                    rect = card.getBoundingClientRect();
                    card.style.transition = 'transform 0.1s ease-out, box-shadow 0.1s ease-out';
                }, {passive: true});
                
                card.addEventListener('mousemove', (e) => {
                    if(!isHovered) return;
                    requestAnimationFrame(() => {
                        const x = e.clientX - rect.left;
                        const y = e.clientY - rect.top;
                        
                        const centerX = rect.width / 2;
                        const centerY = rect.height / 2;
                        
                        // Rotation max: ~8 degrés
                        const rotateX = ((y - centerY) / centerY) * -8;
                        const rotateY = ((x - centerX) / centerX) * 8;
                        
                        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
                        card.style.boxShadow = `0 25px 40px -10px rgba(109, 40, 217, 0.25)`;
                    });
                }, {passive: true});
                
                card.addEventListener('mouseleave', () => {
                    isHovered = false;
                    card.style.transition = 'transform 0.5s ease-out, box-shadow 0.5s ease-out';
                    card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
                    card.style.boxShadow = ''; // fallback
                }, {passive: true});
            });

            // ── Typewriter Effect ───────────────────────────────────────────
            const textToType = window.i18n ? window.i18n.t('idx.js.typewriter') : "même sans connexion.";
            const typeWriterEl = document.querySelector('.typewriter-text');
            if (typeWriterEl) {
                let charIndex = 0;
                let isDeleting = false;
                
                function typeWriter() {
                    const currentText = textToType.substring(0, charIndex);
                    // Use a gradient span for the text
                    typeWriterEl.innerHTML = `<span class="text-gradient">${currentText}</span>`;
                    
                    let typingSpeed = 100;
                    if (isDeleting) {
                        typingSpeed /= 2;
                    }
                    
                    if (!isDeleting && charIndex === textToType.length) {
                        typingSpeed = 2000; // Pause at end
                        isDeleting = true;
                    } else if (isDeleting && charIndex === 0) {
                        isDeleting = false;
                        typingSpeed = 500; // Pause before typing again
                    }
                    
                    charIndex += isDeleting ? -1 : 1;
                    setTimeout(typeWriter, typingSpeed);
                }
                setTimeout(typeWriter, 1000); // Initial delay
                window.addEventListener('languageChanged', (e) => {
                    const newText = window.i18n.t('idx.js.typewriter');
                    typeWriterEl.innerHTML = `<span class="text-gradient">${newText}</span>`;
                });
            }

            // ── Animated Counters ───────────────────────────────────────────
            const statNumbers = document.querySelectorAll('.stat-number');
            const countersObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const targetEl = entry.target;
                        const targetValue = parseInt(targetEl.getAttribute('data-target'), 10);
                        const suffix = targetEl.getAttribute('data-suffix') || '';
                        
                        let current = 0;
                        const duration = 2000; // ms
                        const stepTime = Math.max(10, Math.floor(duration / targetValue));
                        const increment = Math.max(1, Math.floor(targetValue / (duration / stepTime)));
                        
                        const timer = setInterval(() => {
                            current += increment;
                            if (current >= targetValue) {
                                targetEl.textContent = targetValue + suffix;
                                clearInterval(timer);
                            } else {
                                targetEl.textContent = current + suffix;
                            }
                        }, stepTime);
                        
                        observer.unobserve(targetEl); // Run only once
                    }
                });
            }, { threshold: 0.5 });
            
            statNumbers.forEach(num => countersObserver.observe(num));

            // ── RGPD Banner ─────────────────────────────────────────────────
            const rgpdBanner = document.getElementById('rgpd-banner');
            const btnAccept = document.getElementById('rgpd-accept');
            const btnDecline = document.getElementById('rgpd-decline');
            
            if (rgpdBanner && !localStorage.getItem('djangou_rgpd')) {
                rgpdBanner.classList.remove('hidden');
                
                const hideBanner = (choice) => {
                    localStorage.setItem('djangou_rgpd', choice);
                    rgpdBanner.classList.add('hidden');
                };
                
                if(btnAccept) btnAccept.addEventListener('click', () => hideBanner('accepted'));
                if(btnDecline) btnDecline.addEventListener('click', () => hideBanner('declined'));
            }

            // Scroll Reveal Observer
            const revealElements = document.querySelectorAll('.reveal');
            
            const revealCallback = function(entries, observer) {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('active');
                        // Optionnel : on peut garder l'animation ou la jouer une seule fois.
                        // observer.unobserve(entry.target);
                    }
                });
            };
            
            const revealOptions = {
                root: null,
                rootMargin: '0px 0px -50px 0px',
                threshold: 0.1
            };
            
            const revealObserver = new IntersectionObserver(revealCallback, revealOptions);
            
            revealElements.forEach(el => revealObserver.observe(el));

            // FAQ Accordion
            const faqButtons = document.querySelectorAll('.faq-question');
            faqButtons.forEach(button => {
                button.addEventListener('click', function() {
                    const isExpanded = this.getAttribute('aria-expanded') === 'true';
                    const answer = this.nextElementSibling;
                    faqButtons.forEach(btn => {
                        if (btn !== this) {
                            btn.setAttribute('aria-expanded', 'false');
                            btn.nextElementSibling.hidden = true;
                        }
                    });
                    this.setAttribute('aria-expanded', !isExpanded);
                    answer.hidden = isExpanded;
                });
            });

            
            // ── SCROLL OPTIMIZATIONS (Progress, Back-to-top, Sticky CTA) ──
            const progressBar = document.getElementById('scroll-progress');
            const backToTopBtn = document.getElementById('back-to-top');
            const stickyCta = document.querySelector('.mobile-sticky-cta');
            const footer = document.querySelector('.site-footer');
            
            let isScrolling = false;
            
            function onScroll() {
                if (!isScrolling) {
                    window.requestAnimationFrame(() => {
                        const scrollTop = window.scrollY || document.documentElement.scrollTop;
                        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
                        
                        // 1. Scroll Progress
                        if (docHeight > 0) {
                            const scrolled = Math.min(1, Math.max(0, scrollTop / docHeight));
                            if (progressBar) {
                                progressBar.style.transform = `scaleX(${scrolled})`;
                            }
                        }
                        
                        // 2. Back to top visibility (visible after 50%)
                        if (scrollTop > docHeight * 0.5) {
                            if (backToTopBtn) {
                                backToTopBtn.classList.add('show');
                                backToTopBtn.removeAttribute('tabindex');
                            }
                        } else {
                            if (backToTopBtn) {
                                backToTopBtn.classList.remove('show');
                                backToTopBtn.setAttribute('tabindex', '-1');
                            }
                        }
                        
                        // 3. Sticky CTA collision with footer
                        if (stickyCta && footer && window.innerWidth <= 768) {
                            const footerRect = footer.getBoundingClientRect();
                            if (footerRect.top < window.innerHeight) {
                                stickyCta.classList.add('hidden');
                            } else {
                                stickyCta.classList.remove('hidden');
                            }
                        }
                        
                        isScrolling = false;
                    });
                    isScrolling = true;
                }
            }
            
            window.addEventListener('scroll', onScroll, { passive: true });
            window.addEventListener('resize', onScroll, { passive: true });
            onScroll(); // initial state

            // ── V2 OPTIMIZATIONS (ROI & Voice Demo) ──
            const roiStudents = document.getElementById('roi-students');
            const roiStudentsVal = document.getElementById('roi-students-val');
            const roiTimeVal = document.getElementById('roi-time-val');
            
            if (roiStudents && roiStudentsVal && roiTimeVal) {
                roiStudents.addEventListener('input', (e) => {
                    const students = parseInt(e.target.value);
                    roiStudentsVal.textContent = students;
                    // 4 minutes par eleve = 4/60 heures
                    const hours = Math.round((students * 4) / 60);
                    roiTimeVal.textContent = hours;
                });
            }
            
            const voiceDemoBtn = document.querySelector('.voice-demo');
            if (voiceDemoBtn) {
                const voiceContent = voiceDemoBtn.querySelector('.voice-demo-content');
                let isPlaying = false;
                
                voiceDemoBtn.addEventListener('click', () => {
                    if (isPlaying) return;
                    isPlaying = true;
                    voiceContent.textContent = '';
                    voiceDemoBtn.style.borderColor = 'var(--color-primary)';
                    voiceDemoBtn.querySelector('.voice-demo-btn').style.transform = 'scale(1.1)';
                    
                    const text = "Martin : 15/20\nSophie : 17/20\nPaul : 12/20";
                    let i = 0;
                    
                    const typeWriter = setInterval(() => {
                        voiceContent.textContent += text.charAt(i);
                        i++;
                        if (i >= text.length) {
                            clearInterval(typeWriter);
                            isPlaying = false;
                            voiceDemoBtn.style.borderColor = 'var(--color-border)';
                            voiceDemoBtn.querySelector('.voice-demo-btn').style.transform = 'scale(1)';
                        }
                    }, 50); // 50ms per char
                });
            }

            
            if (backToTopBtn) {
                backToTopBtn.setAttribute('tabindex', '-1');
                backToTopBtn.addEventListener('click', () => {
                    window.scrollTo({ top: 0, behavior: 'smooth' });
                });
            }

            // ── Contact Form / EmailJS ──────────────────────────────────────
            // Remplacez ces 3 valeurs par vos identifiants EmailJS réels
            const EMAILJS_PUBLIC_KEY  = 'r-COSI9pUMP1bYgpg';
            const EMAILJS_SERVICE_ID  = 'service_wddeffm';
            const EMAILJS_TEMPLATE_ID = 'template_oxanvvo';

            // Initialisation EmailJS
            if (typeof emailjs !== 'undefined') {
                emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });
            }

            const contactForm   = document.getElementById('contact-form');
            const submitBtn     = document.getElementById('contact-submit');
            const formSuccess   = document.getElementById('form-success');
            const formErrGlobal = document.getElementById('form-error-global');

            // Validation inline à la saisie
            function validateField(input) {
                const group = input.closest('.form-group');
                if (!group) return true;
                const errorEl = group.querySelector('.field-error');
                let valid = input.checkValidity();
                group.classList.toggle('has-error', !valid);
                group.classList.toggle('is-valid', valid && input.value.trim() !== '');
                if (errorEl) errorEl.hidden = valid;
                return valid;
            }

            contactForm && contactForm.querySelectorAll('input, textarea').forEach(field => {
                field.addEventListener('blur', () => validateField(field));
                field.addEventListener('input', () => {
                    if (field.closest('.form-group').classList.contains('has-error')) {
                        validateField(field);
                    }
                });
            });

            contactForm && contactForm.addEventListener('submit', async function(e) {
                e.preventDefault();
                let allValid = true;
                this.querySelectorAll('[required]').forEach(f => { if (!validateField(f)) allValid = false; });
                if (!allValid) return;

                // Etat: chargement
                submitBtn.classList.add('is-loading');
                submitBtn.disabled = true;
                formSuccess.hidden   = true;
                formErrGlobal.hidden = true;

                try {
                    if (typeof emailjs === 'undefined') throw new Error('EmailJS non chargé');
                    await emailjs.sendForm(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, this);
                    // Succès
                    formSuccess.hidden = false;
                    this.reset();
                    this.querySelectorAll('.form-group').forEach(g => g.classList.remove('is-valid', 'has-error'));
                    formSuccess.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                } catch (err) {
                    console.error('EmailJS error:', err);
                    formErrGlobal.hidden = false;
                } finally {
                    submitBtn.classList.remove('is-loading');
                    submitBtn.disabled = false;
                }
            });
            // ── Fin Contact Form ────────────────────────────────────────────
        });
    


    (function () {
        'use strict';

        var canvas = document.getElementById('brainCanvas');
        var stage = document.getElementById('brainStage');
        var fallback = document.getElementById('brainFallback');
        if (!canvas || !stage || !canvas.getContext) return;

        var ctx = canvas.getContext('2d');
        if (!ctx) return;

        var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        var isCoarsePointer = window.matchMedia('(pointer: coarse)').matches;

        /* ---- Device tier: fewer points + lower pixel ratio on modest hardware ---- */
        var cores = navigator.hardwareConcurrency || 4;
        var mem = navigator.deviceMemory || 4;
        var tier = 'high';
        if (cores <= 4 || mem <= 4) tier = 'medium';
        if (cores <= 2 || mem <= 2) tier = 'low';
        if (window.innerWidth < 480 && tier === 'high') tier = 'medium';

        var TIERS = {
            high:   { points: 460, maxLinks: 4, linkDist: 0.62, dpr: Math.min(window.devicePixelRatio || 1, 2),   glow: true  },
            medium: { points: 300, maxLinks: 3, linkDist: 0.58, dpr: Math.min(window.devicePixelRatio || 1, 1.5), glow: true  },
            low:    { points: 160, maxLinks: 2, linkDist: 0.55, dpr: 1,                                            glow: false }
        };
        var cfg = TIERS[tier];
        var fps = tier === 'low' ? 30 : 60;
        var frameInterval = 1000 / fps;

        /* ---- Generate a brain-shaped point cloud (runs once) ---- */
        function generateBrain(n) {
            var pts = [];
            var golden = Math.PI * (3 - Math.sqrt(5));
            for (var i = 0; i < n; i++) {
                var yFrac = 1 - (i / (n - 1)) * 2;
                var radiusAtY = Math.sqrt(Math.max(0, 1 - yFrac * yFrac));
                var theta = golden * i;

                var x = Math.cos(theta) * radiusAtY;
                var y = yFrac;
                var z = Math.sin(theta) * radiusAtY;

                var fold = Math.sin(theta * 3.1 + y * 5) * 0.10 +
                           Math.sin(theta * 6.3 - y * 2.4) * 0.05 +
                           Math.sin(y * 9 + theta * 1.7) * 0.045;
                var r = 1 + fold;
                x *= r; y *= r; z *= r;

                var squeeze = Math.exp(-Math.pow(x * 3.4, 2)) * 0.16;
                x += (x >= 0 ? 1 : -1) * squeeze;

                x *= 0.86; y *= 0.70; z *= 0.98;

                if (y < -0.55) {
                    var t = (y + 0.55) / -0.45;
                    x *= (1 - t * 0.6);
                    z *= (1 - t * 0.6);
                }

                pts.push({ x: x, y: y, z: z });
            }
            return pts;
        }

        var basePoints = generateBrain(cfg.points);

        /* ---- Precompute nearest-neighbour links once (cheap: small n, one-time cost) ---- */
        function buildLinks(pts, maxDist, maxPerPoint) {
            var links = [];
            var count = new Array(pts.length).fill(0);
            for (var i = 0; i < pts.length; i++) {
                if (count[i] >= maxPerPoint) continue;
                var candidates = [];
                for (var j = i + 1; j < pts.length; j++) {
                    if (count[j] >= maxPerPoint) continue;
                    var dx = pts[i].x - pts[j].x, dy = pts[i].y - pts[j].y, dz = pts[i].z - pts[j].z;
                    var d = Math.sqrt(dx * dx + dy * dy + dz * dz);
                    if (d < maxDist) candidates.push([j, d]);
                }
                candidates.sort(function (a, b) { return a[1] - b[1]; });
                for (var k = 0; k < candidates.length && count[i] < maxPerPoint; k++) {
                    var j2 = candidates[k][0];
                    if (count[j2] >= maxPerPoint) continue;
                    links.push([i, j2]);
                    count[i]++; count[j2]++;
                }
            }
            return links;
        }
        var links = buildLinks(basePoints, cfg.linkDist, cfg.maxLinks);

        var startPoints = basePoints.map(function () {
            return {
                x: (Math.random() - 0.5) * 5,
                y: (Math.random() - 0.5) * 5,
                z: (Math.random() - 0.5) * 5
            };
        });

        /* ---- render state ---- */
        var w = 0, h = 0, cx = 0, cy = 0, scale = 0;
        var angleY = 0.4, angleX = 0.15;
        var targetParX = 0, targetParY = 0, parX = 0, parY = 0;
        var running = false, rafId = null;
        var lastFrameTime = 0, prevRenderTime = null;
        var entranceStart = null, entranceDone = reduceMotion;
        var ENTRANCE_MS = 1600;

        function resize() {
            var rect = stage.getBoundingClientRect();
            w = rect.width; h = rect.height;
            if (w === 0 || h === 0) return;
            canvas.width = Math.round(w * cfg.dpr);
            canvas.height = Math.round(h * cfg.dpr);
            canvas.style.width = w + 'px';
            canvas.style.height = h + 'px';
            ctx.setTransform(cfg.dpr, 0, 0, cfg.dpr, 0, 0);
            cx = w / 2; cy = h / 2;
            scale = Math.min(w, h) * 0.40;
        }

        function rotatePoint(p, ay, ax) {
            var cosY = Math.cos(ay), sinY = Math.sin(ay);
            var x1 = p.x * cosY - p.z * sinY;
            var z1 = p.x * sinY + p.z * cosY;
            var cosX = Math.cos(ax), sinX = Math.sin(ax);
            var y2 = p.y * cosX - z1 * sinX;
            var z2 = p.y * sinX + z1 * cosX;
            return { x: x1, y: y2, z: z2 };
        }

        function easeOutCubic(t) { return 1 - Math.pow(1 - t, 3); }
        function lerp(a, b, t) { return a + (b - a) * t; }

        var COLOR_NEAR = [139, 92, 246];
        var COLOR_FAR = [99, 102, 241];

        function render(now) {
            if (w === 0) resize();
            if (w === 0) return;

            var dt = prevRenderTime ? Math.min(now - prevRenderTime, 100) : frameInterval;
            prevRenderTime = now;

            ctx.clearRect(0, 0, w, h);

            var ent = 1;
            if (!entranceDone) {
                if (entranceStart === null) entranceStart = now;
                ent = Math.min(1, (now - entranceStart) / ENTRANCE_MS);
                if (ent >= 1) entranceDone = true;
            }
            var entEase = easeOutCubic(ent);

            if (!reduceMotion) {
                angleY += 0.00028 * dt;
                angleX = 0.15 + Math.sin(now * 0.00025) * 0.05;
                parX = lerp(parX, targetParX, 0.06);
                parY = lerp(parY, targetParY, 0.06);
            }

            var pulse = reduceMotion ? 1 : (0.9 + Math.sin(now * 0.0016) * 0.1);

            var projected = new Array(basePoints.length);
            for (var i = 0; i < basePoints.length; i++) {
                var base = basePoints[i];
                var sp = startPoints[i];
                var sx = lerp(sp.x, base.x, entEase);
                var sy = lerp(sp.y, base.y, entEase);
                var sz = lerp(sp.z, base.z, entEase);
                var r = rotatePoint({ x: sx, y: sy, z: sz }, angleY + parX, angleX + parY);
                var f = 2.6 / (2.6 - r.z);
                projected[i] = { x: cx + r.x * scale * f, y: cy + r.y * scale * f, z: r.z, f: f };
            }

            ctx.lineWidth = 1;
            for (var li = 0; li < links.length; li++) {
                var a = projected[links[li][0]];
                var b = projected[links[li][1]];
                var depth = (a.f + b.f) / 2;
                var lineAlpha = Math.max(0, Math.min(1, (depth - 0.78) * 1.7)) * 0.32 * entEase;
                if (lineAlpha <= 0.01) continue;
                ctx.strokeStyle = 'rgba(' + COLOR_FAR[0] + ',' + COLOR_FAR[1] + ',' + COLOR_FAR[2] + ',' + lineAlpha + ')';
                ctx.beginPath();
                ctx.moveTo(a.x, a.y);
                ctx.lineTo(b.x, b.y);
                ctx.stroke();
            }

            var order = projected.map(function (p, idx) { return idx; });
            order.sort(function (ia, ib) { return projected[ia].z - projected[ib].z; });

            for (var oi = 0; oi < order.length; oi++) {
                var p = projected[order[oi]];
                var depthT = Math.max(0, Math.min(1, (p.f - 0.7) / 0.75));
                var radius = (0.8 + depthT * 1.5) * pulse;
                var ptAlpha = (0.3 + depthT * 0.7) * entEase;
                var c = depthT > 0.55 ? COLOR_NEAR : COLOR_FAR;

                if (cfg.glow && depthT > 0.65) {
                    var grad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, radius * 3);
                    grad.addColorStop(0, 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',' + (ptAlpha * 0.45) + ')');
                    grad.addColorStop(1, 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',0)');
                    ctx.fillStyle = grad;
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, radius * 3, 0, Math.PI * 2);
                    ctx.fill();
                }

                ctx.fillStyle = 'rgba(' + c[0] + ',' + c[1] + ',' + c[2] + ',' + ptAlpha + ')';
                ctx.beginPath();
                ctx.arc(p.x, p.y, radius, 0, Math.PI * 2);
                ctx.fill();
            }
        }

        function loop(now) {
            if (!running) return;
            rafId = requestAnimationFrame(loop);
            if (now - lastFrameTime < frameInterval - 4) return;
            lastFrameTime = now;
            render(now);
        }

        function start() {
            if (running) return;
            running = true;
            lastFrameTime = 0;
            rafId = requestAnimationFrame(loop);
        }

        function stop() {
            running = false;
            if (rafId) cancelAnimationFrame(rafId);
        }

        var hasStarted = false;
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    if (!hasStarted) {
                        hasStarted = true;
                        resize();
                        stage.classList.add('in-view');
                        if (fallback) {
                            fallback.style.transition = 'opacity 0.6s ease-out';
                            fallback.style.opacity = '0';
                        }
                        render(performance.now());
                        if (!reduceMotion) start();
                    } else if (document.visibilityState === 'visible') {
                        start();
                    }
                } else {
                    stop();
                }
            });
        }, { threshold: 0.15 });
        io.observe(stage);

        document.addEventListener('visibilitychange', function () {
            if (document.visibilityState === 'hidden') {
                stop();
            } else if (hasStarted && !reduceMotion) {
                var rect = stage.getBoundingClientRect();
                if (rect.top < window.innerHeight && rect.bottom > 0) start();
            }
        });

        var resizeTimer = null;
        window.addEventListener('resize', function () {
            clearTimeout(resizeTimer);
            resizeTimer = setTimeout(function () {
                resize();
                if (reduceMotion) render(performance.now());
            }, 150);
        }, { passive: true });

        if (!isCoarsePointer && !reduceMotion) {
            stage.addEventListener('mousemove', function (e) {
                var rect = stage.getBoundingClientRect();
                targetParX = ((e.clientX - rect.left) / rect.width - 0.5) * 0.5;
                targetParY = ((e.clientY - rect.top) / rect.height - 0.5) * 0.3;
            }, { passive: true });
            stage.addEventListener('mouseleave', function () {
                targetParX = 0; targetParY = 0;
            }, { passive: true });
        }
    })();
    
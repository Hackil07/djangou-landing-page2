
        // Date cible : 21 Septembre 2026 à 00:00:00
        const targetDate = new Date('2026-09-29T00:00:00').getTime();
        const targetUrl = 'https://djangou.site/';
        let isRedirecting = false;

        // Formspree AJAX Submission
        const waitlistForm = document.querySelector('.waitlist-form');
        const successModal = document.getElementById('successModal');
        const submitBtn = waitlistForm ? waitlistForm.querySelector('.btn-submit') : null;

        if (waitlistForm && submitBtn) {
            waitlistForm.addEventListener('submit', async function(e) {
                e.preventDefault();
                
                const originalBtnText = submitBtn.innerText;
                submitBtn.innerText = window.i18n.t('cs.js.sending');
                submitBtn.style.opacity = '0.7';
                submitBtn.disabled = true;

                const data = new FormData(waitlistForm);
                try {
                    const response = await fetch(waitlistForm.action, {
                        method: 'POST',
                        body: data,
                        headers: {
                            'Accept': 'application/json'
                        }
                    });
                    
                    if (response.ok) {
                        waitlistForm.reset();
                        successModal.classList.add('active');
                    } else {
                        alert(window.i18n.t('cs.js.error'));
                    }
                } catch (error) {
                    alert(window.i18n.t('cs.js.conn_error'));
                } finally {
                    submitBtn.innerText = originalBtnText;
                    submitBtn.style.opacity = '1';
                    submitBtn.disabled = false;
                }
            });
        }

        function closeModal() {
            successModal.classList.remove('active');
        }


        function updateCountdown() {
            if (isRedirecting) return;

            const now = new Date().getTime();
            const distance = targetDate - now;

            if (distance <= 0) {
                // Le compte à rebours est terminé
                isRedirecting = true;
                document.querySelector('.countdown').innerHTML = `<h2 style="grid-column: 1 / -1;">${window.i18n.t('cs.js.redirect')}</h2>`;
                setTimeout(() => {
                    window.location.href = targetUrl;
                }, 1500);
                return;
            }

            const days = Math.floor(distance / (1000 * 60 * 60 * 24));
            const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((distance % (1000 * 60)) / 1000);

            document.getElementById('days').innerText = days.toString().padStart(2, '0');
            document.getElementById('hours').innerText = hours.toString().padStart(2, '0');
            document.getElementById('minutes').innerText = minutes.toString().padStart(2, '0');
            document.getElementById('seconds').innerText = seconds.toString().padStart(2, '0');
        }

        // Optimisation pour les appareils bas de gamme : setInterval avec RequestAnimationFrame fallback possible, 
        // mais setInterval 1000ms est déjà très léger.
        updateCountdown();
        setInterval(updateCountdown, 1000);
    
document.getElementById("btn-close-modal").addEventListener("click", closeModal);

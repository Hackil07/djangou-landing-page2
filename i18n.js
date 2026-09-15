(function() {
    const defaultLang = 'fr';
    const supportedLangs = ['fr', 'en'];

    function getLang() {
        const savedLang = localStorage.getItem('lang');
        if (savedLang && supportedLangs.includes(savedLang)) {
            return savedLang;
        }
        const browserLang = navigator.language.slice(0, 2);
        if (supportedLangs.includes(browserLang)) {
            return browserLang;
        }
        return defaultLang;
    }

    function setLang(lang) {
        if (!supportedLangs.includes(lang)) return;
        localStorage.setItem('lang', lang);
        document.documentElement.setAttribute('lang', lang);
        applyTranslations(lang);
        updateLangSelectors(lang);
    }

    function applyTranslations(lang) {
        if (!window.i18nDictionary || !window.i18nDictionary[lang]) return;
        const dict = window.i18nDictionary[lang];

        // Replace text content
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (dict[key]) {
                // If it's an input/textarea with placeholder, or normal element
                if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
                    // It shouldn't have data-i18n for placeholder, but just in case
                } else {
                    el.innerHTML = dict[key];
                }
            }
        });

        // Replace placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (dict[key]) {
                el.setAttribute('placeholder', dict[key]);
            }
        });

        // Replace titles
        document.querySelectorAll('[data-i18n-title]').forEach(el => {
            const key = el.getAttribute('data-i18n-title');
            if (dict[key]) {
                el.setAttribute('title', dict[key]);
            }
        });

        // Replace aria-labels
        document.querySelectorAll('[data-i18n-aria]').forEach(el => {
            const key = el.getAttribute('data-i18n-aria');
            if (dict[key]) {
                el.setAttribute('aria-label', dict[key]);
            }
        });

        // Dispatch an event so other scripts (typewriter, etc.) can react
        const event = new CustomEvent('languageChanged', { detail: { lang: lang } });
        window.dispatchEvent(event);
    }

    function updateLangSelectors(activeLang) {
        document.querySelectorAll('.lang-selector').forEach(selector => {
            selector.value = activeLang;
        });
        document.querySelectorAll('.lang-btn').forEach(btn => {
            if (btn.getAttribute('data-lang') === activeLang) {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    }

    window.i18n = {
        getLang: getLang,
        setLang: setLang,
        t: function(key) {
            const lang = getLang();
            if (window.i18nDictionary && window.i18nDictionary[lang] && window.i18nDictionary[lang][key]) {
                return window.i18nDictionary[lang][key];
            }
            return key;
        }
    };

    document.addEventListener('DOMContentLoaded', () => {
        const lang = getLang();
        document.documentElement.setAttribute('lang', lang);
        applyTranslations(lang);
        updateLangSelectors(lang);

        document.querySelectorAll('.lang-selector').forEach(selector => {
            selector.addEventListener('change', (e) => {
                setLang(e.target.value);
            });
        });

        document.querySelectorAll('.lang-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                setLang(btn.getAttribute('data-lang'));
            });
        });
    });
})();

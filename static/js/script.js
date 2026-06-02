// Burger menu
const burger   = document.getElementById('burger');
const navLinks = document.getElementById('navLinks');
if (burger) {
  burger.addEventListener('click', () => navLinks.classList.toggle('open'));
}

// Language switcher
function setLang(lang) {
  document.querySelectorAll('[data-tr]').forEach(el => {
    el.innerHTML = lang === 'en' ? el.dataset.en : el.dataset.tr;
  });
  document.querySelectorAll('.lang-btn').forEach(btn => {
    btn.classList.toggle('active', btn.textContent.trim() === lang.toUpperCase());
  });
  document.documentElement.lang = lang;
  localStorage.setItem('alesta-lang', lang);
}

const savedLang = localStorage.getItem('alesta-lang');
if (savedLang && savedLang !== 'tr') setLang(savedLang);
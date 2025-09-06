document.addEventListener('DOMContentLoaded', () => {
  const btn = document.querySelector('.hamburger');
  const nav = document.querySelector('.nav');
  const links = document.querySelectorAll('.nav a');

  if (!btn || !nav) return;

  btn.addEventListener('click', () => {
    const opened = nav.classList.toggle('open');
    btn.classList.toggle('is-active');
    btn.setAttribute('aria-expanded', opened ? 'true' : 'false');
  });

  // Close menu when a nav link is clicked (mobile)
  links.forEach(link => {
    link.addEventListener('click', () => {
      nav.classList.remove('open');
      btn.classList.remove('is-active');
      btn.setAttribute('aria-expanded', 'false');
    });
  });
});



(() => {
  const body = document.body;
  const header = document.querySelector('.site-header');
  const menuToggle = document.querySelector('.menu-toggle');
  const navLinks = document.getElementById('nav-links');
  const navAnchors = Array.from(document.querySelectorAll('.nav-links a[href^="#"]'));
  const yearEl = document.getElementById('year');

  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  // Mobile menu
  const closeMenu = () => { if(!menuToggle||!navLinks)return;menuToggle.setAttribute('aria-expanded','false');navLinks.classList.remove('is-open');body.classList.remove('nav-open'); };
  const openMenu = () => { if(!menuToggle||!navLinks)return;menuToggle.setAttribute('aria-expanded','true');navLinks.classList.add('is-open');body.classList.add('nav-open'); };

  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', () => { menuToggle.getAttribute('aria-expanded')==='true' ? closeMenu() : openMenu(); });
    document.addEventListener('click', (e) => { if(!(e.target instanceof Node)||!navLinks.classList.contains('is-open')||navLinks.contains(e.target)||menuToggle.contains(e.target))return;closeMenu(); });
    window.addEventListener('resize', () => { if(window.innerWidth>860)closeMenu(); });
  }

  navAnchors.forEach(link => { link.addEventListener('click', () => { if(window.innerWidth<=860)closeMenu(); }); });

  // FAQ accordion
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-item');
      if(!item)return;
      const expanded = btn.getAttribute('aria-expanded')==='true';
      btn.setAttribute('aria-expanded', String(!expanded));
      item.classList.toggle('is-open', !expanded);
    });
  });

  // Active nav highlighting
  const sectionIds = ['hero','pricing','advantages','process','regions','faq'];
  const sections = sectionIds.map(id => document.getElementById(id)).filter(Boolean);
  const setActiveLink = (id) => { navAnchors.forEach(a => { a.classList.toggle('active', a.getAttribute('href')?.slice(1)===id); }); };

  if ('IntersectionObserver' in window && sections.length) {
    const obs = new IntersectionObserver((entries) => { entries.forEach(e => { if(e.isIntersecting) setActiveLink(e.target.id); }); }, { rootMargin:'-40% 0px -45% 0px', threshold:0 });
    sections.forEach(s => obs.observe(s));
  } else { setActiveLink('hero'); }

  // Header scroll state
  const updateHeader = () => { if(header) header.classList.toggle('is-scrolled', window.scrollY>8); };
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive:true });

  // Counter animation
  const animateCounters = () => {
    document.querySelectorAll('.stat-number[data-target]').forEach(el => {
      const target = parseInt(el.dataset.target, 10);
      const duration = 2000;
      const start = performance.now();
      const step = (now) => {
        const progress = Math.min((now - start) / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.round(target * eased).toLocaleString();
        if (progress < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    });
  };

  // Trigger counters when hero is visible
  const heroSection = document.getElementById('hero');
  if (heroSection && 'IntersectionObserver' in window) {
    let counted = false;
    const counterObs = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting && !counted) { counted = true; animateCounters(); counterObs.disconnect(); }
    }, { threshold: 0.3 });
    counterObs.observe(heroSection);
  } else { animateCounters(); }

  // Scroll-reveal animations
  const revealElements = document.querySelectorAll('.adv-card, .pricing-card, .process-step, .region-card, .faq-item');
  revealElements.forEach(el => { el.style.opacity = '0'; el.style.transform = 'translateY(24px)'; el.style.transition = 'opacity 0.5s ease, transform 0.5s ease'; });

  if ('IntersectionObserver' in window) {
    const revealObs = new IntersectionObserver((entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          setTimeout(() => { entry.target.style.opacity='1'; entry.target.style.transform='translateY(0)'; }, i * 60);
          revealObs.unobserve(entry.target);
        }
      });
    }, { threshold:0.1, rootMargin:'0px 0px -40px 0px' });
    revealElements.forEach(el => revealObs.observe(el));
  } else {
    revealElements.forEach(el => { el.style.opacity='1'; el.style.transform='none'; });
  }

  // Floating particles
  const particlesContainer = document.getElementById('particles');
  if (particlesContainer) {
    for (let i = 0; i < 30; i++) {
      const p = document.createElement('div');
      const size = Math.random() * 3 + 1;
      const x = Math.random() * 100;
      const y = Math.random() * 100;
      const dur = Math.random() * 20 + 15;
      const delay = Math.random() * -20;
      p.style.cssText = `position:absolute;width:${size}px;height:${size}px;left:${x}%;top:${y}%;border-radius:50%;background:rgba(139,92,246,${Math.random()*0.3+0.1});animation:particleFloat ${dur}s ${delay}s ease-in-out infinite;pointer-events:none;`;
      particlesContainer.appendChild(p);
    }

    const style = document.createElement('style');
    style.textContent = `@keyframes particleFloat{0%,100%{transform:translate(0,0) scale(1);opacity:0.6}25%{transform:translate(${Math.random()*40-20}px,${Math.random()*-60-20}px) scale(1.2);opacity:1}50%{transform:translate(${Math.random()*60-30}px,${Math.random()*-30-10}px) scale(0.8);opacity:0.4}75%{transform:translate(${Math.random()*-40+20}px,${Math.random()*-50-15}px) scale(1.1);opacity:0.8}}`;
    document.head.appendChild(style);
  }
})();

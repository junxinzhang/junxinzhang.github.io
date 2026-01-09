// Theme.js - Pure vanilla JS (no jQuery dependency)

// Alertbar on scroll - throttled with requestAnimationFrame
(function() {
    var ticking = false;
    var alertbar = document.querySelector('.alertbar');
    if (!alertbar) return;

    function updateAlertbar() {
        var y = window.scrollY;
        if (y > 280) {
            alertbar.style.display = 'block';
            alertbar.style.opacity = '1';
        } else {
            alertbar.style.opacity = '0';
            setTimeout(function() {
                if (window.scrollY <= 280) alertbar.style.display = 'none';
            }, 300);
        }
        ticking = false;
    }

    window.addEventListener('scroll', function() {
        if (!ticking) {
            requestAnimationFrame(updateAlertbar);
            ticking = true;
        }
    }, {passive: true});
})();

// Hide Header on scroll down - optimized with passive listener
(function() {
    var didScroll = false;
    var lastScrollTop = 0;
    var delta = 5;
    var nav = document.querySelector('nav');
    if (!nav) return;
    var navbarHeight = nav.offsetHeight;

    window.addEventListener('scroll', function() {
        didScroll = true;
    }, {passive: true});

    setInterval(function() {
        if (didScroll) {
            hasScrolled();
            didScroll = false;
        }
    }, 250);

    function hasScrolled() {
        var st = window.scrollY;

        if (Math.abs(lastScrollTop - st) <= delta) return;

        if (st > lastScrollTop && st > navbarHeight) {
            nav.classList.remove('nav-down');
            nav.classList.add('nav-up');
            nav.style.top = -nav.offsetHeight + 'px';
        } else {
            if (st + window.innerHeight < document.body.scrollHeight) {
                nav.classList.remove('nav-up');
                nav.classList.add('nav-down');
                nav.style.top = '0px';
            }
        }

        lastScrollTop = st;
    }
})();

// Set site-content margin based on header height
(function() {
    var header = document.querySelector('header');
    var siteContent = document.querySelector('.site-content');
    if (header && siteContent) {
        siteContent.style.marginTop = header.offsetHeight + 'px';
    }
})();

// Smooth scrolling - Pure vanilla JS
(function() {
    // Handle initial hash
    setTimeout(function() {
        if (location.hash) {
            window.scrollTo(0, 0);
            var target = document.querySelector(location.hash);
            if (target) {
                smoothScrollTo(target);
            }
        }
    }, 1);

    // Handle anchor clicks
    document.addEventListener('click', function(e) {
        var link = e.target.closest('a[href*="#"]:not([href="#"])');
        if (!link) return;

        if (location.pathname.replace(/^\//, '') === link.pathname.replace(/^\//, '') &&
            location.hostname === link.hostname) {
            var target = document.querySelector(link.hash);
            if (target) {
                e.preventDefault();
                smoothScrollTo(target);
            }
        }
    });

    function smoothScrollTo(target) {
        if (target) {
            window.scrollTo({
                top: target.offsetTop,
                behavior: 'smooth'
            });
        }
    }
})();

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

// Featured carousel - Pure vanilla JS (no jQuery/Bootstrap dependency)
(function() {
    var carousel = document.getElementById('featuredCarousel');
    if (!carousel) return;

    var items = carousel.querySelectorAll('.carousel-item');
    if (!items.length) return;
    var indicators = carousel.querySelectorAll('.carousel-indicators li');
    var prevBtn = carousel.querySelector('.carousel-control-prev');
    var nextBtn = carousel.querySelector('.carousel-control-next');
    var currentIndex = 0;
    var intervalId = null;
    var interval = 5000; // Auto-slide every 5 seconds

    function showSlide(index) {
        if (index >= items.length) index = 0;
        if (index < 0) index = items.length - 1;

        items.forEach(function(item) { item.classList.remove('active'); });
        indicators.forEach(function(ind) { ind.classList.remove('active'); });

        items[index].classList.add('active');
        if (indicators[index]) indicators[index].classList.add('active');

        currentIndex = index;
    }

    function nextSlide() {
        showSlide(currentIndex + 1);
    }

    function prevSlide() {
        showSlide(currentIndex - 1);
    }

    function startAutoSlide() {
        stopAutoSlide();
        intervalId = setInterval(nextSlide, interval);
    }

    function stopAutoSlide() {
        if (intervalId) {
            clearInterval(intervalId);
            intervalId = null;
        }
    }

    if (prevBtn) {
        prevBtn.addEventListener('click', function(e) {
            e.preventDefault();
            prevSlide();
            startAutoSlide();
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', function(e) {
            e.preventDefault();
            nextSlide();
            startAutoSlide();
        });
    }

    indicators.forEach(function(indicator, index) {
        indicator.addEventListener('click', function() {
            showSlide(index);
            startAutoSlide();
        });
    });

    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowLeft') {
            prevSlide();
            startAutoSlide();
        } else if (e.key === 'ArrowRight') {
            nextSlide();
            startAutoSlide();
        }
    });

    carousel.addEventListener('mouseenter', stopAutoSlide);
    carousel.addEventListener('mouseleave', startAutoSlide);

    var touchStartX = 0;
    var touchEndX = 0;
    var touchStartY = 0;
    var touchEndY = 0;
    var minSwipeDistance = 50;

    carousel.addEventListener('touchstart', function(e) {
        touchStartX = e.changedTouches[0].screenX;
        touchStartY = e.changedTouches[0].screenY;
        stopAutoSlide();
    }, {passive: true});

    carousel.addEventListener('touchend', function(e) {
        touchEndX = e.changedTouches[0].screenX;
        touchEndY = e.changedTouches[0].screenY;
        handleSwipe();
        startAutoSlide();
    }, {passive: true});

    function handleSwipe() {
        var deltaX = touchEndX - touchStartX;
        var deltaY = touchEndY - touchStartY;

        if (Math.abs(deltaX) > Math.abs(deltaY) && Math.abs(deltaX) > minSwipeDistance) {
            if (deltaX > 0) {
                prevSlide();
            } else {
                nextSlide();
            }
        }
    }

    startAutoSlide();
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

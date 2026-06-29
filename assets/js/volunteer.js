// ========================================
// VOLUNTEER PAGE - SLIDESHOW + FORM UX
// ========================================

document.addEventListener('DOMContentLoaded', function () {

    // ── Slideshow ────────────────────────────────────────────────────
    const slideshow = document.querySelector('.slideshow');
    const slides = document.querySelectorAll('.slide');

    if (slideshow && slides.length > 0) {
        let currentSlide = 0;

        function showSlide(index) {
            slides.forEach(function (slide) {
                slide.style.display = 'none';
                slide.classList.remove('active');
            });
            slides[index].style.display = 'block';
            slides[index].classList.add('active');
            currentSlide = index;
        }

        showSlide(0);
        if (slides.length > 1) {
            setInterval(function () {
                showSlide((currentSlide + 1) % slides.length);
            }, 4000);
        }
    }

    // ── Submit loading state ─────────────────────────────────────────
    const form = document.querySelector('.volunteer-right form');
    if (form) {
        form.addEventListener('submit', function (e) {
            const btn = form.querySelector('button[type="submit"]');
            if (!btn) return;
            queueMicrotask(function () {
                if (!e.defaultPrevented) {
                    btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Sending...';
                    btn.disabled = true;
                }
            });
        });
    }
});

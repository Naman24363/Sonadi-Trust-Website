// ========================================
// ADOPT-A-DOG PAGE FUNCTIONALITY
// ========================================

document.addEventListener('DOMContentLoaded', function () {

    // GSAP animations for animal cards (if GSAP loaded)
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        gsap.from('.animal-card', {
            scrollTrigger: {
                trigger: '.animal-gallery',
                start: 'top 80%'
            },
            duration: 0.6,
            y: 50,
            opacity: 0,
            stagger: 0.15,
            ease: 'power2.out'
        });
    }
});

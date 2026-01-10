 // Year
        document.getElementById('year').textContent = new Date().getFullYear();

        // Slick: Hero slider
        $('.hero-slider').slick({
            dots: true,
            arrows: true,
            infinite: true,
            speed: 650,
            autoplay: true,
            autoplaySpeed: 3500,
            fade: true,
            cssEase: 'ease-in-out',
            pauseOnHover: false,
            pauseOnFocus: false
        });

        // Slick: Testimonials slider
        $('.testi-slider').slick({
            dots: true,
            arrows: false,
            infinite: true,
            speed: 500,
            autoplay: true,
            autoplaySpeed: 3200,
            slidesToShow: 3,
            slidesToScroll: 1,
            responsive: [
                { breakpoint: 992, settings: { slidesToShow: 2 } },
                { breakpoint: 576, settings: { slidesToShow: 1 } }
            ]
        });

        // Scroll reveal for every section element with .reveal
        const io = new IntersectionObserver((entries) => {
            entries.forEach((e) => {
                if (e.isIntersecting) {
                    e.target.classList.add('in');
                    io.unobserve(e.target);
                }
            });
        }, { threshold: 0.12 });

        document.querySelectorAll('.reveal').forEach((el) => io.observe(el));

        // Toast helper
        function toast(msg) {
            document.getElementById('pcToastBody').textContent = msg;
            const t = bootstrap.Toast.getOrCreateInstance(document.getElementById('pcToast'), { delay: 2600 });
            t.show();
        }
document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Add animation for cards on scroll
    const animateOnScroll = function() {
        const cards = document.querySelectorAll('.overview-card, .highlight-item, .link-card, .cost-card, .phase-card, .risk-card, .governance-card');
        
        cards.forEach(card => {
            const cardPosition = card.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.2;
            
            if (cardPosition < screenPosition) {
                card.classList.add('animate');
            }
        });
    };
    
    // Run animation check on load and scroll
    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll(); // Run once on page load
    
    // Add mobile menu toggle functionality
    const createMobileMenu = function() {
        const header = document.querySelector('header');
        const nav = document.querySelector('nav');
        
        // Create mobile menu button
        const mobileMenuBtn = document.createElement('button');
        mobileMenuBtn.classList.add('mobile-menu-btn');
        mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
        header.insertBefore(mobileMenuBtn, nav);
        
        // Toggle menu on click
        mobileMenuBtn.addEventListener('click', function() {
            nav.classList.toggle('active');
            this.innerHTML = nav.classList.contains('active') ? 
                '<i class="fas fa-times"></i>' : 
                '<i class="fas fa-bars"></i>';
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!nav.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                nav.classList.remove('active');
                mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
            }
        });
    };
    
    // Check if we need mobile menu
    if (window.innerWidth < 768) {
        createMobileMenu();
    }
    
    // Recreate mobile menu on resize if needed
    window.addEventListener('resize', function() {
        const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
        
        if (window.innerWidth < 768 && !mobileMenuBtn) {
            createMobileMenu();
        } else if (window.innerWidth >= 768 && mobileMenuBtn) {
            mobileMenuBtn.remove();
            document.querySelector('nav').classList.remove('active');
        }
    });
});

// Add CSS animation class
document.head.insertAdjacentHTML('beforeend', `
<style>
    .overview-card, .highlight-item, .link-card, .cost-card, .phase-card, .risk-card, .governance-card {
        opacity: 0;
        transform: translateY(20px);
        transition: opacity 0.5s ease, transform 0.5s ease;
    }
    
    .overview-card.animate, .highlight-item.animate, .link-card.animate, .cost-card.animate, .phase-card.animate, .risk-card.animate, .governance-card.animate {
        opacity: 1;
        transform: translateY(0);
    }
    
    /* Mobile menu styles */
    @media screen and (max-width: 768px) {
        .mobile-menu-btn {
            display: block;
            background: none;
            border: none;
            color: var(--truist-white);
            font-size: 1.5rem;
            cursor: pointer;
            position: absolute;
            top: 20px;
            right: 20px;
            z-index: 1001;
        }
        
        nav {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: var(--truist-purple);
            z-index: 1000;
            padding-top: 80px;
        }
        
        nav.active {
            display: block;
        }
        
        nav ul {
            flex-direction: column;
            align-items: center;
        }
        
        nav ul li {
            margin: 15px 0;
        }
    }
</style>
`);

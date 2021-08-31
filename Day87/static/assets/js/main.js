/**
* Template Name: MeFamily - v4.3.0
* Template URL: https://bootstrapmade.com/family-multipurpose-html-bootstrap-template-free/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    if (!header.classList.contains('header-scrolled')) {
      offset -= 16
    }

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Hero carousel indicators
   */
  let heroCarouselIndicators = select("#hero-carousel-indicators")
  let heroCarouselItems = select('#heroCarousel .carousel-item', true)

  heroCarouselItems.forEach((item, index) => {
    (index === 0) ?
    heroCarouselIndicators.innerHTML += "<li data-bs-target='#heroCarousel' data-bs-slide-to='" + index + "' class='active'></li>":
      heroCarouselIndicators.innerHTML += "<li data-bs-target='#heroCarousel' data-bs-slide-to='" + index + "'></li>"
  });

  /**
   * Clients Slider
   */
  new Swiper('.recent-photos-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },
      640: {
        slidesPerView: 2,
        spaceBetween: 20
      },
      992: {
        slidesPerView: 3,
        spaceBetween: 20
      },
      1200: {
        slidesPerView: 5,
        spaceBetween: 20
      }
    }
  });

  /**
   * Gallery isotope and filter
   */
  window.addEventListener('load', () => {
    let galelryContainer = select('.gallery-container');
    if (galelryContainer) {
      let galleryIsotope = new Isotope(galelryContainer, {
        itemSelector: '.gallery-item',
      });

      let galleryFilters = select('#gallery-flters li', true);

      on('click', '#gallery-flters li', function(e) {
        e.preventDefault();
        galleryFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        galleryIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });

      }, true);
    }

  });

  /**
   * Initiate glightbox 
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

})()
if(document.getElementById("has_sockets").checked) {
    document.getElementById('has_socketsHidden').disabled = true;
}
if(document.getElementById("has_toilet").checked) {
    document.getElementById('has_toiletHidden').disabled = true;
}
if(document.getElementById("has_wifi").checked) {
    document.getElementById('has_wifiHidden').disabled = true;
}
if(document.getElementById("can_take_calls").checked) {
    document.getElementById('can_take_callsHidden').disabled = true;
}

/**
 * Font Awesome CDN Setup Webfont
 *
 * This will load Font Awesome from the Font Awesome Free or Pro CDN.
 */
//if (! function_exists('fa_custom_setup_cdn_webfont') ) {
//  function fa_custom_setup_cdn_webfont($cdn_url = '', $integrity = null) {
//    $matches = [];
//    $match_result = preg_match('|/([^/]+?)\.css$|', $cdn_url, $matches);
//    $resource_handle_uniqueness = ($match_result === 1) ? $matches[1] : md5($cdn_url);
//    $resource_handle = "font-awesome-cdn-webfont-$resource_handle_uniqueness";
//
//    foreach ( [ 'wp_enqueue_scripts', 'admin_enqueue_scripts', 'login_enqueue_scripts' ] as $action ) {
//      add_action(
//        $action,
//        function () use ( $cdn_url, $resource_handle ) {
//          wp_enqueue_style( $resource_handle, $cdn_url, [], null );
//        }
//      );
//    }
//
//    if($integrity) {
//      add_filter(
//        'style_loader_tag',
//        function( $html, $handle ) use ( $resource_handle, $integrity ) {
//          if ( in_array( $handle, [ $resource_handle ], true ) ) {
//            return preg_replace(
//              '/\/>$/',
//              'integrity="' . $integrity .
//              '" crossorigin="anonymous" />',
//              $html,
//              1
//            );
//          } else {
//            return $html;
//          }
//        },
//        10,
//        2
//      );
//    }
//  }
//}
//

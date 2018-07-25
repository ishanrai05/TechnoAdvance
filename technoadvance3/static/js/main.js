var i = 0;
     var txt = 'Welcome to Techno Advance';
     var speed = 80;
     
     function typeWriter() {
       if (i < txt.length) {
         document.getElementById("typeText").innerHTML += txt.charAt(i);
         i++;
         setTimeout(typeWriter, speed);
       }
      }
      

jQuery(document).ready(function($) {
  
$(".hover").mouseleave(
    function () {
      $(this).removeClass("hover");
    }
  );

  // Header fixed and Back to top button
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('.back-to-top').fadeIn('slow');
      $('#header').addClass('header-fixed');
    } else {
      $('.back-to-top').fadeOut('slow');
      $('#header').removeClass('header-fixed');
    }
  });

  if ($(this).scrollTop() > 100) {
    $('.back-to-top').fadeIn('slow');
    $('#header').addClass('header-fixed');
  }

  $('.back-to-top').click(function() {
    $('html, body').animate({
      scrollTop: 0
    }, 1500, 'easeInOutExpo');
    return false;
  });

  // Initiate the wowjs animation library
  new WOW().init();

  // Initiate superfish on nav menu
  $('.nav-menu').superfish({
    animation: {
      opacity: 'show'
    },
    speed: 400
  });

  // Mobile Navigation
  if ($('#nav-menu-container').length) {
    var $mobile_nav = $('#nav-menu-container').clone().prop({
      id: 'mobile-nav'
    });
    $mobile_nav.find('> ul').attr({
      'class': '',
      'id': ''
    });
    $('body').append($mobile_nav);
    $('body').prepend('<button type="button" id="mobile-nav-toggle"><i class="fa fa-bars"></i></button>');
    $('body').append('<div id="mobile-body-overly"></div>');
    $('#mobile-nav').find('.menu-has-children').prepend('<i class="fa fa-chevron-down"></i>');

    $(document).on('click', '.menu-has-children i', function(e) {
      $(this).next().toggleClass('menu-item-active');
      $(this).nextAll('ul').eq(0).slideToggle();
      $(this).toggleClass("fa-chevron-up fa-chevron-down");
    });

    $(document).on('click', '#mobile-nav-toggle', function(e) {
      $('body').toggleClass('mobile-nav-active');
      $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
      $('#mobile-body-overly').toggle();
    });

    $(document).click(function(e) {
      var container = $("#mobile-nav, #mobile-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('#mobile-body-overly').fadeOut();
        }
      }
    });
  } else if ($("#mobile-nav, #mobile-nav-toggle").length) {
    $("#mobile-nav, #mobile-nav-toggle").hide();
  }

  // Smoth scroll on page hash links
  $('.nav-menu a, #mobile-nav a, .scrollto').on('click', function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        var top_space = 0;

        if ($('#header').length) {
          top_space = $('#header').outerHeight();

          if( ! $('#header').hasClass('header-fixed') ) {
            top_space = top_space - 20;
          }
        }

        $('html, body').animate({
          scrollTop: target.offset().top - top_space
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu').length) {
          $('.nav-menu .menu-active').removeClass('menu-active');
          $(this).closest('li').addClass('menu-active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('#mobile-body-overly').fadeOut();
        }
        return false;
      }
    }
  });

  // Gallery - uses the magnific popup jQuery plugin
  $('.gallery-popup').magnificPopup({
    type: 'image',
    removalDelay: 300,
    mainClass: 'mfp-fade',
    gallery: {
      enabled: true
    },
    zoom: {
      enabled: true,
      duration: 300,
      easing: 'ease-in-out',
      opener: function(openerElement) {
        return openerElement.is('img') ? openerElement : openerElement.find('img');
      }
    }
  });

  // Couresel
  $(".client-slider").slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 4000,
    dots:true,
    responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
        dots: false
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: false
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
  });

  $(".workshop-list").slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 4000,
    dots:true,
    responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2,
        dots: false
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: false
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
  });


});


$(".testimonials").slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 4000,
    dots:true,
});
/*
  Hielo by TEMPLATED
  templated.co @templatedco
  Released for free under the Creative Commons Attribution 3.0 license (templated.co/license)
*/

var settings = {

  banner: {

    // Indicators (= the clickable dots at the bottom).
      indicators: true,

    // Transition speed (in ms)
    // For timing purposes only. It *must* match the transition speed of "#banner > article".
      speed: 1500,

    // Transition delay (in ms)
      delay: 5000,

    // Parallax intensity (between 0 and 1; higher = more intense, lower = less intense; 0 = off)
      parallax: 0.25

  }

};

(function($) {

  skel.breakpoints({
    xlarge: '(max-width: 1680px)',
    large:  '(max-width: 1280px)',
    medium: '(max-width: 980px)',
    small:  '(max-width: 736px)',
    xsmall: '(max-width: 480px)'
  });

  /**
   * Applies parallax scrolling to an element's background image.
   * @return {jQuery} jQuery object.
   */
  $.fn._parallax = (skel.vars.browser == 'ie' || skel.vars.mobile) ? function() { return $(this) } : function(intensity) {

    var $window = $(window),
      $this = $(this);

    if (this.length == 0 || intensity === 0)
      return $this;

    if (this.length > 1) {

      for (var i=0; i < this.length; i++)
        $(this[i])._parallax(intensity);

      return $this;

    }

    if (!intensity)
      intensity = 0.25;

    $this.each(function() {

      var $t = $(this),
        on, off;

      on = function() {

        $t.css('background-position', 'center 100%, center 100%, center 0px');

        $window
          .on('scroll._parallax', function() {

            var pos = parseInt($window.scrollTop()) - parseInt($t.position().top);

            $t.css('background-position', 'center ' + (pos * (-1 * intensity)) + 'px');

          });

      };

      off = function() {

        $t
          .css('background-position', '');

        $window
          .off('scroll._parallax');

      };

      skel.on('change', function() {

        if (skel.breakpoint('medium').active)
          (off)();
        else
          (on)();

      });

    });

    $window
      .off('load._parallax resize._parallax')
      .on('load._parallax resize._parallax', function() {
        $window.trigger('scroll');
      });

    return $(this);

  };

  /**
   * Custom banner slider for Slate.
   * @return {jQuery} jQuery object.
   */
  $.fn._slider = function(options) {

    var $window = $(window),
      $this = $(this);

    if (this.length == 0)
      return $this;

    if (this.length > 1) {

      for (var i=0; i < this.length; i++)
        $(this[i])._slider(options);

      return $this;

    }

    // Vars.
      var current = 0, pos = 0, lastPos = 0,
        slides = [], indicators = [],
        $indicators,
        $slides = $this.children('article'),
        intervalId,
        isLocked = false,
        i = 0;

    // Turn off indicators if we only have one slide.
      if ($slides.length == 1)
        options.indicators = false;

    // Functions.
      $this._switchTo = function(x, stop) {

        if (isLocked || pos == x)
          return;

        isLocked = true;

        if (stop)
          window.clearInterval(intervalId);

        // Update positions.
          lastPos = pos;
          pos = x;

        // Hide last slide.
          slides[lastPos].removeClass('top');

          if (options.indicators)
            indicators[lastPos].removeClass('visible');

        // Show new slide.
          slides[pos].addClass('visible').addClass('top');

          if (options.indicators)
            indicators[pos].addClass('visible');

        // Finish hiding last slide after a short delay.
          window.setTimeout(function() {

            slides[lastPos].addClass('instant').removeClass('visible');

            window.setTimeout(function() {

              slides[lastPos].removeClass('instant');
              isLocked = false;

            }, 100);

          }, options.speed);

      };

    // Indicators.
      if (options.indicators)
        $indicators = $('<ul class="indicators"></ul>').appendTo($this);

    // Slides.
      $slides
        .each(function() {

          var $slide = $(this),
            $img = $slide.find('img');

          // Slide.
            $slide
              .css('background-image', 'url("' + $img.attr('src') + '")')
              .css('background-position', ($slide.data('position') ? $slide.data('position') : 'center'));

          // Add to slides.
            slides.push($slide);

          // Indicators.
            if (options.indicators) {

              var $indicator_li = $('<li>' + i + '</li>').appendTo($indicators);

              // Indicator.
                $indicator_li
                  .data('index', i)
                  .on('click', function() {
                    $this._switchTo($(this).data('index'), true);
                  });

              // Add to indicators.
                indicators.push($indicator_li);

            }

          i++;

        })
        ._parallax(options.parallax);

    // Initial slide.
      slides[pos].addClass('visible').addClass('top');

      if (options.indicators)
        indicators[pos].addClass('visible');

    // Bail if we only have a single slide.
      if (slides.length == 1)
        return;

    // Main loop.
      intervalId = window.setInterval(function() {

        current++;

        if (current >= slides.length)
          current = 0;

        $this._switchTo(current);

      }, options.delay);

  };

  $(function() {

    var $window   = $(window),
      $body     = $('body'),
      $header   = $('#header'),
      $banner   = $('.banner');

    // Disable animations/transitions until the page has loaded.
      $body.addClass('is-loading');

      $window.on('load', function() {
        window.setTimeout(function() {
          $body.removeClass('is-loading');
        }, 100);
      });

    // Prioritize "important" elements on medium.
      skel.on('+medium -medium', function() {
        $.prioritize(
          '.important\\28 medium\\29',
          skel.breakpoint('medium').active
        );
      });

    // Banner.
      $banner._slider(settings.banner);

    // Menu.
      $('#menu')
        .append('<a href="#menu" class="close"></a>')
        .appendTo($body)
        .panel({
          delay: 500,
          hideOnClick: true,
          hideOnSwipe: true,
          resetScroll: true,
          resetForms: true,
          side: 'right'
        });

    // Header.
      if (skel.vars.IEVersion < 9)
        $header.removeClass('alt');

      if ($banner.length > 0
      &&  $header.hasClass('alt')) {

        $window.on('resize', function() { $window.trigger('scroll'); });

        $banner.scrollex({
          bottom:   $header.outerHeight(),
          terminate:  function() { $header.removeClass('alt'); },
          enter:    function() { $header.addClass('alt'); },
          leave:    function() { $header.removeClass('alt'); $header.addClass('reveal'); }
        });

      }

  });

})(jQuery);


var prevButton = '<button type="button" data-role="none" class="slick-prev" aria-label="prev"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" version="1.1"><path fill="#FFFFFF" d="M 16,16.46 11.415,11.875 16,7.29 14.585,5.875 l -6,6 6,6 z" /></svg></button>',
    nextButton = '<button type="button" data-role="none" class="slick-next" aria-label="next"><svg version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path fill="#FFFFFF" d="M8.585 16.46l4.585-4.585-4.585-4.585 1.415-1.415 6 6-6 6z"></path></svg></button>';

$('.single-item').slick({
  infinite: true,
  dots: true,
  autoplay: true,
  autoplaySpeed: 4000,
  speed: 1000,
  cssEase: 'ease-in-out',
  prevArrow: prevButton,
  nextArrow: nextButton
});

$('.quote-container').mousedown(function(){
  $('.single-item').addClass('dragging');
});
$('.quote-container').mouseup(function(){
  $('.single-item').removeClass('dragging');
});
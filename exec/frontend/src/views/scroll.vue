<template>

  <div class="o-scroll" id="js-scroll">
    <div data-scroll-section>
        <div class="o-container">
            <header class="c-header" id="header">
                <div class="c-header_heading" data-scroll data-scroll-speed="-8" data-scroll-position="top" data-scroll-target="#header">
                    <div class="o-layout">
                        <div class="o-layout_item u-1/2" data-scroll data-scroll-direction="horizontal" data-scroll-speed="-2" data-scroll-position="top" data-scroll-target="#header">
                            <span class="u-label c-header_heading_label">
                                <a href="/">
                                    Locomotive.ca
                                </a>
                            </span>
                        </div>
                        <div class="o-layout_item u-1/2" data-scroll data-scroll-direction="horizontal" data-scroll-speed="2" data-scroll-position="top" data-scroll-target="#header">
                            <div class="u-text-right">
                                <p class="u-label c-header_heading_label">
                                    v3 – Edition
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <h1 class="c-header_title o-h1" data-scroll>
                    <span class="c-header_title_line">
                        <span data-scroll data-scroll-speed="3" data-scroll-position="top">Locomotive</span>
                    </span>
                    <span class="c-header_title_line">
                        <span data-scroll data-scroll-speed="2" data-scroll-position="top">Scroll</span>
                    </span>
                    <span class="c-header_title_line -version u-white">
                        <span class="o-h1" data-scroll data-scroll-speed="3" data-scroll-position="top" data-scroll-delay="0.05">v</span><span class="o-h1" data-scroll data-scroll-speed="5" data-scroll-position="top" data-scroll-delay="0.05">3</span><span class="o-h1" data-scroll data-scroll-speed="2" data-scroll-position="top" data-scroll-delay="0.05">.</span><span class="o-h1" data-scroll data-scroll-speed="4" data-scroll-position="top" data-scroll-delay="0.05">0</span>
                    </span>
                </h1>
                <hr class="c-header_line" data-scroll data-scroll-offset="100" />
                <a class="c-header_logo" href="https://locomotive.ca" target="_blank">
                    <svg role="img"><use xlink:href="dist/images/sprite.svg#logo"></use></svg>
                </a>
            </header>
        </div>
    </div>

    <section data-scroll-section>
        <div class="o-container">
            <div class="c-summary" data-scroll data-scroll-offset="100">
                <div class="o-layout -gutter">
                    <div class="o-layout_item u-2/5@from-medium">
                        <p class="c-summary_text">
                            A simple scroll library used by developers at Locomotive. Built as a layer on top of <em>ayamflow's</em> <a href="https://github.com/ayamflow/virtual-scroll" target="_blank">virtual-scroll</a>, it provides smooth scrolling with support for parallax effects, toggling classes, and triggering event listeners when elements are in the viewport.
                        </p>
                    </div>
                    <div class="o-layout_item u-3/5@from-medium">
                        <ul class="c-summary_list">
                            <li class="c-summary_list_item u-label" data-scroll>
                                <a href="#speed-control" data-scroll-to>
                                    01. Speed Control
                                    <span class="c-summary_list_icon u-icon">
                                        ↓
                                    </span>
                                </a>
                            </li>
                            <li class="c-summary_list_item u-label" data-scroll>
                                <a href="#scroll-direction" data-scroll-to>
                                    02. Scroll direction
                                    <span class="c-summary_list_icon u-icon">
                                        ↓
                                    </span>
                                </a>
                            </li>
                            <li class="c-summary_list_item u-label" data-scroll>
                                <a href="#lerp-effect" data-scroll-to>
                                    03. Lerp effect
                                    <span class="c-summary_list_icon u-icon">
                                        ↓
                                    </span>
                                </a>
                            </li>
                            <li class="c-summary_list_item u-label" data-scroll>
                                <a href="#fixed-elements" data-scroll-to>
                                    04. Fixed Elements
                                    <span class="c-summary_list_icon u-icon">
                                        ↓
                                    </span>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="c-section" data-scroll-section>
        <div class="o-container" id="speed-control">
            <div class="o-layout -gutter">
                <div class="o-layout_item u-2/5@from-medium">
                    <div class="c-section_infos -padding" data-scroll data-scroll-speed="-2">
                        <div class="c-section_infos_inner" data-scroll data-scroll-offset="200">
                            <h3>
                                01. <br>
                                Speed control
                            </h3>
                            <div class="c-sections_infos_text u-text">
                                <p>
                                    Each element can be animated at a different speed. You get to choo-choo-choose!
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="o-layout_item u-3/5@from-medium">
                    <div class="c-speed-block" data-scroll data-scroll-speed="2">
                        <div class="o-image_wrapper" data-scroll data-scroll-call="dynamicBackground" data-scroll-repeat>
                            <div class="o-image" data-scroll>
                                <img class="c-speed-block_image" src="dist/images/locomotive01.jpg" alt="Locomotive image from unsplash">
                            </div>
                        </div>
                        <p class="c-speed-block_title" data-scroll>
                            Speed x2
                        </p>
                        <span class="c-speed-block_bubble" data-scroll data-scroll-speed="4" data-scroll-call="dynamicColor" data-scroll-repeat>
                            4x
                        </span>
                    </div>
                </div>
            </div>
            <div class="o-layout -gutter -bottom">
                <div class="o-layout_item u-2/5@from-medium">
                    <div class="c-speed-block" data-scroll data-scroll-speed="4">
                        <div class="o-image_wrapper" data-scroll data-scroll-call="dynamicBackground" data-scroll-repeat>
                            <div class="o-image" data-scroll data-scroll-speed="-1.5">
                                <img class="c-speed-block_image" src="dist/images/locomotive02.jpg" alt="Locomotive image from unsplash">
                            </div>
                        </div>
                        <p class="c-speed-block_title" data-scroll>
                            Speed x4
                        </p>
                        <span class="c-speed-block_bubble -right" data-scroll data-scroll-speed="1" data-scroll-call="dynamicColor" data-scroll-repeat>
                            1x
                        </span>
                        <span class="c-speed-block_bubble -left -bottom" data-scroll data-scroll-speed="3" data-scroll-call="dynamicColor" data-scroll-repeat>
                            3x
                        </span>
                    </div>
                </div>
                <div class="o-layout_item u-3/5@from-medium">
                    <div class="o-layout u-text-right">
                        <div class="o-layout_item u-1/2@from-medium">
                            <div class="c-speed-block -margin" data-scroll data-scroll-speed="6">
                                <div class="o-image_wrapper" data-scroll data-scroll-call="dynamicBackground" data-scroll-repeat>
                                    <div class="o-image" data-scroll data-scroll-speed="-2">
                                        <img class="c-speed-block_image" src="dist/images/locomotive03.jpg" alt="Locomotive image from unsplash">
                                    </div>
                                </div>
                                <p class="c-speed-block_title" data-scroll>
                                    Speed x6
                                </p>
                                <span class="c-speed-block_bubble -left -top" data-scroll data-scroll-speed="2" data-scroll-call="dynamicColor" data-scroll-repeat>
                                    2x
                                </span>
                                <span class="c-speed-block_bubble -right" data-scroll data-scroll-speed="6" data-scroll-call="dynamicColor" data-scroll-repeat>
                                    6x
                                </span>
                                <span class="c-speed-block_bubble -left -bottom" data-scroll data-scroll-speed="9" data-scroll-call="dynamicColor" data-scroll-repeat>
                                    9x
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="c-section" data-scroll-section>
        <div class="o-container" id="scroll-direction">
            <div class="c-direction-block_wrapper">
                <div class="c-section_infos -padding" data-scroll data-scroll-sticky data-scroll-target="#scroll-direction">
                    <div class="c-section_infos_inner" data-scroll>
                        <h3>
                            02. <br>
                            Scroll direction
                        </h3>
                        <div class="c-sections_infos_text u-text">
                            <p>
                                And if that wasn't enough, make 'em go backwards. Or upwards. Or downwards!
                            </p>
                        </div>
                    </div>
                </div>
                <div class="c-direction-block" id="direction">
                    <div class="c-direction-block_item -one">
                        <span class="c-direction-block_item_inner" data-scroll data-scroll-direction="horizontal" data-scroll-speed="6" data-scroll-target="#direction">
                            I'm moving in this direction
                        </span>
                    </div>
                    <div class="c-direction-block_item -two">
                        <span class="c-direction-block_item_inner" data-scroll data-scroll-direction="horizontal" data-scroll-speed="-8" data-scroll-target="#direction">
                            And in this direction
                        </span>
                    </div>
                    <div class="c-direction-block_item -three">
                        <span class="c-direction-block_item_inner" data-scroll data-scroll-direction="horizontal" data-scroll-speed="9" data-scroll-target="#direction" data-scroll-delay="0.05">
                            Sooo customizable. Right?
                        </span>
                    </div>
                    <div class="c-direction-block_item -four">
                        <span class="c-direction-block_item_inner" data-scroll data-scroll-direction="horizontal" data-scroll-speed="15" data-scroll-target="#direction">
                            I can also go in this direction
                        </span>
                    </div>
                    <div class="c-direction-block_item -five">
                        <span class="c-direction-block_item_inner" data-scroll data-scroll-direction="horizontal" data-scroll-speed="-20" data-scroll-target="#direction" data-scroll-delay="0.05">
                            Ok, enough!!!!
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="c-section" data-scroll-section>
        <div class="o-container" id="lerp-effect">
            <div class="o-layout">
                <div class="o-layout_item u-2/5@from-medium">
                    <div class="c-section_infos" data-scroll>
                        <div class="c-section_infos_inner" data-scroll data-scroll-offset="200">
                            <h3>
                                03. <br>
                                Lerp elements
                            </h3>
                            <div class="c-sections_infos_text u-text">
                                <p>
                                    Stagger those smooth animations using delays to create a rushing or dragging effect.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="o-layout_item u-3/5@from-medium">
                    <div class="c-lerp-block">
                        <span class="c-lerp-block_index" data-scroll data-scroll-delay="0.2" data-scroll-speed="6" data-scroll-call="dynamicColor" data-scroll-repeat>
                            01
                        </span>
                        <span class="c-lerp-block_title" data-scroll data-scroll-delay="0.6" data-scroll-speed="6">
                            <span>
                                I have a lerp
                            </span>
                        </span>
                    </div>
                    <div class="c-lerp-block">
                        <span class="c-lerp-block_index" data-scroll data-scroll-delay="0.06" data-scroll-speed="6" data-scroll-call="dynamicColor" data-scroll-repeat>
                            02
                        </span>
                        <span class="c-lerp-block_title" data-scroll data-scroll-delay="0.1" data-scroll-speed="6">
                            <span>
                                Me too! <br>
                                And even more
                            </span>
                        </span>
                    </div>
                    <div class="c-lerp-block">
                        <span class="c-lerp-block_index" data-scroll data-scroll-delay="0.06" data-scroll-speed="6" data-scroll-call="dynamicColor" data-scroll-repeat>
                            03
                        </span>
                        <span class="c-lerp-block_title" data-scroll>
                            <span data-scroll data-scroll-delay="0.13" data-scroll-speed="6">B</span>
                            <span data-scroll data-scroll-delay="0.12" data-scroll-speed="6">y</span>
                            <span data-scroll data-scroll-delay="0.11" data-scroll-speed="6"> </span>
                            <span data-scroll data-scroll-delay="0.1" data-scroll-speed="6">L</span>
                            <span data-scroll data-scroll-delay="0.09" data-scroll-speed="6">e</span>
                            <span data-scroll data-scroll-delay="0.08" data-scroll-speed="6">t</span>
                            <span data-scroll data-scroll-delay="0.07" data-scroll-speed="6">t</span>
                            <span data-scroll data-scroll-delay="0.06" data-scroll-speed="6">e</span>
                            <span data-scroll data-scroll-delay="0.05" data-scroll-speed="6">r</span>
                        </span>
                    </div>
                    <div class="c-lerp-block">
                        <span class="c-lerp-block_index" data-scroll data-scroll-delay="0.03" data-scroll-speed="6" data-scroll-call="dynamicColor" data-scroll-repeat>
                            04
                        </span>
                        <span class="c-lerp-block_title" data-scroll data-scroll-delay="0.04" data-scroll-speed="6">
                            <span>
                                Soooo smooooth
                            </span>
                        </span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="c-section -fixed" data-scroll-section data-persistent>
        <div class="o-container" id="fixed-elements">
            <div class="o-layout">
                <div class="o-layout_item u-2/5@from-medium">
                    <div class="c-section_infos -padding" data-scroll data-scroll-sticky data-scroll-target="#fixed-elements">
                        <div class="c-section_infos_inner" data-scroll data-scroll-offset="200">
                            <h3>
                                04. <br>
                                Fixed elements
                            </h3>
                            <div class="c-sections_infos_text u-text">
                                <p>
                                    Create slides that stick and untick to the viewport while scrolling through.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="o-layout_item u-3/5@from-medium">
                    <div class="c-fixed_wrapper" data-scroll data-scroll-call="dynamicBackground" data-scroll-repeat>
                        <div class="c-fixed_target" id="fixed-target"></div>
                        <div class="c-fixed" data-scroll data-scroll-sticky data-scroll-target="#fixed-target" style="background-image:url('dist/images/locomotive04.jpg')"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="c-section" data-scroll-section>
        <div class="o-container">
            <div class="c-cta">
                <h1 class="o-title" data-scroll>
                    <span class="o-title_line">
                        <span>If you</span>
                    </span>
                    <span class="o-title_line">
                        <span>Enjoyed</span>
                    </span>
                    <span class="o-title_line u-white">
                        <span>Scrolling</span>
                    </span>
                </h1>
                <hr class="c-cta_line" data-scroll data-scroll-offset="100"/>
                <div class="c-cta_content">
                    <div class="o-layout -gutter">
                        <div class="o-layout_item u-2/5@from-medium">
                            <p class="u-label">
                                Github
                            </p>
                        </div>
                        <div class="o-layout_item u-3/5@from-medium">
                            <div class="c-cta_section">
                                <div class="c-cta_content_text" data-scroll data-scroll-offset="100">
                                    <h3>Check out Locomotive Scroll v3</h3>
                                    <p>
                                        This library has evolved considerably over the years. The architecture and conventions shift according to our projects.
                                    </p>
                                    <p>
                                        Visit the GitHub repository page for a complete introduction and list of available options. Search the GitHub issue tracker carefully to check if your issue/feature has already been reported/requested before opening a new issue or submitting a pull request.
                                    </p>
                                </div>
                                <a class="c-cta_button o-button" href="https://github.com/locomotivemtl/locomotive-scroll" target="_blank" data-scroll data-scroll-offset="100">
                                    <span class="o-button_icon">
                                        <svg role="img"><use xlink:href="dist/images/sprite.svg#github"></use></svg>
                                    </span>
                                    Check on Github
                                    <span class="o-button_arrow u-icon">
                                        →
                                    </span>
                                </a>
                            </div>
                            <hr class="c-cta_line -margin" data-scroll data-scroll-offset="100"/>
                            <div class="c-cta_section">
                                <div class="c-cta_content_text" data-scroll data-scroll-offset="100">
                                    <h4>Neue Montreal <br>Pangram Pangram® Foundry</h4>
                                    <p>
                                        You like the font used on this page? Well this is your lucky day. You can get it for free on <a class="o-link -underline" href="https://pangrampangram.com/" target="_blank">pangrampangram.com</a>! Thanks to our good friend Mathieu Desjardins ❤️
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section data-scroll-section>
        <div class="c-choochoo">
            <div class="c-choochoo_item u-text-center" data-scroll data-scroll-direction="horizontal" data-scroll-speed="10">
                <span>
                    🚂
                </span>
            </div>
            <div class="c-choochoo_item u-text-center -reverse" data-scroll data-scroll-direction="horizontal" data-scroll-speed="-10">
                <span>
                    🚂
                </span>
            </div>
        </div>
    </section>

    <section data-scroll-section>
        <div class="o-container">
            <div class="c-damn">
                <h1 class="o-title" data-scroll>
                    <span class="o-title_line">
                        <span>
                            Damn
                        </span>
                    </span>
                    <span class="o-title_line">
                        <span>
                            You really
                        </span>
                    </span>
                    <span class="o-title_line">
                        <span>
                            like to
                        </span>
                    </span>
                    <span class="o-title_line u-white">
                        <span>
                            scroll
                        </span>
                    </span>
                </h1>
            </div>
        </div>
    </section>

  </div>


</template>

<script>
// import { gsap } from 'gsap';
import { ScrollTrigger } from "gsap/ScrollTrigger";
import LocomotiveScroll from 'locomotive-scroll';

export default {
  components: {

  },

  data() {
    return {

    }
  },

  methods: {
  }, 
  mounted : function () {
    !(function() {
  "use strict";
  function s(t, e) {
    if (!(t instanceof e))
      throw new TypeError("Cannot call a class as a function");
  }
  function n(t, e) {
    for (var i = 0; i < e.length; i++) {
      var s = e[i];
      (s.enumerable = s.enumerable || !1),
        (s.configurable = !0),
        "value" in s && (s.writable = !0),
        Object.defineProperty(t, s.key, s);
    }
  }
  function l(t, e, i) {
    return e && n(t.prototype, e), i && n(t, i), t;
  }
  function i(e, t) {
    var i = Object.keys(e);
    if (Object.getOwnPropertySymbols) {
      var s = Object.getOwnPropertySymbols(e);
      t &&
        (s = s.filter(function(t) {
          return Object.getOwnPropertyDescriptor(e, t).enumerable;
        })),
        i.push.apply(i, s);
    }
    return i;
  }
  function e(t, e) {
    if ("function" != typeof e && null !== e)
      throw new TypeError("Super expression must either be null or a function");
    (t.prototype = Object.create(e && e.prototype, {
      constructor: { value: t, writable: !0, configurable: !0 }
    })),
      e && a(t, e);
  }
  function o(t) {
    return (o = Object.setPrototypeOf
      ? Object.getPrototypeOf
      : function(t) {
          return t.__proto__ || Object.getPrototypeOf(t);
        })(t);
  }
  function a(t, e) {
    return (a =
      Object.setPrototypeOf ||
      function(t, e) {
        return (t.__proto__ = e), t;
      })(t, e);
  }
  function r(t) {
    if (void 0 === t)
      throw new ReferenceError(
        "this hasn't been initialised - super() hasn't been called"
      );
    return t;
  }
  function c(t, e) {
    return !e || ("object" != typeof e && "function" != typeof e) ? r(t) : e;
  }
  function h(t, e, i) {
    return (h =
      "undefined" != typeof Reflect && Reflect.get
        ? Reflect.get
        : function(t, e, i) {
            var s = (function(t, e) {
              for (
                ;
                !Object.prototype.hasOwnProperty.call(t, e) &&
                null !== (t = o(t));

              );
              return t;
            })(t, e);
            if (s) {
              var n = Object.getOwnPropertyDescriptor(s, e);
              return n.get ? n.get.call(i) : n.value;
            }
          })(t, e, i || t);
  }
  var u = {
      el: document,
      elMobile: document,
      name: "scroll",
      offset: 0,
      repeat: !1,
      smooth: !1,
      smoothMobile: !1,
      direction: "vertical",
      inertia: 1,
      class: "is-inview",
      scrollbarClass: "c-scrollbar",
      scrollingClass: "has-scroll-scrolling",
      draggingClass: "has-scroll-dragging",
      smoothClass: "has-scroll-smooth",
      initClass: "has-scroll-init",
      getSpeed: !1,
      getDirection: !1,
      firefoxMultiplier: 50,
      touchMultiplier: 2
    },
    d = (function() {
      function e() {
        var t =
          0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {};
        s(this, e),
          window.scrollTo(0, 0),
          Object.assign(this, u, t),
          (this.namespace = "locomotive"),
          (this.html = document.documentElement),
          (this.windowHeight = window.innerHeight),
          (this.windowMiddle = this.windowHeight / 2),
          (this.els = []),
          (this.listeners = {}),
          (this.hasScrollTicking = !1),
          (this.hasCallEventSet = !1),
          (this.checkScroll = this.checkScroll.bind(this)),
          (this.checkResize = this.checkResize.bind(this)),
          (this.checkEvent = this.checkEvent.bind(this)),
          (this.instance = {
            scroll: { x: 0, y: 0 },
            limit: this.html.offsetHeight
          }),
          this.getDirection && (this.instance.direction = null),
          this.getDirection && (this.instance.speed = 0),
          this.html.classList.add(this.initClass),
          window.addEventListener("resize", this.checkResize, !1);
      }
      return (
        l(e, [
          {
            key: "init",
            value: function() {
              this.initEvents();
            }
          },
          {
            key: "checkScroll",
            value: function() {
              this.dispatchScroll();
            }
          },
          { key: "checkResize", value: function() {} },
          {
            key: "initEvents",
            value: function() {
              var e = this;
              (this.scrollToEls = this.el.querySelectorAll(
                "[data-".concat(this.name, "-to]")
              )),
                (this.setScrollTo = this.setScrollTo.bind(this)),
                this.scrollToEls.forEach(function(t) {
                  t.addEventListener("click", e.setScrollTo, !1);
                });
            }
          },
          {
            key: "setScrollTo",
            value: function(t) {
              t.preventDefault(),
                this.scrollTo(
                  t.currentTarget.getAttribute(
                    "data-".concat(this.name, "-href")
                  ) || t.currentTarget.getAttribute("href"),
                  t.currentTarget.getAttribute(
                    "data-".concat(this.name, "-offset")
                  )
                );
            }
          },
          { key: "addElements", value: function() {} },
          {
            key: "detectElements",
            value: function(i) {
              var s = this,
                n = this.instance.scroll.y,
                l = n + this.windowHeight;
              this.els.forEach(function(t, e) {
                !t ||
                  (t.inView && !i) ||
                  (l >= t.top && n < t.bottom && s.setInView(t, e)),
                  t &&
                    t.inView &&
                    (l < t.top || n > t.bottom) &&
                    s.setOutOfView(t, e);
              }),
                (this.els = this.els.filter(function(t, e) {
                  return null !== t;
                })),
                (this.hasScrollTicking = !1);
            }
          },
          {
            key: "setInView",
            value: function(t, e) {
              (this.els[e].inView = !0),
                t.el.classList.add(t.class),
                t.call &&
                  this.hasCallEventSet &&
                  (this.dispatchCall(t, "enter"),
                  t.repeat || (this.els[e].call = !1)),
                t.repeat ||
                  t.speed ||
                  t.sticky ||
                  ((!t.call || (t.call && this.hasCallEventSet)) &&
                    (this.els[e] = null));
            }
          },
          {
            key: "setOutOfView",
            value: function(t, e) {
              (t.repeat || void 0 !== t.speed) && (this.els[e].inView = !1),
                t.call && this.hasCallEventSet && this.dispatchCall(t, "exit"),
                t.repeat && t.el.classList.remove(t.class);
            }
          },
          {
            key: "dispatchCall",
            value: function(t, e) {
              (this.callWay = e),
                (this.callValue = t.call.split(",").map(function(t) {
                  return t.trim();
                })),
                (this.callObj = t),
                1 == this.callValue.length &&
                  (this.callValue = this.callValue[0]);
              var i = new Event(this.namespace + "call");
              this.el.dispatchEvent(i);
            }
          },
          {
            key: "dispatchScroll",
            value: function() {
              var t = new Event(this.namespace + "scroll");
              this.el.dispatchEvent(t);
            }
          },
          {
            key: "setEvents",
            value: function(t, e) {
              this.listeners[t] || (this.listeners[t] = []);
              var i = this.listeners[t];
              i.push(e),
                1 === i.length &&
                  this.el.addEventListener(
                    this.namespace + t,
                    this.checkEvent,
                    !1
                  ),
                "call" === t &&
                  ((this.hasCallEventSet = !0), this.detectElements(!0));
            }
          },
          {
            key: "unsetEvents",
            value: function(t, e) {
              if (this.listeners[t]) {
                var i = this.listeners[t],
                  s = i.indexOf(e);
                s < 0 ||
                  (i.splice(s, 1),
                  0 === i.index &&
                    this.el.removeEventListener(
                      this.namespace + t,
                      this.checkEvent,
                      !1
                    ));
              }
            }
          },
          {
            key: "checkEvent",
            value: function(t) {
              var e = this,
                i = t.type.replace(this.namespace, ""),
                s = this.listeners[i];
              s &&
                0 !== s.length &&
                s.forEach(function(t) {
                  switch (i) {
                    case "scroll":
                      return t(e.instance);
                    case "call":
                      return t(e.callValue, e.callWay, e.callObj);
                    default:
                      return t();
                  }
                });
            }
          },
          { key: "startScroll", value: function() {} },
          { key: "stopScroll", value: function() {} },
          {
            key: "setScroll",
            value: function(t, e) {
              this.instance.scroll = { x: 0, y: 0 };
            }
          },
          {
            key: "destroy",
            value: function() {
              var e = this;
              window.removeEventListener("resize", this.checkResize, !1),
                Object.keys(this.listeners).forEach(function(t) {
                  e.el.removeEventListener(e.namespace + t, e.checkEvent, !1);
                }),
                (this.listeners = {}),
                this.scrollToEls.forEach(function(t) {
                  t.removeEventListener("click", e.setScrollTo, !1);
                });
            }
          }
        ]),
        e
      );
    })(),
    t = (function(t) {
      function i() {
        var t,
          e =
            0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {};
        return (
          s(this, i),
          (t = c(this, o(i).call(this, e))),
          window.addEventListener("scroll", t.checkScroll, !1),
          t
        );
      }
      return (
        e(i, d),
        l(i, [
          {
            key: "init",
            value: function() {
              (this.instance.scroll.y = window.pageYOffset),
                this.addElements(),
                this.detectElements(),
                h(o(i.prototype), "init", this).call(this);
            }
          },
          {
            key: "checkScroll",
            value: function() {
              var t = this;
              h(o(i.prototype), "checkScroll", this).call(this),
                (this.instance.scroll.y = window.pageYOffset),
                this.els.length &&
                  (this.hasScrollTicking ||
                    (requestAnimationFrame(function() {
                      t.detectElements();
                    }),
                    (this.hasScrollTicking = !0)));
            }
          },
          {
            key: "checkResize",
            value: function() {
              var t = this;
              this.els.length &&
                ((this.windowHeight = window.innerHeight),
                this.hasScrollTicking ||
                  (requestAnimationFrame(function() {
                    t.updateElements();
                  }),
                  (this.hasScrollTicking = !0)));
            }
          },
          {
            key: "addElements",
            value: function() {
              var c = this;
              (this.els = []),
                this.el
                  .querySelectorAll("[data-" + this.name + "]")
                  .forEach(function(t, e) {
                    var i = t.dataset[c.name + "Class"] || c.class,
                      s = t.getBoundingClientRect().top + c.instance.scroll.y,
                      n = s + t.offsetHeight,
                      l =
                        parseInt(t.dataset[c.name + "Offset"]) ||
                        parseInt(c.offset),
                      o = t.dataset[c.name + "Repeat"],
                      a = t.dataset[c.name + "Call"],
                      r = {
                        el: t,
                        id: e,
                        class: i,
                        top: s + l,
                        bottom: n,
                        offset: l,
                        repeat: (o = "false" != o && (null != o || c.repeat)),
                        inView: !1,
                        call: a
                      };
                    c.els.push(r);
                  });
            }
          },
          {
            key: "updateElements",
            value: function() {
              var n = this;
              this.els.forEach(function(t, e) {
                var i = t.el.getBoundingClientRect().top + n.instance.scroll.y,
                  s = i + t.el.offsetHeight;
                (n.els[e].top = i + t.offset), (n.els[e].bottom = s);
              }),
                (this.hasScrollTicking = !1);
            }
          },
          {
            key: "scrollTo",
            value: function(t, e) {
              var i,
                s = e ? parseInt(e) : 0;
              "string" == typeof t
                ? "top" === t
                  ? (i = this.html)
                  : "bottom" === t
                  ? (s = this.html.offsetHeight - window.innerHeight)
                  : (i = document.querySelectorAll(t)[0])
                : t.target || (i = t),
                i && (s = i.getBoundingClientRect().top + s),
                (s += this.instance.scroll.y),
                window.scrollTo({ top: s, behavior: "smooth" });
            }
          },
          {
            key: "update",
            value: function() {
              this.addElements(), this.detectElements();
            }
          },
          {
            key: "destroy",
            value: function() {
              h(o(i.prototype), "destroy", this).call(this),
                window.removeEventListener("scroll", this.checkScroll, !1);
            }
          }
        ]),
        i
      );
    })(),
    f = Object.getOwnPropertySymbols,
    p = Object.prototype.hasOwnProperty,
    y = Object.prototype.propertyIsEnumerable;
  var m = (function() {
    try {
      if (!Object.assign) return !1;
      var t = new String("abc");
      if (((t[5] = "de"), "5" === Object.getOwnPropertyNames(t)[0])) return !1;
      for (var e = {}, i = 0; i < 10; i++) e["_" + String.fromCharCode(i)] = i;
      if (
        "0123456789" !==
        Object.getOwnPropertyNames(e)
          .map(function(t) {
            return e[t];
          })
          .join("")
      )
        return !1;
      var s = {};
      return (
        "abcdefghijklmnopqrst".split("").forEach(function(t) {
          s[t] = t;
        }),
        "abcdefghijklmnopqrst" === Object.keys(Object.assign({}, s)).join("")
      );
    } catch (t) {
      return !1;
    }
  })()
    ? Object.assign
    : function(t, e) {
        for (
          var i,
            s,
            n = (function(t) {
              if (null == t)
                throw new TypeError(
                  "Object.assign cannot be called with null or undefined"
                );
              return Object(t);
            })(t),
            l = 1;
          l < arguments.length;
          l++
        ) {
          for (var o in (i = Object(arguments[l])))
            p.call(i, o) && (n[o] = i[o]);
          if (f) {
            s = f(i);
            for (var a = 0; a < s.length; a++)
              y.call(i, s[a]) && (n[s[a]] = i[s[a]]);
          }
        }
        return n;
      };
  function v() {}
  v.prototype = {
    on: function(t, e, i) {
      var s = this.e || (this.e = {});
      return (s[t] || (s[t] = [])).push({ fn: e, ctx: i }), this;
    },
    once: function(t, e, i) {
      var s = this;
      function n() {
        s.off(t, n), e.apply(i, arguments);
      }
      return (n._ = e), this.on(t, n, i);
    },
    emit: function(t) {
      for (
        var e = [].slice.call(arguments, 1),
          i = ((this.e || (this.e = {}))[t] || []).slice(),
          s = 0,
          n = i.length;
        s < n;
        s++
      )
        i[s].fn.apply(i[s].ctx, e);
      return this;
    },
    off: function(t, e) {
      var i = this.e || (this.e = {}),
        s = i[t],
        n = [];
      if (s && e)
        for (var l = 0, o = s.length; l < o; l++)
          s[l].fn !== e && s[l].fn._ !== e && n.push(s[l]);
      return n.length ? (i[t] = n) : delete i[t], this;
    }
  };
  var g = v,
    w =
      "undefined" != typeof globalThis
        ? globalThis
        : "undefined" != typeof window
        ? window
        : "undefined" != typeof global
        ? global
        : "undefined" != typeof self
        ? self
        : {};
  var b,
    k =
      ((function(t, e) {
        (function() {
          (null !== e ? e : this).Lethargy = (function() {
            function t(t, e, i, s) {
              (this.stability = null != t ? Math.abs(t) : 8),
                (this.sensitivity = null != e ? 1 + Math.abs(e) : 100),
                (this.tolerance = null != i ? 1 + Math.abs(i) : 1.1),
                (this.delay = null != s ? s : 150),
                (this.lastUpDeltas = function() {
                  var t, e, i;
                  for (
                    i = [], t = 1, e = 2 * this.stability;
                    1 <= e ? t <= e : e <= t;
                    1 <= e ? t++ : t--
                  )
                    i.push(null);
                  return i;
                }.call(this)),
                (this.lastDownDeltas = function() {
                  var t, e, i;
                  for (
                    i = [], t = 1, e = 2 * this.stability;
                    1 <= e ? t <= e : e <= t;
                    1 <= e ? t++ : t--
                  )
                    i.push(null);
                  return i;
                }.call(this)),
                (this.deltasTimestamp = function() {
                  var t, e, i;
                  for (
                    i = [], t = 1, e = 2 * this.stability;
                    1 <= e ? t <= e : e <= t;
                    1 <= e ? t++ : t--
                  )
                    i.push(null);
                  return i;
                }.call(this));
            }
            return (
              (t.prototype.check = function(t) {
                var e;
                return (
                  null != (t = t.originalEvent || t).wheelDelta
                    ? (e = t.wheelDelta)
                    : null != t.deltaY
                    ? (e = -40 * t.deltaY)
                    : (null == t.detail && 0 !== t.detail) ||
                      (e = -40 * t.detail),
                  this.deltasTimestamp.push(Date.now()),
                  this.deltasTimestamp.shift(),
                  0 < e
                    ? (this.lastUpDeltas.push(e),
                      this.lastUpDeltas.shift(),
                      this.isInertia(1))
                    : (this.lastDownDeltas.push(e),
                      this.lastDownDeltas.shift(),
                      this.isInertia(-1))
                );
              }),
              (t.prototype.isInertia = function(t) {
                var e, i, s, n, l, o, a;
                return null ===
                  (e = -1 === t ? this.lastDownDeltas : this.lastUpDeltas)[0]
                  ? t
                  : !(
                      this.deltasTimestamp[2 * this.stability - 2] +
                        this.delay >
                        Date.now() && e[0] === e[2 * this.stability - 1]
                    ) &&
                      ((s = e.slice(0, this.stability)),
                      (i = e.slice(this.stability, 2 * this.stability)),
                      (a = s.reduce(function(t, e) {
                        return t + e;
                      })),
                      (l = i.reduce(function(t, e) {
                        return t + e;
                      })),
                      (o = a / s.length),
                      (n = l / i.length),
                      Math.abs(o) < Math.abs(n * this.tolerance) &&
                        this.sensitivity < Math.abs(n) &&
                        t);
              }),
              (t.prototype.showLastUpDeltas = function() {
                return this.lastUpDeltas;
              }),
              (t.prototype.showLastDownDeltas = function() {
                return this.lastDownDeltas;
              }),
              t
            );
          })();
        }.call(w));
      })((b = { exports: {} }), b.exports),
      b.exports),
    S = {
      hasWheelEvent: "onwheel" in document,
      hasMouseWheelEvent: "onmousewheel" in document,
      hasTouch: "ontouchstart" in document,
      hasTouchWin: navigator.msMaxTouchPoints && 1 < navigator.msMaxTouchPoints,
      hasPointer: !!window.navigator.msPointerEnabled,
      hasKeyDown: "onkeydown" in document,
      isFirefox: -1 < navigator.userAgent.indexOf("Firefox")
    },
    E = Object.prototype.toString,
    T = Object.prototype.hasOwnProperty;
  function O(t, e) {
    return function() {
      return t.apply(e, arguments);
    };
  }
  var D = k.Lethargy,
    _ = "virtualscroll",
    L = B,
    M = 37,
    C = 38,
    H = 39,
    x = 40,
    j = 32;
  function B(t) {
    !(function(t) {
      if (!t) return console.warn("bindAll requires at least one argument.");
      var e = Array.prototype.slice.call(arguments, 1);
      if (0 === e.length)
        for (var i in t)
          T.call(t, i) &&
            "function" == typeof t[i] &&
            "[object Function]" == E.call(t[i]) &&
            e.push(i);
      for (var s = 0; s < e.length; s++) {
        var n = e[s];
        t[n] = O(t[n], t);
      }
    })(
      this,
      "_onWheel",
      "_onMouseWheel",
      "_onTouchStart",
      "_onTouchMove",
      "_onKeyDown"
    ),
      (this.el = window),
      t && t.el && ((this.el = t.el), delete t.el),
      (this.options = m(
        {
          mouseMultiplier: 1,
          touchMultiplier: 2,
          firefoxMultiplier: 15,
          keyStep: 120,
          preventTouch: !1,
          unpreventTouchClass: "vs-touchmove-allowed",
          limitInertia: !1,
          useKeyboard: !0,
          useTouch: !0
        },
        t
      )),
      this.options.limitInertia && (this._lethargy = new D()),
      (this._emitter = new g()),
      (this._event = { y: 0, x: 0, deltaX: 0, deltaY: 0 }),
      (this.touchStartX = null),
      (this.touchStartY = null),
      (this.bodyTouchAction = null),
      void 0 !== this.options.passive &&
        (this.listenerOptions = { passive: this.options.passive });
  }
  function P(t, e, i) {
    return (1 - i) * t + i * e;
  }
  function Y(t) {
    var e = {};
    if (window.getComputedStyle) {
      var i = getComputedStyle(t),
        s = i.transform || i.webkitTransform || i.mozTransform,
        n = s.match(/^matrix3d\((.+)\)$/);
      return n
        ? parseFloat(n[1].split(", ")[13])
        : ((n = s.match(/^matrix\((.+)\)$/)),
          (e.x = n ? parseFloat(n[1].split(", ")[4]) : 0),
          (e.y = n ? parseFloat(n[1].split(", ")[5]) : 0),
          e);
    }
  }
  (B.prototype._notify = function(t) {
    var e = this._event;
    (e.x += e.deltaX),
      (e.y += e.deltaY),
      this._emitter.emit(_, {
        x: e.x,
        y: e.y,
        deltaX: e.deltaX,
        deltaY: e.deltaY,
        originalEvent: t
      });
  }),
    (B.prototype._onWheel = function(t) {
      var e = this.options;
      if (!this._lethargy || !1 !== this._lethargy.check(t)) {
        var i = this._event;
        (i.deltaX = t.wheelDeltaX || -1 * t.deltaX),
          (i.deltaY = t.wheelDeltaY || -1 * t.deltaY),
          S.isFirefox &&
            1 == t.deltaMode &&
            ((i.deltaX *= e.firefoxMultiplier),
            (i.deltaY *= e.firefoxMultiplier)),
          (i.deltaX *= e.mouseMultiplier),
          (i.deltaY *= e.mouseMultiplier),
          this._notify(t);
      }
    }),
    (B.prototype._onMouseWheel = function(t) {
      if (!this.options.limitInertia || !1 !== this._lethargy.check(t)) {
        var e = this._event;
        (e.deltaX = t.wheelDeltaX ? t.wheelDeltaX : 0),
          (e.deltaY = t.wheelDeltaY ? t.wheelDeltaY : t.wheelDelta),
          this._notify(t);
      }
    }),
    (B.prototype._onTouchStart = function(t) {
      var e = t.targetTouches ? t.targetTouches[0] : t;
      (this.touchStartX = e.pageX), (this.touchStartY = e.pageY);
    }),
    (B.prototype._onTouchMove = function(t) {
      var e = this.options;
      e.preventTouch &&
        !t.target.classList.contains(e.unpreventTouchClass) &&
        t.preventDefault();
      var i = this._event,
        s = t.targetTouches ? t.targetTouches[0] : t;
      (i.deltaX = (s.pageX - this.touchStartX) * e.touchMultiplier),
        (i.deltaY = (s.pageY - this.touchStartY) * e.touchMultiplier),
        (this.touchStartX = s.pageX),
        (this.touchStartY = s.pageY),
        this._notify(t);
    }),
    (B.prototype._onKeyDown = function(t) {
      var e = this._event;
      e.deltaX = e.deltaY = 0;
      var i = window.innerHeight - 40;
      switch (t.keyCode) {
        case M:
        case C:
          e.deltaY = this.options.keyStep;
          break;
        case H:
        case x:
          e.deltaY = -this.options.keyStep;
          break;
        case t.shiftKey:
          e.deltaY = i;
          break;
        case j:
          e.deltaY = -i;
          break;
        default:
          return;
      }
      this._notify(t);
    }),
    (B.prototype._bind = function() {
      S.hasWheelEvent &&
        this.el.addEventListener("wheel", this._onWheel, this.listenerOptions),
        S.hasMouseWheelEvent &&
          this.el.addEventListener(
            "mousewheel",
            this._onMouseWheel,
            this.listenerOptions
          ),
        S.hasTouch &&
          this.options.useTouch &&
          (this.el.addEventListener(
            "touchstart",
            this._onTouchStart,
            this.listenerOptions
          ),
          this.el.addEventListener(
            "touchmove",
            this._onTouchMove,
            this.listenerOptions
          )),
        S.hasPointer &&
          S.hasTouchWin &&
          ((this.bodyTouchAction = document.body.style.msTouchAction),
          (document.body.style.msTouchAction = "none"),
          this.el.addEventListener("MSPointerDown", this._onTouchStart, !0),
          this.el.addEventListener("MSPointerMove", this._onTouchMove, !0)),
        S.hasKeyDown &&
          this.options.useKeyboard &&
          document.addEventListener("keydown", this._onKeyDown);
    }),
    (B.prototype._unbind = function() {
      S.hasWheelEvent && this.el.removeEventListener("wheel", this._onWheel),
        S.hasMouseWheelEvent &&
          this.el.removeEventListener("mousewheel", this._onMouseWheel),
        S.hasTouch &&
          (this.el.removeEventListener("touchstart", this._onTouchStart),
          this.el.removeEventListener("touchmove", this._onTouchMove)),
        S.hasPointer &&
          S.hasTouchWin &&
          ((document.body.style.msTouchAction = this.bodyTouchAction),
          this.el.removeEventListener("MSPointerDown", this._onTouchStart, !0),
          this.el.removeEventListener("MSPointerMove", this._onTouchMove, !0)),
        S.hasKeyDown &&
          this.options.useKeyboard &&
          document.removeEventListener("keydown", this._onKeyDown);
    }),
    (B.prototype.on = function(t, e) {
      this._emitter.on(_, t, e);
      var i = this._emitter.e;
      i && i[_] && 1 === i[_].length && this._bind();
    }),
    (B.prototype.off = function(t, e) {
      this._emitter.off(_, t, e);
      var i = this._emitter.e;
      (!i[_] || i[_].length <= 0) && this._unbind();
    }),
    (B.prototype.reset = function() {
      var t = this._event;
      (t.x = 0), (t.y = 0);
    }),
    (B.prototype.destroy = function() {
      this._emitter.off(), this._unbind();
    });
  var R = 38,
    A = 40,
    V = 32,
    X = 9,
    W = 33,
    K = 34,
    I = 36,
    q = 35,
    F = (function(t) {
      function n() {
        var t,
          e =
            0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {};
        return (
          s(this, n),
          ((t = c(this, o(n).call(this, e))).inertia = 0.1 * t.inertia),
          (t.isScrolling = !1),
          (t.isDraggingScrollbar = !1),
          (t.isTicking = !1),
          (t.hasScrollTicking = !1),
          (t.parallaxElements = []),
          (t.inertiaRatio = 1),
          (t.stop = !1),
          (t.checkKey = t.checkKey.bind(r(t))),
          window.addEventListener("keydown", t.checkKey, !1),
          t
        );
      }
      return (
        e(n, d),
        l(n, [
          {
            key: "init",
            value: function() {
              var e = this;
              this.html.classList.add(this.smoothClass),
                (this.instance = (function(n) {
                  for (var t = 1; t < arguments.length; t++) {
                    var l = null != arguments[t] ? arguments[t] : {};
                    t % 2
                      ? i(l, !0).forEach(function(t) {
                          var e, i, s;
                          (e = n),
                            (s = l[(i = t)]),
                            i in e
                              ? Object.defineProperty(e, i, {
                                  value: s,
                                  enumerable: !0,
                                  configurable: !0,
                                  writable: !0
                                })
                              : (e[i] = s);
                        })
                      : Object.getOwnPropertyDescriptors
                      ? Object.defineProperties(
                          n,
                          Object.getOwnPropertyDescriptors(l)
                        )
                      : i(l).forEach(function(t) {
                          Object.defineProperty(
                            n,
                            t,
                            Object.getOwnPropertyDescriptor(l, t)
                          );
                        });
                  }
                  return n;
                })({ delta: { x: 0, y: 0 } }, this.instance)),
                (this.vs = new L({
                  el: this.el,
                  mouseMultiplier:
                    -1 < navigator.platform.indexOf("Win") ? 1 : 0.4,
                  firefoxMultiplier: this.firefoxMultiplier,
                  touchMultiplier: this.touchMultiplier,
                  useKeyboard: !1,
                  passive: !0
                })),
                this.vs.on(function(t) {
                  e.stop ||
                    (e.isTicking ||
                      e.isDraggingScrollbar ||
                      (requestAnimationFrame(function() {
                        e.isScrolling || e.startScrolling(), e.updateDelta(t);
                      }),
                      (e.isTicking = !0)),
                    (e.isTicking = !1));
                }),
                this.setScrollLimit(),
                this.initScrollBar(),
                this.addSections(),
                this.addElements(),
                this.detectElements(),
                this.transformElements(!0),
                h(o(n.prototype), "init", this).call(this);
            }
          },
          {
            key: "setScrollLimit",
            value: function() {
              this.instance.limit = this.el.offsetHeight - this.windowHeight;
            }
          },
          {
            key: "startScrolling",
            value: function() {
              (this.isScrolling = !0),
                this.checkScroll(),
                this.html.classList.add(this.scrollingClass);
            }
          },
          {
            key: "stopScrolling",
            value: function() {
              (this.isScrolling = !1),
                (this.inertiaRatio = 1),
                (this.instance.scroll.y = Math.round(this.instance.scroll.y)),
                this.html.classList.remove(this.scrollingClass);
            }
          },
          {
            key: "checkKey",
            value: function(t) {
              var e = this;
              switch (t.keyCode) {
                case X:
                  setTimeout(function() {
                    (document.documentElement.scrollTop = 0),
                      (document.body.scrollTop = 0),
                      document.activeElement instanceof HTMLBodyElement ||
                        e.scrollTo(
                          document.activeElement,
                          -window.innerHeight / 2
                        );
                  }, 0);
                  break;
                case R:
                  this.instance.delta.y -= 240;
                  break;
                case A:
                  this.instance.delta.y += 240;
                  break;
                case W:
                  this.instance.delta.y -= window.innerHeight;
                  break;
                case K:
                  this.instance.delta.y += window.innerHeight;
                  break;
                case I:
                  this.instance.delta.y -= this.instance.limit;
                  break;
                case q:
                  this.instance.delta.y += this.instance.limit;
                  break;
                case V:
                  document.activeElement instanceof HTMLInputElement ||
                    document.activeElement instanceof HTMLTextAreaElement ||
                    (t.shiftKey
                      ? (this.instance.delta.y -= window.innerHeight)
                      : (this.instance.delta.y += window.innerHeight));
                  break;
                default:
                  return;
              }
              this.instance.delta.y < 0 && (this.instance.delta.y = 0),
                this.instance.delta.y > this.instance.limit &&
                  (this.instance.delta.y = this.instance.limit),
                (this.isScrolling = !0),
                this.checkScroll(),
                this.html.classList.add(this.scrollingClass);
            }
          },
          {
            key: "checkScroll",
            value: function() {
              var t = this;
              if (this.isScrolling || this.isDraggingScrollbar) {
                this.hasScrollTicking ||
                  (requestAnimationFrame(function() {
                    return t.checkScroll();
                  }),
                  (this.hasScrollTicking = !0));
                var e = Math.abs(
                  this.instance.delta.y - this.instance.scroll.y
                );
                ((e < 0.5 && 0 != this.instance.delta.y) ||
                  (e < 0.5 && 0 == this.instance.delta.y)) &&
                  this.stopScrolling(),
                  this.updateScroll();
                for (var i = this.sections.length - 1; 0 <= i; i--)
                  this.sections[i].persistent ||
                  (this.instance.scroll.y > this.sections[i].offset &&
                    this.instance.scroll.y < this.sections[i].limit)
                    ? (this.transform(
                        this.sections[i].el,
                        0,
                        -this.instance.scroll.y
                      ),
                      (this.sections[i].el.style.visibility = "visible"),
                      (this.sections[i].inView = !0))
                    : ((this.sections[i].el.style.visibility = "hidden"),
                      (this.sections[i].inView = !1),
                      this.transform(this.sections[i].el, 0, 0));
                this.getDirection && this.addDirection(),
                  this.getSpeed &&
                    (this.addSpeed(), (this.timestamp = Date.now())),
                  this.detectElements(),
                  this.transformElements();
                var s =
                  (this.instance.scroll.y / this.instance.limit) *
                  this.scrollBarLimit;
                this.transform(this.scrollbarThumb, 0, s),
                  h(o(n.prototype), "checkScroll", this).call(this),
                  (this.hasScrollTicking = !1);
              }
            }
          },
          {
            key: "checkResize",
            value: function() {
              (this.windowHeight = window.innerHeight),
                (this.windowMiddle = this.windowHeight / 2),
                this.update();
            }
          },
          {
            key: "updateDelta",
            value: function(t) {
              (this.instance.delta.y -= t.deltaY),
                this.instance.delta.y < 0 && (this.instance.delta.y = 0),
                this.instance.delta.y > this.instance.limit &&
                  (this.instance.delta.y = this.instance.limit);
            }
          },
          {
            key: "updateScroll",
            value: function(t) {
              this.isScrolling || this.isDraggingScrollbar
                ? (this.instance.scroll.y = P(
                    this.instance.scroll.y,
                    this.instance.delta.y,
                    this.inertia * this.inertiaRatio
                  ))
                : (this.instance.scroll.y = this.instance.delta.y);
            }
          },
          {
            key: "addDirection",
            value: function() {
              this.instance.delta.y > this.instance.scroll.y
                ? "down" !== this.instance.direction &&
                  (this.instance.direction = "down")
                : this.instance.delta.y < this.instance.scroll.y &&
                  "up" !== this.instance.direction &&
                  (this.instance.direction = "up");
            }
          },
          {
            key: "addSpeed",
            value: function() {
              this.instance.delta.y != this.instance.scroll.y
                ? (this.instance.speed =
                    (this.instance.delta.y - this.instance.scroll.y) /
                    (Date.now() - this.timestamp))
                : (this.instance.speed = 0);
            }
          },
          {
            key: "initScrollBar",
            value: function() {
              (this.scrollbar = document.createElement("span")),
                (this.scrollbarThumb = document.createElement("span")),
                this.scrollbar.classList.add("".concat(this.scrollbarClass)),
                this.scrollbarThumb.classList.add(
                  "".concat(this.scrollbarClass, "_thumb")
                ),
                this.scrollbar.append(this.scrollbarThumb),
                document.body.append(this.scrollbar),
                (this.scrollbarHeight = this.scrollbar.getBoundingClientRect().height),
                (this.scrollbarThumb.style.height = "".concat(
                  (this.scrollbarHeight * this.scrollbarHeight) /
                    (this.instance.limit + this.scrollbarHeight),
                  "px"
                )),
                (this.scrollBarLimit =
                  this.scrollbarHeight -
                  this.scrollbarThumb.getBoundingClientRect().height),
                (this.getScrollBar = this.getScrollBar.bind(this)),
                (this.releaseScrollBar = this.releaseScrollBar.bind(this)),
                (this.moveScrollBar = this.moveScrollBar.bind(this)),
                this.scrollbarThumb.addEventListener(
                  "mousedown",
                  this.getScrollBar
                ),
                window.addEventListener("mouseup", this.releaseScrollBar),
                window.addEventListener("mousemove", this.moveScrollBar);
            }
          },
          {
            key: "reinitScrollBar",
            value: function() {
              (this.scrollbarHeight = this.scrollbar.getBoundingClientRect().height),
                (this.scrollbarThumb.style.height = "".concat(
                  (this.scrollbarHeight * this.scrollbarHeight) /
                    this.instance.limit,
                  "px"
                )),
                (this.scrollBarLimit =
                  this.scrollbarHeight -
                  this.scrollbarThumb.getBoundingClientRect().height);
            }
          },
          {
            key: "destroyScrollBar",
            value: function() {
              this.scrollbarThumb.removeEventListener(
                "mousedown",
                this.getScrollBar
              ),
                window.removeEventListener("mouseup", this.releaseScrollBar),
                window.removeEventListener("mousemove", this.moveScrollBar),
                this.scrollbar.remove();
            }
          },
          {
            key: "getScrollBar",
            value: function(t) {
              (this.isDraggingScrollbar = !0),
                this.checkScroll(),
                this.html.classList.remove(this.scrollingClass),
                this.html.classList.add(this.draggingClass);
            }
          },
          {
            key: "releaseScrollBar",
            value: function(t) {
              (this.isDraggingScrollbar = !1),
                this.html.classList.add(this.scrollingClass),
                this.html.classList.remove(this.draggingClass);
            }
          },
          {
            key: "moveScrollBar",
            value: function(e) {
              var i = this;
              !this.isTicking &&
                this.isDraggingScrollbar &&
                (requestAnimationFrame(function() {
                  var t =
                    (((100 * e.clientY) / i.scrollbarHeight) *
                      i.instance.limit) /
                    100;
                  0 < t && t < i.instance.limit && (i.instance.delta.y = t);
                }),
                (this.isTicking = !0)),
                (this.isTicking = !1);
            }
          },
          {
            key: "addElements",
            value: function() {
              var b = this;
              (this.els = []),
                (this.parallaxElements = []),
                this.sections.forEach(function(t, w) {
                  b.sections[w].el
                    .querySelectorAll("[data-".concat(b.name, "]"))
                    .forEach(function(t, e) {
                      var i,
                        s,
                        n = t.dataset[b.name + "Class"] || b.class,
                        l = t.dataset[b.name + "Repeat"],
                        o = t.dataset[b.name + "Call"],
                        a = t.dataset[b.name + "Position"],
                        r = t.dataset[b.name + "Delay"],
                        c = t.dataset[b.name + "Direction"],
                        h = "string" == typeof t.dataset[b.name + "Sticky"],
                        u =
                          !!t.dataset[b.name + "Speed"] &&
                          parseFloat(t.dataset[b.name + "Speed"]) / 10,
                        d =
                          "string" == typeof t.dataset[b.name + "Offset"] &&
                          t.dataset[b.name + "Offset"].split(","),
                        f = t.dataset[b.name + "Target"];
                      s =
                        void 0 !== f ? document.querySelector("".concat(f)) : t;
                      var p =
                          (i = b.sections[w].inView
                            ? s.getBoundingClientRect().top +
                              b.instance.scroll.y -
                              Y(s).y
                            : s.getBoundingClientRect().top -
                              Y(b.sections[w].el).y -
                              Y(s).y) + s.offsetHeight,
                        y = (p - i) / 2 + i;
                      if (h) {
                        var m = t.getBoundingClientRect().top - i;
                        y =
                          ((p =
                            (i += window.innerHeight) +
                            s.offsetHeight -
                            window.innerHeight -
                            t.offsetHeight -
                            m) -
                            i) /
                            2 +
                          i;
                      }
                      l = "false" != l && (null != l || b.repeat);
                      var v = [0, 0];
                      if (d)
                        for (e = 0; e < d.length; e++)
                          d[e].includes("%")
                            ? (v[e] = parseInt(
                                (d[e].replace("%", "") * b.windowHeight) / 100
                              ))
                            : (v[e] = parseInt(d[e]));
                      var g = {
                        el: t,
                        id: e,
                        class: n,
                        top: i + v[0],
                        middle: y,
                        bottom: p - v[1],
                        offset: d,
                        repeat: l,
                        inView: !1,
                        call: o,
                        speed: u,
                        delay: r,
                        position: a,
                        target: s,
                        direction: c,
                        sticky: h
                      };
                      b.els.push(g),
                        (!1 !== u || h) && b.parallaxElements.push(g);
                    });
                });
            }
          },
          {
            key: "addSections",
            value: function() {
              var a = this;
              this.sections = [];
              var t = this.el.querySelectorAll(
                "[data-".concat(this.name, "-section]")
              );
              0 === t.length && (t = [this.el]),
                t.forEach(function(t, e) {
                  var i =
                      t.getBoundingClientRect().top -
                      1.5 * window.innerHeight -
                      Y(t).y,
                    s =
                      i +
                      t.getBoundingClientRect().height +
                      2 * window.innerHeight,
                    n = "string" == typeof t.dataset[a.name + "Persistent"],
                    l = !1;
                  a.instance.scroll.y >= i &&
                    a.instance.scroll.y <= s &&
                    (l = !0);
                  var o = {
                    el: t,
                    offset: i,
                    limit: s,
                    inView: l,
                    persistent: n
                  };
                  a.sections[e] = o;
                });
            }
          },
          {
            key: "transform",
            value: function(t, e, i, s) {
              var n;
              if (s) {
                var l = Y(t),
                  o = P(l.x, e, s),
                  a = P(l.y, i, s);
                n = "matrix3d(1,0,0.00,0,0.00,1,0.00,0,0,0,1,0,"
                  .concat(o, ",")
                  .concat(a, ",0,1)");
              } else
                n = "matrix3d(1,0,0.00,0,0.00,1,0.00,0,0,0,1,0,"
                  .concat(e, ",")
                  .concat(i, ",0,1)");
              (t.style.webkitTransform = n),
                (t.style.msTransform = n),
                (t.style.transform = n);
            }
          },
          {
            key: "transformElements",
            value: function(s) {
              var n = this,
                l = this.instance.scroll.y + this.windowHeight,
                o = this.instance.scroll.y + this.windowMiddle;
              this.parallaxElements.forEach(function(t, e) {
                var i = !1;
                if ((s && (i = 0), t.inView))
                  switch (t.position) {
                    case "top":
                      i = n.instance.scroll.y * -t.speed;
                      break;
                    case "elementTop":
                      i = (l - t.top) * -t.speed;
                      break;
                    case "bottom":
                      i = (n.instance.limit - l + n.windowHeight) * t.speed;
                      break;
                    default:
                      i = (o - t.middle) * -t.speed;
                  }
                t.sticky &&
                  (i = t.inView
                    ? n.instance.scroll.y - t.top + window.innerHeight
                    : n.instance.scroll.y < t.top - window.innerHeight &&
                      n.instance.scroll.y < t.top - window.innerHeight / 2
                    ? 0
                    : n.instance.scroll.y > t.bottom &&
                      n.instance.scroll.y > t.bottom + 100 &&
                      t.bottom - t.top + window.innerHeight),
                  !1 !== i &&
                    ("horizontal" === t.direction
                      ? n.transform(t.el, i, 0, !s && t.delay)
                      : n.transform(t.el, 0, i, !s && t.delay));
              });
            }
          },
          {
            key: "scrollTo",
            value: function(t, e) {
              var i,
                s = this,
                n = e ? parseInt(e) : 0;
              if (
                ("string" == typeof t
                  ? "top" === t
                    ? (n = 0)
                    : "bottom" === t
                    ? (n = this.instance.limit)
                    : (i = document.querySelectorAll(t)[0])
                  : t.target || (i = t),
                i)
              ) {
                var l = i.getBoundingClientRect().top + this.instance.scroll.y,
                  o = (function(t) {
                    for (var e = []; t && t !== document; t = t.parentNode)
                      e.push(t);
                    return e;
                  })(i).find(function(e) {
                    return s.sections.find(function(t) {
                      return t.el == e;
                    });
                  }),
                  a = 0;
                o && (a = Y(o).y), (n = l + n - a);
              }
              (n -= this.instance.scroll.y),
                (this.instance.delta.y = Math.min(n, this.instance.limit)),
                (this.inertiaRatio = Math.min(
                  4e3 /
                    Math.abs(this.instance.delta.y - this.instance.scroll.y),
                  0.8
                )),
                (this.isScrolling = !0),
                this.checkScroll(),
                this.html.classList.add(this.scrollingClass);
            }
          },
          {
            key: "update",
            value: function() {
              this.setScrollLimit(),
                this.addSections(),
                this.addElements(),
                this.detectElements(),
                this.updateScroll(),
                this.transformElements(!0),
                this.reinitScrollBar();
            }
          },
          {
            key: "startScroll",
            value: function() {
              this.stop = !1;
            }
          },
          {
            key: "stopScroll",
            value: function() {
              this.stop = !0;
            }
          },
          {
            key: "setScroll",
            value: function(t, e) {
              this.instance = { scroll: { x: t, y: e }, delta: { x: t, y: e } };
            }
          },
          {
            key: "destroy",
            value: function() {
              h(o(n.prototype), "destroy", this).call(this),
                this.stopScrolling(),
                this.html.classList.remove(this.smoothClass),
                this.vs.destroy(),
                this.destroyScrollBar(),
                window.removeEventListener("keydown", this.checkKey, !1);
            }
          }
        ]),
        n
      );
    })(),
    z = (function() {
      function e() {
        var t =
          0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {};
        s(this, e), (this.options = t), Object.assign(this, u, t), this.init();
      }
      return (
        l(e, [
          {
            key: "init",
            value: function() {
              this.smoothMobile ||
                (this.isMobile =
                  /Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
                    navigator.userAgent
                  ) ||
                  ("MacIntel" === navigator.platform &&
                    1 < navigator.maxTouchPoints)),
                !0 !== this.smooth || this.isMobile
                  ? (this.scroll = new t(this.options))
                  : (this.scroll = new F(this.options)),
                this.scroll.init(),
                window.location.hash &&
                  this.scroll.scrollTo(window.location.hash);
            }
          },
          {
            key: "update",
            value: function() {
              this.scroll.update();
            }
          },
          {
            key: "start",
            value: function() {
              this.scroll.startScroll();
            }
          },
          {
            key: "stop",
            value: function() {
              this.scroll.stopScroll();
            }
          },
          {
            key: "scrollTo",
            value: function(t, e) {
              this.scroll.scrollTo(t, e);
            }
          },
          {
            key: "setScroll",
            value: function(t, e) {
              this.scroll.setScroll(t, e);
            }
          },
          {
            key: "on",
            value: function(t, e) {
              this.scroll.setEvents(t, e);
            }
          },
          {
            key: "off",
            value: function(t, e) {
              this.scroll.unsetEvents(t, e);
            }
          },
          {
            key: "destroy",
            value: function() {
              this.scroll.destroy();
            }
          }
        ]),
        e
      );
    })();
  document.documentElement.classList.add("is-loaded"),
    document.documentElement.classList.remove("is-loading"),
    setTimeout(function() {
      document.documentElement.classList.add("is-ready");
    }, 300),
    setTimeout(function() {
      var i = new z({
          el: document.querySelector("#js-scroll"),
          smooth: !0,
          getSpeed: !0,
          getDirection: !0,
          useKeyboard: !0
        }),
        n = [],
        l = [];
      i.on("scroll", function(t) {
        var e = (360 * t.scroll.y) / t.limit;
        (i.el.style.backgroundColor = "hsl(".concat(e, ", 11%, 81%)")),
          n.forEach(function(t) {
            t.el.style.backgroundColor = "hsl(".concat(e, ", 11%, 81%)");
          }),
          l.forEach(function(t) {
            t.el.style.color = "hsl(".concat(e, ", 11%, 81%)");
          }),
          document.documentElement.setAttribute("data-direction", t.direction);
      }),
        i.on("call", function(t, e, i) {
          if ("dynamicBackground" === t)
            if ("enter" === e) n.push({ id: i.id, el: i.el });
            else
              for (var s = 0; s < n.length; s++)
                i.id === n[s].id && n.splice(s, 1);
          else if ("dynamicColor" === t)
            if ("enter" === e) l.push({ id: i.id, el: i.el });
            else
              for (s = 0; s < l.length; s++) i.id === l[s].id && l.splice(s, 1);
        });
    }, 1e3);
})();


  }
}
</script>


<style scoped>
/*! locomotive-scroll v3.2.8 | MIT License | https://github.com/locomotivemtl/locomotive-scroll */
/*! normalize.css v8.0.1 | MIT License | github.com/necolas/normalize.css */
html {
  line-height: 1.15;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
main {
  display: block;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
hr {
  box-sizing: content-box;
  height: 0;
  overflow: visible;
}
pre {
  font-family: monospace, monospace;
  font-size: 1em;
}
a {
  background-color: transparent;
}
abbr[title] {
  border-bottom: none;
  text-decoration: underline;
  -webkit-text-decoration: underline dotted;
  text-decoration: underline dotted;
}
b,
strong {
  font-weight: bolder;
}
code,
kbd,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sub {
  bottom: -0.25em;
}
sup {
  top: -0.5em;
}
img {
  border-style: none;
}
button,
input,
optgroup,
select,
textarea {
  font-family: inherit;
  font-size: 100%;
  line-height: 1.15;
  margin: 0;
}
button,
input {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
[type="button"],
[type="reset"],
[type="submit"],
button {
  -webkit-appearance: button;
}
[type="button"]::-moz-focus-inner,
[type="reset"]::-moz-focus-inner,
[type="submit"]::-moz-focus-inner,
button::-moz-focus-inner {
  border-style: none;
  padding: 0;
}
[type="button"]:-moz-focusring,
[type="reset"]:-moz-focusring,
[type="submit"]:-moz-focusring,
button:-moz-focusring {
  outline: 1px dotted ButtonText;
}
fieldset {
  padding: 0.35em 0.75em 0.625em;
}
legend {
  box-sizing: border-box;
  color: inherit;
  display: table;
  max-width: 100%;
  padding: 0;
  white-space: normal;
}
progress {
  vertical-align: baseline;
}
[type="checkbox"],
[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
[type="number"]::-webkit-inner-spin-button,
[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
[type="search"] {
  -webkit-appearance: textfield;
  outline-offset: -2px;
}
[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
::-webkit-file-upload-button {
  -webkit-appearance: button;
  font: inherit;
}
details {
  display: block;
}
summary {
  display: list-item;
}
[hidden],
template {
  display: none;
}
html {
  box-sizing: border-box;
}
[hidden],
template {
  display: none;
}
*,
:after,
:before {
  box-sizing: inherit;
}
address {
  font-style: inherit;
}
cite,
dfn,
em,
i {
  font-style: italic;
}
b,
strong {
  font-weight: 700;
}
a {
  text-decoration: none;
}
a svg {
  pointer-events: none;
}
ol,
ul {
  list-style: none;
}
figure,
ol,
p,
ul {
  margin: 0;
  padding: 0;
}
[tabindex],
a,
area,
button,
input,
label,
select,
textarea {
  touch-action: manipulation;
}
[hreflang] > abbr[title] {
  text-decoration: none;
}
table {
  border-spacing: 0;
  border-collapse: collapse;
}
hr {
  display: block;
  margin: 1em 0;
  padding: 0;
  height: 1px;
  border: 0;
  border-top: 1px solid #272727;
}
audio,
canvas,
iframe,
img,
svg,
video {
  vertical-align: middle;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
img,
svg {
  max-width: 100%;
  height: auto;
}
img[height],
img[width],
svg[height],
svg[width] {
  max-width: none;
}
img {
  font-style: italic;
}
svg {
  fill: currentColor;
}
input,
select,
textarea {
  display: block;
  margin: 0;
  padding: 0;
  width: 100%;
  outline: 0;
  border: 0;
  border-radius: 0;
  background: none transparent;
  color: inherit;
  font: inherit;
  line-height: normal;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
}
select {
  text-transform: none;
}
select::-ms-expand {
  display: none;
}
select::-ms-value {
  background: none;
  color: inherit;
}
textarea {
  overflow: auto;
  resize: vertical;
}
.o-button,
button {
  display: inline-block;
  overflow: visible;
  margin: 0;
  padding: 0;
  outline: 0;
  border: 0;
  background: none transparent;
  color: inherit;
  vertical-align: middle;
  text-align: center;
  text-transform: none;
  font: inherit;
  line-height: normal;
  cursor: pointer;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.o-button,
.o-button:focus,
.o-button:hover,
button,
button:focus,
button:hover {
  text-decoration: none;
}
@font-face {
  font-family: Neue Montreal;
  src: url(../fonts/NeueMontreal-Medium.woff2) format("woff2"),
    url(../fonts/NeueMontreal-Medium.woff) format("woff");
  font-weight: 500;
  font-style: normal;
}
html {
  color: #222;
  font-family: Neue Montreal;
  line-height: 1.5;
}
@media (max-width: 699px) {
  html {
    font-size: 12px;
  }
}
@media (min-width: 700px) and (max-width: 999px) {
  html {
    font-size: 13px;
  }
}
@media (min-width: 1000px) and (max-width: 1199px) {
  html {
    font-size: 14px;
  }
}
@media (min-width: 1200px) and (max-width: 1599px) {
  html {
    font-size: 16px;
  }
}
@media (min-width: 1600px) and (max-width: 1999px) {
  html {
    font-size: 18px;
  }
}
@media (min-width: 2000px) and (max-width: 2399px) {
  html {
    font-size: 21px;
  }
}
@media (min-width: 2400px) {
  html {
    font-size: 24px;
  }
}
html:not(.has-scroll-init) {
  cursor: wait;
  overflow: hidden;
}
html.has-scroll-smooth {
  overflow: hidden;
}
html.has-scroll-dragging {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.has-scroll-smooth body {
  overflow: hidden;
}
::-moz-selection {
  background-color: #272727;
  color: #fff;
  text-shadow: none;
}
::selection {
  background-color: #272727;
  color: #fff;
  text-shadow: none;
}
a {
  transition: color 0.3s cubic-bezier(0.215, 0.61, 0.355, 1);
  color: #272727;
}
@media (min-width: 1200px) {
  a:focus,
  a:hover {
    color: #fff;
  }
}
a.-underline {
  text-decoration: underline;
}
.o-h,
.o-h1,
.o-h2,
.o-h3,
.o-h4,
.o-h5,
.o-h6,
h1,
h2,
h3,
h4,
h5,
h6 {
  margin-top: 0;
  line-height: 1.5;
  margin-bottom: 0;
  line-height: 1;
  font-weight: 400;
}
.o-h1,
h1 {
  line-height: 0.9;
  text-transform: uppercase;
}
@media (max-width: 699px) {
  .o-h1,
  h1 {
    font-size: 12vw;
  }
}
@media (min-width: 700px) and (max-width: 1599px) {
  .o-h1,
  h1 {
    font-size: 13.5vw;
  }
}
@media (min-width: 1600px) {
  .o-h1,
  h1 {
    font-size: 12vw;
  }
}
.o-h2,
h2 {
  font-size: 2rem;
}
.o-h3,
h3 {
  font-size: 1.5rem;
}
.o-h4,
h4 {
  line-height: 1.2;
}
.o-h4,
.o-h5,
h4,
h5 {
  font-size: 1rem;
}
.o-h6,
h6 {
  font-size: 0.9375rem;
}
.o-container {
  margin-right: auto;
  margin-left: auto;
  max-width: 95rem;
}
@media (max-width: 699px) {
  .o-container {
    padding-right: 20px;
    padding-left: 20px;
  }
}
@media (min-width: 700px) {
  .o-container {
    padding-right: 2.5rem;
    padding-left: 2.5rem;
  }
}
.o-ratio {
  position: relative;
  display: block;
  overflow: hidden;
}
.o-ratio:before {
  display: block;
  padding-bottom: 100%;
  width: 100%;
  content: "";
}
.o-ratio > embed,
.o-ratio > iframe,
.o-ratio > img,
.o-ratio > object,
.o-ratio_content {
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  width: 100%;
}
.o-layout {
  padding: 0;
  list-style: none;
  font-size: 0;
  margin: 0;
}
.o-layout.-gutter {
  margin-left: -3.75rem;
}
.o-layout.-gutter-small {
  margin-left: -1.875rem;
}
.o-layout.-center {
  text-align: center;
}
.o-layout.-right {
  text-align: right;
}
.o-layout.-reverse {
  direction: rtl;
}
.o-layout.-reverse.-flex {
  flex-direction: row-reverse;
}
.o-layout.-flex {
  display: flex;
}
.o-layout.-flex.-top {
  align-items: flex-start;
}
.o-layout.-flex.-middle {
  align-items: center;
}
.o-layout.-flex.-bottom {
  align-items: flex-end;
}
.o-layout.-stretch {
  align-items: stretch;
}
.o-layout_item {
  display: inline-block;
  width: 100%;
  vertical-align: top;
  font-size: 1rem;
  padding-left: 0;
}
.o-layout.-gutter > .o-layout_item {
  padding-left: 3.75rem;
}
.o-layout.-gutter-small > .o-layout_item {
  padding-left: 1.875rem;
}
.o-layout.-middle > .o-layout_item {
  vertical-align: middle;
}
.o-layout.-bottom > .o-layout_item {
  vertical-align: bottom;
}
.o-layout.-center > .o-layout_item,
.o-layout.-reverse > .o-layout_item,
.o-layout.-right > .o-layout_item {
  text-align: left;
}
.o-layout.-reverse > .o-layout_item {
  direction: ltr;
}
.o-checkbox-label,
.o-label,
.o-radio-label {
  display: block;
  margin-bottom: 0.9375rem;
}
.o-input,
.o-select,
.o-textarea {
  padding: 0.625rem;
  border: 1px solid #d3d3d3;
  background-color: #fff;
}
.o-input:focus,
.o-select:focus,
.o-textarea:focus {
  border-color: grey;
}
.o-input::-webkit-input-placeholder,
.o-select::-webkit-input-placeholder,
.o-textarea::-webkit-input-placeholder {
  color: grey;
}
.o-input::-moz-placeholder,
.o-select::-moz-placeholder,
.o-textarea::-moz-placeholder {
  color: grey;
}
.o-input:-ms-input-placeholder,
.o-select:-ms-input-placeholder,
.o-textarea:-ms-input-placeholder {
  color: grey;
}
.o-input::-ms-input-placeholder,
.o-select::-ms-input-placeholder,
.o-textarea::-ms-input-placeholder {
  color: grey;
}
.o-input::placeholder,
.o-select::placeholder,
.o-textarea::placeholder {
  color: grey;
}
.o-checkbox,
.o-radio {
  position: absolute;
  width: 0;
  opacity: 0;
}
.o-checkbox:focus + .o-checkbox-label:before,
.o-checkbox:focus + .o-radio-label:before,
.o-radio:focus + .o-checkbox-label:before,
.o-radio:focus + .o-radio-label:before {
  border-color: grey;
}
.o-checkbox:checked + .o-checkbox-label:after,
.o-checkbox:checked + .o-radio-label:after,
.o-radio:checked + .o-checkbox-label:after,
.o-radio:checked + .o-radio-label:after {
  opacity: 1;
}
.o-checkbox-label,
.o-radio-label {
  position: relative;
  display: inline-block;
  margin-right: 0.5em;
  padding-left: 1.75rem;
}
.o-checkbox-label:after,
.o-checkbox-label:before,
.o-radio-label:after,
.o-radio-label:before {
  position: absolute;
  top: 50%;
  left: 0;
  display: inline-block;
  margin-top: -0.5625rem;
  padding: 0;
  width: 1.125rem;
  height: 1.125rem;
  content: "";
}
.o-checkbox-label:before,
.o-radio-label:before {
  background-color: #fff;
}
.o-checkbox-label:after,
.o-radio-label:after {
  border-color: transparent;
  background-color: transparent;
  background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='13' height='10.5'%3E%3Cpath fill='%23424242' d='M4.8 5.8L2.4 3.3 0 5.7l4.8 4.8L13 2.4 10.6 0 4.8 5.8z'/%3E%3C/svg%3E");
  background-position: 50%;
  background-size: 0.8125rem;
  background-repeat: no-repeat;
  opacity: 0;
}
.o-radio-label:after,
.o-radio-label:before {
  border-radius: 50%;
}
.o-radio-label:after {
  background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='13' height='13'%3E%3Ccircle fill='%23424242' cx='6.5' cy='6.5' r='6.5'/%3E%3C/svg%3E");
  background-size: 0.5rem;
}
.o-select {
  z-index: 1;
  padding-right: 2.5rem;
}
.o-select,
.o-select-wrap {
  position: relative;
}
.o-select-wrap:after {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  z-index: 2;
  width: 2.5rem;
  background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='13' height='11.3'%3E%3Cpath fill='%23424242' d='M6.5 11.3L3.3 5.6 0 0h13L9.8 5.6z'/%3E%3C/svg%3E");
  background-position: 50%;
  background-size: 0.625rem;
  background-repeat: no-repeat;
  content: "";
  pointer-events: none;
}
.o-textarea {
  min-height: 6.25rem;
}
.o-button {
  position: relative;
  z-index: 1;
  color: #fff;
  padding: 2rem 2.1875rem;
  font-size: 1.5rem;
  background-color: #272727;
  transition: color 0.3s cubic-bezier(0.215, 0.61, 0.355, 1);
  width: 100%;
  text-align: left;
}
.o-button:before {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  z-index: -1;
  transform: scaleY(0);
  transform-origin: center top;
  background-color: #fff;
  transition: transform 0.3s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.o-button:focus,
.o-button:hover {
  color: #272727;
}
.o-button:focus:before,
.o-button:hover:before {
  transform: scaleY(1);
  transform-origin: center bottom;
}
.o-button_icon {
  display: inline-block;
  vertical-align: middle;
  width: 3.4375rem;
  height: 3.4375rem;
  margin-right: 0.9375rem;
}
.o-button_icon svg {
  display: block;
  width: 100%;
  height: 100%;
}
.o-button_arrow {
  position: absolute;
  top: 50%;
  right: 2.1875rem;
  transform: translateY(-50%);
}
.o-scroll {
  box-sizing: border-box;
  overflow: hidden;
  width: 100vw;
  background-color: #d4c9c9;
}
.has-scroll-smooth .o-scroll {
  position: relative;
}
.c-scrollbar {
  width: 10px;
  position: absolute;
  right: 0;
  top: 0;
  height: 100vh;
  transform-origin: center right;
  transform: scaleX(1);
  transition: transform 0.2s linear;
}
.c-scrollbar:hover {
  transform: scaleX(1.3);
  cursor: -webkit-grab;
  cursor: grab;
}
.c-scrollbar_thumb {
  background-color: #000;
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
}
.c-scrollbar_thumb:hover {
  cursor: pointer;
}
.o-title {
  margin: 0;
  padding: 2.5rem 0;
  perspective: 600px;
  -webkit-perspective: 600px;
}
.o-title_line {
  display: block;
  opacity: 0;
  transform-origin: center top;
  transform-style: preserve-3d;
  transform: translateY(100%) rotateX(-80deg);
  transition: opacity 0.8s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 0.8s cubic-bezier(0.215, 0.61, 0.355, 1);
  font-size: 0;
}
.o-title.is-inview .o-title_line {
  transform: none;
  opacity: 1;
}
.o-title.is-inview .o-title_line:first-child {
  transition-delay: 0.4s;
}
.o-title.is-inview .o-title_line:nth-child(2) {
  transition-delay: 0.5s;
}
.o-title.is-inview .o-title_line:nth-child(3) {
  transition-delay: 0.6s;
}
.o-title.is-inview .o-title_line:nth-child(4) {
  transition-delay: 0.7s;
}
.o-title_line span {
  display: inline-block;
  min-width: 0.05em;
  font-size: 13.5vw;
}
.o-image_wrapper {
  position: relative;
  overflow: hidden;
  background-color: #d4c9c9;
}
.o-image {
  opacity: 0.75;
  mix-blend-mode: multiply;
}
.o-image img {
  width: 100%;
  opacity: 0;
  transform: scale(1.4);
  transition: opacity 1.2s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 1.2s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.o-image.is-inview img {
  opacity: 1;
  transform: scale(1);
  transition-delay: 0.6s;
}
.c-header {
  position: relative;
}
@media (max-width: 699px) {
  .c-header {
    height: 50vh;
    min-height: 340px;
  }
}
@media (min-width: 700px) and (max-width: 999px) {
  .c-header {
    height: 80vh;
    min-height: 380px;
  }
}
@media (min-width: 1000px) {
  .c-header {
    height: 100vh;
    min-height: 46.875rem;
  }
}
.c-header_title {
  padding: 2.5rem 0;
  perspective: 600px;
  -webkit-perspective: 600px;
}
.c-header_line,
.c-header_title {
  position: absolute;
  bottom: 0;
  left: 0;
  margin: 0;
}
.c-header_line {
  right: 0;
  transform: scaleX(0);
  transition: transform 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.c-header_line.is-inview {
  transform: scaleX(1);
}
.c-header_title_line {
  display: block;
  opacity: 0;
  transform-origin: center top;
  transform-style: preserve-3d;
  transform: translateY(100%) rotateX(-80deg);
  transition: opacity 0s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 0s cubic-bezier(0.215, 0.61, 0.355, 1);
}
html.is-ready .c-header_title_line {
  transform: none;
  opacity: 1;
  transition-duration: 0.8s;
}
html.is-ready .c-header_title_line:first-child {
  transition-delay: 0.1s;
}
html.is-ready .c-header_title_line:nth-child(2) {
  transition-delay: 0.2s;
}
html.is-ready .c-header_title_line:nth-child(3) {
  transition-delay: 0.3s;
}
html.is-ready .c-header_title_line:nth-child(4) {
  transition-delay: 0.4s;
}
.c-header_title_line span {
  display: inline-block;
}
.c-header_title_line.-version {
  text-transform: none;
  font-size: 0;
}
.c-header_heading {
  padding: 1.875rem 0;
}
.c-header_heading_label {
  display: block;
  transition: transform 0s cubic-bezier(0.215, 0.61, 0.355, 1);
  transform: translateY(-60px);
}
html.is-ready .c-header_heading_label {
  transform: none;
  transition-duration: 0.6s;
}
html.is-ready .o-layout_item:nth-child(2) .c-header_heading_label {
  transition-delay: 0.1s;
}
.c-header_logo {
  position: absolute;
  bottom: 2.5rem;
  right: 0;
  opacity: 0;
  transform: translateY(120px);
  transition: opacity 0s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 0s cubic-bezier(0.215, 0.61, 0.355, 1);
}
@media (max-width: 699px) {
  .c-header_logo {
    width: 30px;
    height: 66px;
  }
}
@media (min-width: 700px) {
  .c-header_logo {
    width: 4rem;
    height: 8.75rem;
  }
}
.c-header_logo svg {
  display: block;
  width: 100%;
  height: 100%;
}
html.is-ready .c-header_logo {
  transform: none;
  opacity: 1;
  transition-delay: 0.6s;
  transition-duration: 0.6s;
}
.c-fixed_wrapper {
  position: relative;
  overflow: hidden;
  background-color: #d4c9c9;
}
@media (min-width: 1000px) {
  .c-fixed_wrapper {
    height: 100vh;
  }
}
@media (max-width: 999px) {
  .c-fixed_wrapper {
    height: 50vh;
  }
}
.c-fixed_target {
  bottom: -100vh;
}
.c-fixed,
.c-fixed_target {
  position: absolute;
  top: -100vh;
  right: 0;
  left: 0;
}
.c-fixed {
  height: 100%;
  background-size: cover;
  background-position: 50%;
  opacity: 0.75;
  mix-blend-mode: multiply;
}
html:not(.has-scroll-smooth) .c-fixed {
  top: 0;
}
.c-intro {
  margin: 7.5rem 0;
  font-size: 2.1875rem;
  line-height: 1.2;
  opacity: 0;
  transform: translateY(60px);
  transition: opacity 0.6s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.c-intro.is-inview {
  opacity: 1;
  transform: none;
  transition-delay: 0.3s;
}
.c-features {
  padding: 7.5rem 0;
}
.c-features_item {
  background-color: rgba(0, 0, 0, 0.1);
  border-radius: 20px;
  padding: 3.75rem;
  margin-bottom: 3.75rem;
}
.c-summary {
  margin: 3.75rem 0 7.5rem;
}
.c-summary_text {
  font-size: 1.125rem;
  font-weight: 600;
  opacity: 0;
  transform: translateY(60px);
  transition: transform 1s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.c-summary.is-inview .c-summary_text {
  opacity: 1;
  transform: none;
}
@media (min-width: 1000px) {
  .c-summary_text {
    max-width: 320px;
  }
}
@media (max-width: 999px) {
  .c-summary_list {
    margin-top: 1.875rem;
  }
}
.c-summary_list_item {
  position: relative;
  opacity: 0;
  transform: translateY(60px);
  transition: opacity 0.6s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.c-summary_list_item:after {
  content: "";
  position: absolute;
  bottom: 0;
  right: 0;
  left: 0;
  height: 1px;
  background-color: #272727;
  transform: scaleX(0);
  transform-origin: center left;
  transition: transform 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.c-summary_list_item.is-inview {
  transform: none;
  opacity: 1;
}
.c-summary_list_item.is-inview:after {
  transform: scaleX(1);
}
.c-summary_list_item.is-inview:first-child {
  transition-delay: 0.1s;
}
.c-summary_list_item.is-inview:first-child:after {
  transition-delay: 0.5s;
}
.c-summary_list_item.is-inview:nth-child(2) {
  transition-delay: 0.2s;
}
.c-summary_list_item.is-inview:nth-child(2):after {
  transition-delay: 0.6s;
}
.c-summary_list_item.is-inview:nth-child(3) {
  transition-delay: 0.3s;
}
.c-summary_list_item.is-inview:nth-child(3):after {
  transition-delay: 0.7s;
}
.c-summary_list_item.is-inview:nth-child(4) {
  transition-delay: 0.4s;
}
.c-summary_list_item.is-inview:nth-child(4):after {
  transition-delay: 0.8s;
}
.c-summary_list_item.is-inview:nth-child(5) {
  transition-delay: 0.5s;
}
.c-summary_list_item.is-inview:nth-child(5):after {
  transition-delay: 0.9s;
}
.c-summary_list_item.is-inview:nth-child(6) {
  transition-delay: 0.6s;
}
.c-summary_list_item.is-inview:nth-child(6):after {
  transition-delay: 1s;
}
.c-summary_list_item a {
  display: block;
  padding: 8px 0;
}
.c-summary_list_icon {
  position: absolute;
  top: 50%;
  right: 0;
  transform: translateY(-50%) translateX(30px) rotate(90deg);
  opacity: 0;
  transition: opacity 0.4s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 0.4s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.c-summary_list_item.is-inview .c-summary_list_icon {
  transform: translateY(-50%) rotate(0deg);
  opacity: 1;
}
.c-summary_list_item.is-inview:first-child .c-summary_list_icon {
  transition-delay: 0.6s;
}
.c-summary_list_item.is-inview:nth-child(2) .c-summary_list_icon {
  transition-delay: 0.7s;
}
.c-summary_list_item.is-inview:nth-child(3) .c-summary_list_icon {
  transition-delay: 0.8s;
}
.c-summary_list_item.is-inview:nth-child(4) .c-summary_list_icon {
  transition-delay: 0.9s;
}
.c-summary_list_item.is-inview:nth-child(5) .c-summary_list_icon {
  transition-delay: 1s;
}
.c-summary_list_item.is-inview:nth-child(6) .c-summary_list_icon {
  transition-delay: 1.1s;
}
.c-section {
  position: relative;
}
@media (max-width: 1199px) {
  .c-section {
    padding-bottom: 10vh;
    margin-bottom: 10vh;
  }
}
@media (min-width: 1200px) {
  .c-section {
    margin-bottom: 35vh;
  }
}
.c-section_infos {
  position: relative;
  max-width: 320px;
  z-index: 0;
}
@media (min-width: 1000px) {
  .c-section_infos {
    padding-top: 7.5rem;
  }
  .c-section_infos.-padding {
    padding-top: 35vh;
  }
}
@media (max-width: 999px) {
  .c-section_infos {
    margin-bottom: 1.875rem;
  }
}
.c-section_infos_inner > * {
  opacity: 0;
  transform: translateY(60px);
  transition: opacity 0.6s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.c-section_infos_inner.is-inview > * {
  opacity: 1;
  transform: none;
}
.c-section_infos_inner.is-inview > :first-child {
  transition-delay: 0.06s;
}
.c-section_infos_inner.is-inview > :nth-child(2) {
  transition-delay: 0.12s;
}
.c-section_infos_inner.is-inview > :nth-child(3) {
  transition-delay: 0.18s;
}
.c-sections_infos_text {
  margin-top: 1.25rem;
}
.c-speed-block {
  position: relative;
}
@media (min-width: 1000px) {
  .c-speed-block.-margin {
    margin-top: 7.5rem;
  }
}
@media (max-width: 999px) {
  .c-speed-block {
    margin: 1.875rem 0;
  }
}
@media (max-width: 699px) {
  .c-speed-block {
    margin: 15px 0;
  }
}
.c-speed-block_image {
  margin-top: -30px;
  margin-bottom: -30px;
}
.c-speed-block_title {
  font-size: 1.5rem;
  text-transform: uppercase;
  font-weight: 600;
  color: #fff;
  text-align: center;
  position: absolute;
  bottom: 3.75rem;
  right: 0;
  left: 0;
  opacity: 0;
  transform: translateY(60px);
  transition: opacity 0.6s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.c-speed-block_title.is-inview {
  opacity: 1;
  transform: none;
  transition-delay: 0.3s;
}
@media (max-width: 1199px) {
  .c-speed-block_title {
    display: none;
  }
}
.c-speed-block_bubble {
  position: absolute;
  right: 20px;
  top: 30%;
  z-index: 1;
  color: #d4c9c9;
  padding: 1.5rem 2.5rem;
  font-size: 1.25rem;
}
.c-speed-block_bubble.-right {
  right: -30px;
}
.c-speed-block_bubble.-left {
  right: auto;
  left: -30px;
}
.c-speed-block_bubble.-top {
  top: -20%;
}
.c-speed-block_bubble.-bottom {
  top: auto;
  bottom: 0;
}
.c-speed-block_bubble:before {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  z-index: -1;
  background-color: #272727;
  border-radius: 50%;
  transform: scale(0);
  transition: transform 0.6s cubic-bezier(0.17, 0.67, 0.3, 1.33);
}
.c-speed-block_bubble.is-inview:before {
  transform: scale(1);
  transition-delay: 0.3s;
}
@media (max-width: 1199px) {
  .c-speed-block_bubble {
    display: none;
  }
}
.c-direction-block_wrapper {
  margin-bottom: 31.25rem;
}
@media (min-width: 1200px) {
  .c-direction-block_wrapper {
    min-height: 180vh;
  }
}
@media (min-width: 1000px) and (max-width: 1199px) {
  .c-direction-block_wrapper {
    min-height: 130vh;
  }
}
@media (min-width: 700px) and (max-width: 999px) {
  .c-direction-block_wrapper {
    min-height: 100vh;
  }
}
@media (max-width: 699px) {
  .c-direction-block_wrapper {
    min-height: 70vh;
  }
}
@media (min-width: 1000px) {
  .c-direction-block_wrapper {
    margin-top: -35vh;
  }
}
.c-direction-block {
  position: absolute;
  right: 0;
  left: 0;
  z-index: 1;
}
@media (min-width: 1200px) {
  .c-direction-block {
    top: -50vh;
    bottom: -50vh;
  }
}
@media (min-width: 700px) and (max-width: 1199px) {
  .c-direction-block {
    top: -30vh;
    bottom: -50vh;
  }
}
@media (max-width: 699px) {
  .c-direction-block {
    top: -15vh;
    bottom: 0;
  }
}
@media (min-width: 1000px) and (max-width: 1199px) {
  .c-direction-block {
    margin-top: 6.25rem;
  }
}
@media (min-width: 1200px) {
  .c-direction-block {
    margin-top: 18.75rem;
  }
}
.c-direction-block_item {
  position: absolute;
  font-size: 10vw;
  white-space: nowrap;
  font-weight: 600;
  text-transform: uppercase;
  line-height: 1;
}
.c-direction-block_item span {
  display: block;
  background-color: #fff;
  white-space: nowrap;
  padding: 0 20px;
}
.c-direction-block_item.-one {
  top: 33%;
  transform: translateX(-50vw) rotate(26deg);
}
.c-direction-block_item.-two {
  top: 45%;
}
.c-direction-block_item.-three {
  top: 55%;
  transform: rotate(9deg);
}
.c-direction-block_item.-four {
  top: 68%;
  transform: translateX(-50vw) rotate(-19deg);
}
.c-direction-block_item.-five {
  top: 63%;
  transform: translateX(-10vw) rotate(3deg);
}
.c-lerp-block {
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 10rem;
}
@media (min-width: 1000px) {
  .c-lerp-block:not(:first-child) {
    margin-top: 3.75rem;
  }
}
@media (max-width: 999px) {
  .c-lerp-block {
    margin-top: 1.875rem;
  }
}
.c-lerp-block_index {
  vertical-align: middle;
  color: #d4c9c9;
  width: 3.75rem;
  height: 2.8125rem;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  position: relative;
  z-index: 1;
}
.c-lerp-block_index:before {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  z-index: -1;
  background-color: #272727;
  border-radius: 50%;
  transform: scale(0);
  transition: transform 0.6s cubic-bezier(0.17, 0.67, 0.3, 1.33);
}
.c-lerp-block_index.is-inview:before {
  transform: scale(1);
  transition-delay: 0.3s;
}
.c-lerp-block_title {
  display: inline-block;
  vertical-align: middle;
  font-size: 0;
  margin-left: 1.25rem;
  line-height: 1.1;
}
.c-lerp-block_title.is-inview > span:not([data-scroll]) {
  opacity: 1;
  transform: none;
  transition-delay: 0.4s;
}
.c-lerp-block_title > span:not([data-scroll]) {
  opacity: 0;
  transform: translateY(60px);
  transition: opacity 0.6s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.c-lerp-block_title span {
  display: inline-block;
  min-width: 0.3em;
}
@media (max-width: 699px) {
  .c-lerp-block_title span {
    font-size: 1.5625rem;
  }
}
@media (min-width: 700px) {
  .c-lerp-block_title span {
    font-size: 4.375rem;
  }
}
.c-cta_line {
  margin: 0;
  transform: scaleX(0);
  transition: transform 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.c-cta_line.-margin {
  margin-bottom: 30px;
}
.c-cta_line.is-inview {
  transform: scaleX(1);
}
.c-cta_content {
  margin: 3.75rem 0;
}
.c-cta_content_text {
  max-width: 520px;
}
.c-cta_content_text > * {
  opacity: 0;
  transform: translateY(60px);
  transition: opacity 0.6s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
}
.c-cta_content_text > :not(:first-child) {
  margin-top: 1.875rem;
}
.c-cta_content_text.is-inview > * {
  opacity: 1;
  transform: none;
}
.c-cta_content_text.is-inview > :first-child {
  transition-delay: 0.06s;
}
.c-cta_content_text.is-inview > :nth-child(2) {
  transition-delay: 0.12s;
}
.c-cta_content_text.is-inview > :nth-child(3) {
  transition-delay: 0.18s;
}
.c-cta_button {
  opacity: 0;
  transform: translateY(60px);
  transition: opacity 0.6s cubic-bezier(0.215, 0.61, 0.355, 1),
    transform 0.6s cubic-bezier(0.215, 0.61, 0.355, 1);
  margin-top: 5.625rem;
}
.c-cta_button.is-inview {
  opacity: 1;
  transform: none;
}
.c-cta_section {
  margin-bottom: 11.25rem;
}
.c-choochoo_item {
  padding: 50vh 0;
  font-size: 6.25rem;
}
.c-choochoo_item span {
  display: block;
}
.c-choochoo_item.-reverse span,
html[data-direction="up"] .c-choochoo_item span {
  transform: rotateY(180deg);
}
html[data-direction="up"] .c-choochoo_item.-reverse span {
  transform: rotateY(0deg);
}
@media (max-width: 1199px) {
  .c-choochoo_item {
    display: none;
  }
}
@media (max-width: 999px) {
  .c-damn {
    padding: 150vh 0 0;
  }
}
@media (min-width: 1000px) {
  .c-damn {
    padding: 100vh 0 0;
  }
}
.u-2\:1:before {
  padding-bottom: 50%;
}
.u-4\:3:before {
  padding-bottom: 75%;
}
.u-16\:9:before {
  padding-bottom: 56.25%;
}
.u-1\/1 {
  width: 100% !important;
}
.u-1\/2 {
  width: 50% !important;
}
.u-2\/2 {
  width: 100% !important;
}
.u-1\/3 {
  width: 33.33333% !important;
}
.u-2\/3 {
  width: 66.66667% !important;
}
.u-3\/3 {
  width: 100% !important;
}
.u-1\/4 {
  width: 25% !important;
}
.u-2\/4 {
  width: 50% !important;
}
.u-3\/4 {
  width: 75% !important;
}
.u-4\/4 {
  width: 100% !important;
}
.u-1\/5 {
  width: 20% !important;
}
.u-2\/5 {
  width: 40% !important;
}
.u-3\/5 {
  width: 60% !important;
}
.u-4\/5 {
  width: 80% !important;
}
.u-5\/5 {
  width: 100% !important;
}
@media (min-width: 700px) {
  .u-1\/2\@from-small {
    width: 50%;
  }
}
@media (min-width: 1000px) {
  .u-1\/3\@from-medium {
    width: 33.33333%;
  }
}
@media (min-width: 1000px) {
  .u-1\/2\@from-medium {
    width: 50%;
  }
}
@media (min-width: 1000px) {
  .u-2\/5\@from-medium {
    width: 40%;
  }
}
@media (min-width: 1000px) {
  .u-3\/5\@from-medium {
    width: 60%;
  }
}
.u-float-left {
  float: left !important;
}
.u-float-right {
  float: right !important;
}
.u-text-center {
  text-align: center !important;
}
.u-text-left {
  text-align: left !important;
}
.u-text-right {
  text-align: right !important;
}
.u-align-baseline {
  vertical-align: baseline !important;
}
.u-align-bottom {
  vertical-align: bottom !important;
}
.u-align-middle {
  vertical-align: middle !important;
}
.u-align-top {
  vertical-align: top !important;
}
.u-vertical-center {
  font-size: 0;
}
.u-vertical-center:before {
  display: inline-block;
  height: 100%;
  content: "";
  vertical-align: middle;
}
.u-vertical-center > * {
  display: inline-block;
  vertical-align: middle;
  font-size: 1rem;
}
.u-white {
  color: #fff;
}
.u-label {
  font-size: 1.5rem;
  text-transform: uppercase;
  font-weight: 600;
}
.u-icon {
  font-family: Lucida Grande;
  font-size: 1.125rem;
}
.u-text {
  font-size: 0.875rem;
}
.u-clearfix:after {
  display: block;
  clear: both;
  content: "";
}
.u-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  word-wrap: normal;
  max-width: 100%;
}
[hidden][aria-hidden="false"] {
  position: absolute;
  display: inherit;
  clip: rect(0, 0, 0, 0);
}
[hidden][aria-hidden="false"]:focus {
  clip: auto;
}
.u-screen-reader-text {
  position: absolute !important;
  overflow: hidden;
  clip: rect(0 0 0 0);
  margin: 0;
  padding: 0;
  width: 1px;
  height: 1px;
  border: 0;
}
@media not print {
  .u-screen-reader-text\@screen {
    position: absolute !important;
    overflow: hidden;
    clip: rect(0 0 0 0);
    margin: 0;
    padding: 0;
    width: 1px;
    height: 1px;
    border: 0;
  }
}
.u-screen-reader-text.-focusable:active,
.u-screen-reader-text.-focusable:focus {
  clip: auto;
  width: auto;
  height: auto;
}

</style>

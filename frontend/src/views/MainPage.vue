<template>
  <div>
    <div class="cover-5">
      <div class="container">
        <section data-bgcolor="#bcb8ad" data-textcolor="#032f35">
        <div>
          <h1 data-scroll data-scroll-speed="1"><span>Horizontal</span> <span>scroll</span> <span>section</span></h1>
          <p data-scroll data-scroll-speed="2" data-scroll-delay="0.2">with GSAP ScrollTrigger & Locomotive Scroll</p>
          <router-link :to="'/tutorial'">
            <div class='btn'>go to tutorial</div>
          </router-link>
        </div>
        </section>

        <section id="sectionPin">
          <div class="pin-wrap">
            <h2>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</h2>
            <img src="https://images.pexels.com/photos/5207262/pexels-photo-5207262.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=900" alt="">
            <img src="https://images.pexels.com/photos/3371358/pexels-photo-3371358.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=900" alt="">
            <img src="https://images.pexels.com/photos/3618545/pexels-photo-3618545.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=900" alt="">

          </div>
        </section>

        <section data-bgcolor="#e3857a" data-textcolor="#f1dba7"><img src="https://images.pexels.com/photos/4791474/pexels-photo-4791474.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" alt="">
          <h2 data-scroll data-scroll-speed="1" class="credit"><a href="https://thisisadvantage.com" target="_blank">Made by Advantage</a></h2>
        </section>
        </div>
      </div>
    <div class="cover">
      <div class="cover-heading">
        <span class="imsrk">GNM</span>
        <span class="dot">.</span>
      </div>
    </div>
    <div class="imsrk2">welcome!</div>
  </div>
</template>

<script>
import { gsap } from 'gsap';
import { ScrollTrigger } from "gsap/ScrollTrigger";
import LocomotiveScroll from 'locomotive-scroll';

gsap.registerPlugin(ScrollTrigger);

export default {
  name: 'MainPage',
  data() {
    return {
      options: {
        navigation: true,
        onLeave: this.onLeave,
        licenseKey: "your_key"
      },
    };
  },
  methods: {
    // onScroll() {
    //   const pageContainer = document.querySelector(".container");
    //   /* SMOOTH SCROLL */
    //   const scroller = new LocomotiveScroll({
    //     el: pageContainer,
    //     smooth: true
    //   });
    //   let pinWrap = document.querySelector(".pin-wrap");
    //   let pinWrapWidth = pinWrap.offsetWidth;
    //   let horizontalScrollLength = pinWrapWidth - window.innerWidth;
  
    //   // Pinning and horizontal scrolling

    //   gsap.to(".pin-wrap", {
    //     scrollTrigger: {
    //       scroller: pageContainer, //locomotive-scroll
    //       scrub: true,
    //       trigger: "#sectionPin",
    //       pin: true,
    //       // anticipatePin: 1,
    //       start: "top top",
    //       end: pinWrapWidth
    //     },
    //     x: -horizontalScrollLength,
    //     ease: "none"
    //   });

    //   ScrollTrigger.addEventListener("refresh", () => scroller.update()); //locomotive-scroll

    //   ScrollTrigger.refresh();
    // }
  }, 
  mounted: function(){ 
    const pageContainer = document.querySelector(".container");
    /* SMOOTH SCROLL */
    const scroller = new LocomotiveScroll({
      el: pageContainer,
      smooth: true
    });
    scroller.on("scroll", ScrollTrigger.update);
    ScrollTrigger.scrollerProxy(pageContainer, {
      scrollTop(value) {
        return arguments.length
          ? scroller.scrollTo(value, 0, 0)
          : scroller.scroll.instance.scroll.y;
      },
      getBoundingClientRect() {
        return {
          left: 0,
          top: 0,
          width: window.innerWidth,
          height: window.innerHeight
        };
      },
      pinType: pageContainer.style.transform ? "transform" : "fixed"
    });
    let t1 = gsap.timeline();
    t1.from(".imsrk", {
      opacity: 0,
      xPercent: -100,
      delay: 0.5,
      duration: 1,
      ease: "power1.out",
      yoyo: true,
    });
    t1.from(
      ".dot",
      {
        opacity: 0,
        yPercent: 100,
        delay: 0.5,
        repeatDelay: 1,
        duration: 1,
        ease: "power1.out",
      },
      0.01
    );

    t1.to(".dot", {
      x: 20,
      duration: 1,
      ease: "power1.out",
    });

    t1.to(".dot", {
      x: -10,
      duration: 0.5,
      ease: "power1.out",
    });

    t1.to(".imsrk", {
      opacity: 0,
      xPercent: -100,
      duration: 1,
      ease: "power1.out",
      yoyo: true,
    });

    t1.to(
      ".dot",
      {
        opacity: 0,
        duration: 1,
        ease: "expo.out",
      },
      3
    );

    t1.to(
      ".cover",
      {
        xPercent: -100,
        duration: 1,
        ease: "power1.out",
      },
      3
    );

    t1.from(
      ".imsrk2",
      {
        xPercent: -100,
        duration: 1,
        ease: "power1.out",
        opacity: 0,
      },
      3.8
    );

    t1.from(".cover-5", {
      yPercent: -100,
      duration: 1,
      ease: "power1.out",
      delay: 0.4,
    });
  },
}
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Karla:wght@400;700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap");
*,
*::after,
*::before {
  margin: 0;
  padding: 0;
  -webkit-box-sizing: inherit;
          box-sizing: inherit;
}

:root {
  --text-color: #111;
  --bg-color: #dad4cc;
}

.cover {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  font-family: "Karla", sans-serif;
  line-height: 1.7;
  position: relative;
  height: 100vh;
  overflow: hidden;
}

.container {
  color: var(--text-color);
  background: var(--bg-color);
  transition: 0.3s ease-out;
  overflow-x: hidden;
  max-width: 100%;
  width: 100%;
  overscroll-behavior: none;
}
.btn {
  text-decoration: none;
  color: #fe3901;
  position: fixed;
  display: flex;
  margin-top: 40px;
  opacity: 0.5;
  border: 1px solid gray;
  padding: 5px 12px 6px 12px;
  border-radius: 5px;
  font-weight: 600;
  font-size: 40px;
  
}
header {
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  padding: 20px 14px;
}

header img {
  height: 15px;
}

header ul {
  margin-left: auto;
}

header ul li {
  color: white;
  text-transform: uppercase;
  font-weight: 600;
  font-size: 10px;
  letter-spacing: 1px;
  display: inline-block;
  margin-left: 10px;
}

.cover-5 {
  background: -webkit-gradient(linear, left top, left bottom, from(#1d1d1d), to(black));
  background: linear-gradient(to bottom, #1d1d1d, black);
  position: absolute;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

article {
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-wrap: wrap;
      flex-wrap: wrap;
  max-width: 80%;
}

.cover {
  background-color: black;
  position: absolute;
  width: 100%;
  height: 100vh;
}

.cover-heading {
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
}

.cover-heading span {
  color: white;
  font-size: 60px;
  font-weight: 900;
  display: inline-block;
  font-family: "Roboto", sans-serif;
}

.imsrk2 {
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  color: blac;
  font-size: 72px;
  font-weight: 900;
  z-index: -1;
  color: #2d2d2d;
  font-family: "Roboto", sans-serif;
  letter-spacing: -4px;
  line-height: 1;
}
.imsrk {
  color: white;
  font-size: 52px;
  font-weight: 900;
  display: inline-block;
  font-family: "Roboto", sans-serif;
}
section:not(#sectionPin) {
  min-height: 100vh;
  width: 100%;
  position: relative;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  grid-gap: 2rem;
  padding: 50px 10vw;
  margin: auto;
  place-items: center;
}
img {
  height: 80vh;
  width: auto;
  object-fit: cover;
}

h1 {
  font-size: 5rem;
  line-height: 1;
  font-weight: 800;
  margin-bottom: 1rem;
  position: absolute;
  top: 10vw;
  left: 10vw;
  z-index: 4;
  overflow-wrap: break-word;
  hyphens: auto;
  color:white;
  font-family: 'Cinzel';

  @media (max-width: 768px) {
    font-size: 16vw;
  }
  span {
    display: block;
    color: white;
  }
}

h2 {
  font-size: 2rem;
  max-width: 400px;
  color: white;
}

.credit {
  font-family: 'Cinzel', sans-serif;
  a {
    color: var(--text-color);
  }
}

* {
  box-sizing: border-box;
}

#sectionPin {
  height: 100vh;
  overflow: hidden;
  display: flex;
  left: 0;
  background: var(--text-color);
  color: var(--bg-color);
}

.pin-wrap {
  height: 100vh;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  padding: 50px 10vw;

  & > * {
    min-width: 60vw;
    padding: 0 5vw;
  }
}

p {
  position: absolute;
  bottom: 10vw;
  right: 10vw;
  width: 200px;
  line-height: 1.5;
  color:white;
  font-family: "Roboto";
}



// @media (min-width: 1024px) {
//   .cover-heading h1 {
//     font-size: 60px;
//   }
//   .cover-heading span {
//     font-size: 60px;
//   }
//   .imsrk2 {
//     font-size: 124px;
//   }
//   header {
//     padding: 50px 80px;
//   }
//   header ul {
//     margin-left: auto;
//   }
//   header ul li {
//     font-size: 20px;
//   }
//   .container {
//     margin-top: 100px;
//     display: -ms-grid;
//     display: grid;
//     -ms-grid-columns: 1fr 1fr;
//         grid-template-columns: 1fr 1fr;
//     -webkit-box-align: center;
//         -ms-flex-align: center;
//             align-items: center;
//   }
//   .container .left{
//     margin-left:20%;
//   }
//   .container .right {
//     padding: 0;
//     margin-top: -80px;
//   }
//   .container .right h1 {
//     color: white;
//     font-size: 140px;
//     font-weight: 400;
//     display: inline-block;
//     font-family: 'Cinzel';
//     line-height: 1;
//   }
//   .container .right span {
//     font-size: 50px;
//     letter-spacing: -4px;
//     color: #6b6b6b;
//   }
//   .container .right p {
//     margin-top: 40px;
//     max-width: 600px;
//     color: white;
//     opacity: 0.5;
//     font-size: 18px;
//     line-height: 1.7;
//   }
//   .container .right a {
//     text-decoration: none;
//     color: white;
//     display: inline-block;
//     margin-top: 40px;
//     opacity: 0.5;
//     border: 1px solid gray;
//     padding: 5px 12px 6px 12px;
//     border-radius: 5px;
//   }
// }
// /*# sourceMappingURL=style.css.map */



</style>

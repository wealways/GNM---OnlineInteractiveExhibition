<template>
  <div>
    <div class="cover-5">
        <header>
          <!-- <img class="logo" src="https://i.imgur.com/ZFnSyPe.png" alt="" /> -->

          <ul class="items">
            <li class="item">
              Actor
            </li>
            <li class="item">
              Producer
            </li>
            <li class="item">
              Contact
            </li>
          </ul>
        </header>

        <div class="container">
          <div class="left">
            <img class="header-img" src="https://i.imgur.com/9huul5F.png" alt="" />
          </div>

          <div class="right">
            <h1 class="heading">
              <span>The King </span><br />
              KHAN
            </h1>
            <p class="sub-heading">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda
              unde dicta, repellendus consequuntur, at.
            </p>

            <a class="button" href="#">Learn More</a>
          </div>
        </div>
      </div>
      <div class="cover-4"></div>
      <div class="cover-3"></div>
      <div class="cover-2"></div>
      <div class="cover">
        <div class="cover-heading">
          <h1 class="imsrk">imsrk</h1>
          <span class="dot">.</span>
        </div>
      </div>

      <div class="imsrk2">Shahrukh Khan</div>
  </div>
</template>

<script>
import { gsap } from 'gsap'

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
  mounted: function(){
    let t1 = gsap.timeline()
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

    t1.to(
      ".cover-2",
      {
        xPercent: -100,
        duration: 1,
        ease: "power1.out",
      },
      3.2
    );

    t1.to(
      ".cover-3",
      {
        xPercent: -100,
        duration: 1,
        ease: "power1.out",
      },
      3.4
    );

    t1.to(
      ".cover-4",
      {
        xPercent: -100,
        duration: 1,
        ease: "power1.out",
      },
      3.6
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

    t1.from(".logo", {
      xPercent: -100,
      opacity: 0,
      duration: 1,
      ease: "power1.out",
    });

    t1.from(
      ".item",
      {
        xPercent: 100,
        opacity: 0,
        duration: 1,
        ease: "power1.out",
        stagger: {
          amount: 0.5,
          from: "left",
        },
      },
      6
    );

    t1.from(
      ".header-img",
      {
        xPercent: -100,
        opacity: 0,
        duration: 1,
        ease: "power1.out",
      },
      6.2
    );

    t1.from(
      ".heading",
      {
        xPercent: 100,
        opacity: 0,
        duration: 1,
        ease: "power1.out",
      },
      6.2
    );

    t1.from(
      ".sub-heading",
      {
        xPercent: 100,
        opacity: 0,
        duration: 1.1,
        ease: "power1.out",
      },
      6.2
    );

    t1.from(
      ".button",
      {
        yPercent: 100,
        opacity: 0,
        duration: 2,
        ease: "bounce",
      },
      6.5
    );
  }, 
  methods: {
    componentsReady(){
      this.$refs.fullpage.init()
    },
  }
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

body {
  -webkit-box-sizing: border-box;
          box-sizing: border-box;
  font-family: "Karla", sans-serif;
  line-height: 1.7;
  position: relative;
  height: 100vh;
  overflow: hidden;
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

.container {
  margin-top: 20px;
  display: -ms-grid;
  display: grid;
  -ms-grid-columns: 1fr;
      grid-template-columns: 1fr;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
}

.container .left img {
  width: 100%;
  border-radius: 5px;
}

.container .right {
  padding: 0 10px;
  margin-top: -100px;
}

.container .right h1 {
  color: white;
  font-size: 124px;
  font-weight: 900;
  display: inline-block;
  font-family: serif;
  line-height: 1;
}

.container .right span {
  font-size: 72px;
  letter-spacing: -4px;
  color: #232323;
}

.container .right p {
  margin-top: 40px;
  max-width: 600px;
  color: white;
  opacity: 0.5;
  font-size: 18px;
  line-height: 1.7;
}

.container .right a {
  text-decoration: none;
  color: white;
  display: inline-block;
  margin-top: 40px;
  opacity: 0.5;
  border: 1px solid gray;
  padding: 5px 12px 6px 12px;
  border-radius: 5px;
}

.cover-2 {
  background-color: #0f0f0f;
  position: absolute;
  width: 100%;
  height: 100vh;
}

.cover-3 {
  background-color: #111111;
  position: absolute;
  width: 100%;
  height: 100vh;
}

.cover-4 {
  background-color: #131313;
  position: absolute;
  width: 100%;
  height: 100vh;
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

.cover-heading h1 {
  color: white;
  font-size: 52px;
  font-weight: 900;
  display: inline-block;
  font-family: "Roboto", sans-serif;
}

.cover-heading span {
  color: white;
  font-size: 52px;
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

@media (min-width: 1024px) {
  .cover-heading h1 {
    font-size: 72px;
  }
  .cover-heading span {
    font-size: 72px;
  }
  .imsrk2 {
    font-size: 124px;
  }
  header {
    padding: 50px 80px;
  }
  header ul {
    margin-left: auto;
  }
  header ul li {
    font-size: 14px;
    margin-left: 50px;
  }
  .container {
    margin-top: 100px;
    display: -ms-grid;
    display: grid;
    -ms-grid-columns: 1fr 1fr;
        grid-template-columns: 1fr 1fr;
    -webkit-box-align: center;
        -ms-flex-align: center;
            align-items: center;
  }
  .container .left img {
    width: auto;
    height: 600px;
    border-radius: 5px;
  }
  .container .right {
    padding: 0;
    margin-top: -80px;
  }
  .container .right h1 {
    color: white;
    font-size: 124px;
    font-weight: 900;
    display: inline-block;
    font-family: serif;
    line-height: 1;
  }
  .container .right span {
    font-size: 72px;
    letter-spacing: -4px;
    color: #232323;
  }
  .container .right p {
    margin-top: 40px;
    max-width: 600px;
    color: white;
    opacity: 0.5;
    font-size: 18px;
    line-height: 1.7;
  }
  .container .right a {
    text-decoration: none;
    color: white;
    display: inline-block;
    margin-top: 40px;
    opacity: 0.5;
    border: 1px solid gray;
    padding: 5px 12px 6px 12px;
    border-radius: 5px;
  }
}
/*# sourceMappingURL=style.css.map */
</style>

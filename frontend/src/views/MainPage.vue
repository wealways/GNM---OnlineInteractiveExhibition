<template>
  <div>
    <div class="cover-5">
      <router-link :to="'/tutorial'">
        <GoToTutorial class="tutorial"/>
      </router-link>
      <div class="container">
        <div class="scrollicon">
          <div class="icon-scroll">
            <div class="scrolltext" style="color:white; font-family:'Cinzel">
              scroll
            </div>
          </div>
        </div>
       
        <section data-bgcolor="#bcb8ad">
          <div>
            <div class='maintext' data-scroll data-scroll-speed="1" style="margin-top:0;">
              <span>On-line</span> <span>Interactive</span>
              <span>Exhibition</span>
              <div class='myname'>그림이 널 만났을 때</div>
              <img src="@/assets/GNM2.png" alt="" style="width:40vw;height:27vh;margin-top:60px;">
            </div>
            <div id="tutorialbtn" class="btn desc__gototutorial">전시 보러 가기</div>
            
          </div>
        </section>

        <section class="" style="" >
          <div class="row panel">
            <div class="col-4 wrapper">
              <img src="../assets/main/art6.jpg" alt="art" class=" col-3 " style="height: 100%; width: 100%; position:relative;">
              <p class="description q-pt-xl"> 코시국으로<br> 외출한 지가 오래라 <br>마지막으로<br> 미술관 간지가 <br>언젠지도 몰라</p>
            </div>
            <div class="col-8 row" style="position:relative;">
              <div class="col-6 wrapper">
                <img src="../assets/main/ma2.jpg" alt="art" class="" >
                <p class="description q-pt-lg"> <br>그림?<br>전 그림이 너무 <br>어려워요.</p>
              </div>
              <div class="col-6 wrapper ">
                <img src="../assets/main/art5.png" alt="art" class="" >
                <p class="description q-pt-md"> 언제까지 <br>멀리서 <br>구경만 할 거예요?</p>
              </div>
              <div class="col-6 wrapper">
                <img src="../assets/main/kids7.jpg" alt="art" class="" >
                <p class="description q-pt-sm" style='margin-top:20px;'> 미술관은 지루해.<br>집에 가서 게임하면<br> 안 돼요?</p>
              </div>
              <div class="col-6 wrapper row justify-center items-center">
                <img src="../assets/main/clo.jpg" alt="art" class="">
                <p class="description q-pt-xl">미술관에 가려면... <br>뭘 입어야 하지?</p>
              </div>
            </div>
          </div>
        </section>


        <section class="c-section" style="height:300vh;">
            <div class="o-container" id="scroll-direction">
                <div class="c-direction-block_wrapper">
                    <div class="c-section_infos -padding" data-scroll data-scroll-sticky data-scroll-target="#scroll-direction">
                        <div class="c-section_infos_inner" data-scroll>
                          <div>
                            <img src="../assets/main/arrow.png" alt="">
                          </div>

                        </div>
                    </div>
                    <div class="c-direction-block" id="direction">
                        <div class="c-direction-block_item -one">
                            <span class="c-direction-block_item_inner" data-scroll data-scroll-direction="horizontal" data-scroll-speed="6" data-scroll-target="#direction">
                                U think art is difficult?
                            </span>
                        </div>
                        <div class="c-direction-block_item -two">
                            <span class="c-direction-block_item_inner" data-scroll data-scroll-direction="horizontal" data-scroll-speed="-8" data-scroll-target="#direction">
                                Come see enjoy our gallery.
                            </span>
                        </div>
                        <div class="c-direction-block_item -three">
                            <span class="c-direction-block_item_inner" data-scroll data-scroll-direction="horizontal" data-scroll-speed="9" data-scroll-target="#direction" data-scroll-delay="0.05">
                                Hav fun with art. It's not difficult. Right?
                            </span>
                        </div>
                        <div class="c-direction-block_item -four">
                            <span class="c-direction-block_item_inner" data-scroll data-scroll-direction="horizontal" data-scroll-speed="15" data-scroll-target="#direction">
                                You are gonna love this. I guarantee!
                            </span>
                        </div>
                        <div class="c-direction-block_item -five">
                            <span class="c-direction-block_item_inner" data-scroll data-scroll-direction="horizontal" data-scroll-speed="-20" data-scroll-target="#direction" data-scroll-delay="0.05">
                                Ohhhhh, Our gallery is F U N !!!!
                            </span>
                        </div>
                    </div>
                </div>
              </div>
        </section>



        <section class="section cheon">
          <img src="../assets/main/cheon.png" alt="art" class="" >
          <div class="section-0" data-scroll data-scroll-speed="3">
            <p style="color:black;position:relative;"
                data-scroll 
                data-scroll-direction="horizontal" 
                data-scroll-speed="-2"
            >
                천
            </p>
            <p style="color:black;position:relative;"
                data-scroll 
                data-scroll-direction="horizontal" 
                data-scroll-speed="3"
            >
                경
            </p>
            <p style="color:black;position:relative;"
                data-scroll 
                data-scroll-direction="horizontal" 
                data-scroll-speed="2"
            >
                자
            </p>
          </div>    
 
        </section>
        
        <section class="section klimt">
          <img src="../assets/main/klimt.png" alt="art" class="klimt-img" >
          <div class="section-0" data-scroll data-scroll-speed="4">
            <p style="color:black;position:relative;"
                data-scroll 
                data-scroll-direction="horizontal" 
                data-scroll-speed="-2"
            >
                Gustav 
            </p>
            <p style="color:black;position:relative;"
                data-scroll 
                data-scroll-direction="horizontal" 
                data-scroll-speed="2"
            >
                Klimt 
            </p>
          </div>    
          

        </section>


        <section class="section monet">
          
          <div class="section-0" data-scroll data-scroll-speed="4">
            <p style="color:black;position:relative;"
                data-scroll 
                data-scroll-direction="horizontal" 
                data-scroll-speed="-2"
            >
                Claude
            </p>
            <p style="color:black;position:relative;"
                data-scroll 
                data-scroll-direction="horizontal" 
                data-scroll-speed="2"
            >
                Monet
            </p>            
          </div>
          <img src="../assets/main/monetcut.png" alt="art" class="" >
        </section>

        <section style="background: linear-gradient(white, #111); height: 120vh;">


        </section>

        <section style="height:180vh;">
          <div class="row panel">
  
            <div class="col-8 row" style="position:relative;">
              <div class="col-6 wrapper">
                <img src="../assets/main/vb1.jpg" alt="art" class="art" >
                <p class="description q-pt-lg"> <br>그림?<br>너무<br>재밌잖아?</p>
              </div>
              <div class="col-6 wrapper ">
                <img src="../assets/main/bed.jpg" alt="art" class="art" >
                <p class="description q-pt-md" style="padding-top : 170px;"> 내 침대가 <br> 바로 미술관</p>
              </div>
              <div class="col-6 wrapper row justify-center items-center">
                <img src="../assets/main/kids5.jpg" alt="art" class="art">
                <p class="description q-pt-sm" style="margin-top:20px;" > 저... 오늘부터<br>그림 그릴거예요 </p>
              </div>
              <div class="col-6 wrapper">
                <img src="../assets/main/kids.jpg" alt="art" class="art" >
                <p class="description q-pt-xl" style="margin-bottom:100px;"> 게임보다<br>재밌어!</p>
              </div>
            </div>
            <div class="col-4 art wrapper">
              <img src="../assets/main/fri.jpg" alt="art" class=" col-3 art" style="height: 100%; width: 100%; position:relative;">
              <p class="description q-pt-xl"> 우리 심심한데 <br> 미술관 갈까?</p>
            </div>
          </div>
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
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import LocomotiveScroll from "locomotive-scroll";
import GoToTutorial from '@/components/IconMap/GoToTutorial';


gsap.registerPlugin(ScrollTrigger);

export default {
  name: "MainPage",
  data() {
    return {
      options: {
        navigation: true,
        onLeave: this.onLeave,
        licenseKey: "your_key",
      },
    };
  },
  components:{
    GoToTutorial
  },
  mounted: function() {
    const pageContainer = document.querySelector(".container");
    /* SMOOTH SCROLL */
    const scroller = new LocomotiveScroll({
      el: pageContainer,
      smooth: true,
    });
    scroller.on("scroll", ScrollTrigger.update);
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
      2
    );

    t1.to(
      ".cover",
      {
        xPercent: -100,
        duration: 1,
        ease: "power1.out",
      },
      2
    );

    t1.from(
      ".imsrk2",
      {
        xPercent: -100,
        duration: 0.1,
        ease: "power1.out",
        opacity: 0,
      },
      1
    );

    t1.from(".cover-5", {
      yPercent: -100,
      duration: 1,
      ease: "power1.out",
      delay: 0.1,
    },
    3
    );
  },
};
</script>
<style scoped>
.klimt-img {
  position: absolute;
  left:5%;
}

.klimt > div {
  position: absolute; 
  right: 20%;
}

.section {
  height: 140vh;
  background-color: white;
  position:relative;
}

.klimt > div > p,
.monet > div > p {
  font-family: 'Playfair Display';
}

.cheon > div > p {
  font-family: 'Noto Serif KR', serif;
}


.description {
  position:absolute;
  z-index: 100;
  top:0;
  left:0;
  width: 100%;
  height:100%;
  font-size : 2rem;
  color: white;
  text-align: center;
  font-family: 'Noto Serif KR', serif;
  white-space: pre-wrap;
  line-break: strict;
  vertical-align: middle;
}

.wrapper {
  position: relative;
  /* width: 100%; */
  /* height:100%; */
  overflow:hidden;
  object-fit: contain;
}

.wrapper > img {
  width: 100%;
  height: 100%;
  background-color: #2a433b;
  opacity:0.6;
}



.wrapper:hover > img{
  transition: 0.7s;
  transform: scale(1.08);
  background-color: black;
  opacity: 0.8;
}

.scrollicon{
  position:fixed;
  left: 13%;
  top: 7%;
}
.scrolltext {
  position: absolute;
  bottom: 100%;
  transform: translateX(-10%) translateY(-30%);
}
.icon-scroll,
.icon-scroll:before {
  position: absolute;
  left: 50%;
}
.icon-scroll {
  width: 40px;
  height: 70px;
  margin-left: -20px;
  top: 90%;
  margin-top: -35px;
  box-shadow: inset 0 0 0 1px #fff;
  border-radius: 25px;
}
.icon-scroll:before {
  content: "";
  width: 8px;
  height: 8px;
  background: #fff;
  margin-left: -4px;
  top: 8px;
  border-radius: 4px;
  -webkit-animation-duration: 1.5s;
  animation-duration: 1.5s;
  -webkit-animation-iteration-count: infinite;
  animation-iteration-count: infinite;
  -webkit-animation-name: scroll;
  animation-name: scroll;
}
@-webkit-keyframes scroll {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    transform: translateY(46px);
  }
}
@keyframes scroll {
  0% {
    opacity: 1;
  }
  100% {
    opacity: 0;
    transform: translateY(46px);
  }
}
</style>
<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Karla:wght@400;700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap");
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css?family=Playfair+Display:400,400i,700,700i,900,900i');
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
#tutorialbtn {
  color: white;
}
.desc__gototutorial{
  position: absolute !important;
  font-size:50px;
  bottom: 9%;
  right: 17%;
}
.img__gototutorial{
  position: absolute !important;
  bottom: 12%;
  right: 13%;
  width:100px !important;
  height:100px !important;
  transform:rotate(-30deg);
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
  font-family: "Cinzel";
  color: black;
  text-decoration: none;
  position: sticky;
  display: flex;
  margin-top: 40px;
  opacity: 0.8;
  border-radius: 5px;
  font-weight: 600;
  font-size: 50px;
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
  background: -webkit-gradient(
    linear,
    left top,
    left bottom,
    from(#1d1d1d),
    to(black)
  );
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

.maintext {
  font-size: 1.2rem;
  line-height: 1;
  font-weight: 400;
  margin-bottom: 1rem;
  position: absolute;
  top: 10vw;
  left: 10vw;
  z-index: 4;
  overflow-wrap: break-word;
  hyphens: auto;

  @media (max-width: 768px) {
    font-size: 16vw;
  }
  span {
    display: block;
    font-family: 'Montserrat','Noto Sans KR';
    color:rgba(221, 221, 221, 0.568);
    
  }
}
.myname {
  margin-top: 10px;
  color: rgb(248, 247, 237);
  font-size: 2rem;
  font-weight: 700;
}
h2 {
  font-size: 2rem;
  max-width: 400px;
  color: white;
}

.credit {
  font-family: "Cinzel", sans-serif;
  a {
    color: var(--text-color);
  }
}

* {
  box-sizing: border-box;
}

p {
  position: absolute;
  bottom: 10vw;
  right: 10vw;
  width: 200px;
  line-height: 1.5;
  color: white;
  font-family: "Roboto";
}

.tutorial {
  position: absolute;
  bottom: 8%;
  right: 7%;
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





.c-section {
  position: relative;
  background: linear-gradient(#111, white);
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




.section-0 {
    margin-top: 20vh;
    text-align: center;
    p {
        font-size: 8vw;
    }
}



</style>

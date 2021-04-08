<template>
  <div class="body">
    <IconMap mapColor="#608091"/>
    <IconVoice voiceColor="#608091"/>
    <div class="page">
      <div class="description">
        <div class="desc-main">
          <h1 class="desc-main__title">Der Kuss</h1>
          <div class="desc-main__subtitle">키스 <span style="font-size:1rem">(1907)</span></div>
          <div class="desc-main__description">
            우리에게 잘 알려진 <strong>"클림트의 키스"</strong>는
            원형, 네모, 직선과 곡선 등 기하학 문양과 함께<br>
            금박 무늬 등 <span style="color:#FFD700">화려한 색체</span>를 앞세운 화풍이 잘 드러납니다.
          </div>
        </div>
        <br>
        <div class="desc-footer">
          <div 
            class="column items-center desc-footer-info"
            @click="hintView">
            <q-icon
              class="desc-footer-info-icon" 
              name="info"
            />
            Click
          </div>
          <div v-if="!hintflag" class="desc-main__description">
            그림 위에서 마우스를 움직이며<br>
            클림트의 화풍을 경험해보세요
          </div>
          <div v-if="hintflag" class="desc-main__description">
            그림 위에서 마우스를 길게 눌러보세요. <br> 
            키스의 모든 색감을 경험할 수 있습니다.
          </div>
        </div>
      </div>
      <svg id="demo" xmlns="http://www.w3.org/2000/svg">
        <defs>
        <radialGradient id="maskGradient">
          <stop offset="50%" stop-color="#fff"/>
          <stop offset="100%" stop-color="#000"/>
        </radialGradient>
        <mask id="theMask">
        <circle id="masker" r="100" fill="url(#maskGradient)" cx="800" cy="450" />
        </mask>
        </defs> 
          <image id="lines" v-if="!originalflag" xlink:href="https://i.ibb.co/jkqJsth/klimt-sketch.png" x="0" y="0" width="800" height="800" />
          <image id="lines" v-if="originalflag" xlink:href="https://i.ibb.co/HzsVFPC/klimt.jpg" x="0" y="0" width="800" height="800" />
          <g id="maskReveal" mask="url(#theMask)" > 
            <image id="regular" xlink:href="https://i.ibb.co/HzsVFPC/klimt.jpg" x="0" y="0" width="800" height="800" />
          </g>
          <circle id="dot" r="4" fill="#dc143c" cx="800" cy="450" />
      </svg>

      <div @click="nextKlimts" class="nextbtn">
        <div class="diamond-container">
        <div class="diamond left"></div>
        <div class="diamond right"></div>
        <div class="arrow"></div>
        </div>
      </div>
      <div class="original-view column items-center" @click="originalView">
        <q-icon class="original-view-icon" name="photo"/>
        <div v-if="!originalflag">Original</div>
        <div v-if="originalflag">Interact</div>
      </div>

      <div id="instructions" style="display:none;">
        <svg id="dial" xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
        <path id="progressRing" d="M50,10A40,40,0,1,1,10,50,40,40,0,0,1,50,10Z" fill="none" stroke="#fff" stroke-miterlimit="10" stroke-width="6"/>
        <circle r="43" fill="none" stroke="#fff" cx="50" cy="50" stroke-width="2" opacity="0.5" />
        <circle r="37" fill="none" stroke="#fff" cx="50" cy="50" stroke-width="2" opacity="0.5"/>
        <text transform="translate(55 56)" text-anchor="start" font-size="20" fill="#fff">%</text>
        <text id="counter" transform="translate(55 56)" text-anchor="end" font-size="20" fill="#fff">0</text>
        </svg>
        <p>Hover mouse to move mask around.</p>
        <p>Hold &amp; release mouse button to expand &amp; contract mask.</p>
      </div>
    </div>
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/2.0.1/TweenLite.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/2.0.1/TimelineMax.min.js"></script>

<script scoped>

import { gsap,TimelineMax } from 'gsap';

export default {
  name:'Klimt',
  data(){
    return {
      hintflag:false,
      originalflag:false
    }
  },
  components:{
    IconMap: () => import('@/components/IconMap/IconMap'),
    IconVoice: () => import('@/components/IconMap/IconVoice')
  },
  mounted(){
    const svg = document.querySelector("#demo");
    const tl = new TimelineMax({onUpdate:onUpdate});
    let pt = svg.createSVGPoint();
    let data = document.querySelector(".tlProgress");
    let counter = document.querySelector("#counter");
    const ratio = 0.5625;

    gsap.set("#instructions, #dial", {xPercent: -50});
    gsap.set("#progressRing", {drawSVG:0});

    tl.to("#masker", {duration: 2, attr:{r:1600}, ease:"power2.in"});
    tl.reversed(true);

    function mouseHandler() {
      tl.reversed(!tl.reversed());
    }

    function getPoint(evt){
      pt.x = evt.clientX; 
      pt.y = evt.clientY;
      return pt.matrixTransform(svg.getScreenCTM().inverse());
    }

    function mouseMove(evt) {
      let newPoint = getPoint(evt);
      gsap.set("#dot", {attr:{cx:newPoint.x, cy:newPoint.y}});
      gsap.to("#ring, #masker", 0.88, {attr:{cx:newPoint.x, cy:newPoint.y}, ease:"power2.out"});
    }

    function onUpdate() {
      let prog = (tl.progress() * 100);
      // gsap.set("#progressRing", {drawSVG:prog + "%"});
      counter.textContent = prog.toFixed();
    }
    const frame = document.querySelector('.page')
    function newSize() {
      let w = frame.offsetWidth ;
      let h = frame.offsetHeight;
      if (w > h * (16/9) ) {
        gsap.set("#demo", { attr: { width: w, height: w * ratio } });
      } else {
        gsap.set("#demo", { attr: { width: h / ratio, height: h } });
      }
      let data = svg.getBoundingClientRect();
      gsap.set("#demo", {x:w/2 - data.width/2});
      gsap.set("#demo", {y:h/2 - data.height/2});
    }

    frame.addEventListener("mousedown", mouseHandler);
    frame.addEventListener("mouseup", mouseHandler);
    frame.addEventListener("mousemove", mouseMove);

    newSize();
    frame.addEventListener("resize", newSize);
    
  },
  methods:{
    nextKlimts(){
      this.$store.dispatch('page/pageChange',1)
      this.$router.push({path:'klimts'})
    },
    hintView(){
      this.hintflag = !this.hintflag
    },
    originalView(){
      this.originalflag = !this.originalflag;
      // console.log(document.querySelector('#demo').style)
      document.querySelector('#demo').style.boxShadow = "0 0 0 0 rgba(202, 202, 202, 0.548);"
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Prata&display=swap');
@import url('https://fonts.googleapis.com/css?family=Playfair+Display:400,400i,700,700i,900,900i');
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i');

.body{
  padding:2rem;
  background-color: #28353c;
  height: 100vh;

}
.page{
  padding: 3% 5%;
  margin: 0 auto;
  font-family: "Signika", sans-serif;
  background-color: #28353c;
  height: 95vh;
  width: 100%;
  overflow: hidden;
  color: white;
  z-index: 1;
  display: flex;
  flex-direction: row !important;
}
.description{
  min-width: 44%;
  height: 800px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.desc-main{
  margin-top:20%
}
.desc-main__title{
  color:#FFD700;
  font-family:'Playfair Display', serif;
  letter-spacing: 3px;
}
.desc-main__subtitle{
  font-size: 1.5rem;
  margin:1rem 0;
}
.desc-main__description{
  line-height: 22px;
}
.desc-footer{
  display: flex;
  align-items: center;
}
.desc-footer-info{
  cursor: pointer;
  color:aliceblue;
  margin-right: 20px;
}
.desc-footer-info:hover{
  color:#fe3901
}
.desc-footer-info-icon{
  font-size:1.5rem;
}
.next-view{
  position:absolute;
  right: 5.5%;
  bottom: 50%;
  display: flex;
  cursor: pointer;
}
.next-view:hover{
  color:#fe3901;
}
.next-view-icon{
  font-size: 2rem;
}
.original-view{
  position:absolute;
  bottom: 17%;
  right: 4.9%;
  display: flex;
  cursor: pointer;
}
.original-view:hover{
  color:#fe3901;
}
.original-view-icon{
  font-size: 2rem;
}


p {
  margin: 0;
  text-align: center;
  white-space: nowrap;
}

* {
  box-sizing: border-box;
}

#demo {
  cursor: none;
  width:800px !important;
  height: 800px !important;
  transform: translate(0,0) !important;
  box-shadow: 0px 5px 40px 0 rgba(202, 202, 202, 0.548);
}

#instructions {
  padding: 12px;
  bottom: 20px;
  background: rgba(0, 0, 0, 0.75);
  left: 50%;
  cursor: none;
  padding-top: 100px;
  user-select: none;
  border-radius: 4px;
}

#dial {
  top: 0;
  left: 50%;
}

</style>

<style lang="scss" scoped>
// DIMENSIONS
$width: 100px; // Button With
$outerDiamondHeight: $width / 3; //Button Height
$outerDiamondWidth: $width / 2;
$innerDiamondHeight: $outerDiamondHeight - 1;
$innerDiamondWidth: $outerDiamondWidth - 1;
$arrowSize: $width / 6;

// COLORS
$borderColor: #333;
$backgroundColor: white;

//TRANSITION
$transition: all 0.25s ease;

.diamond-container {
  z-index:1000;
  width: $width;
  position: absolute;
  top:45%; right: 3%;
  transform: translate(-10%);
  cursor: pointer;
  
  // CLEARFIX
  &:after {
    content:'';
    display: table;
    height: 0;
    clear: both;
  }
  
  // DIAMOND BUTTON - LEFT&RIGHT
  .diamond {
    position: relative;
    width: $outerDiamondWidth;
    height: $outerDiamondHeight*2;
    float: left;
    overflow: hidden;

    &:after, &:before {
      border: solid transparent;
      content: ' ';
      position: absolute;
      width: 0%; height: 0%;
      transition: $transition;
    }

    &:after {
      border-width: $innerDiamondHeight 0 $innerDiamondHeight $innerDiamondWidth;
      border-left-color: $backgroundColor;
      top: 1px; left: -1px;
    }
    &:before {
      border-width: $outerDiamondHeight 0 $outerDiamondHeight $outerDiamondWidth;
      border-left-color: $borderColor;
    }

    &.left {
      &:after {
        border-width: $innerDiamondHeight $innerDiamondWidth $innerDiamondHeight 0;
        border-left-color: transparent;
        border-right-color: $backgroundColor;
        left: 2px;
      }
      &:before {
        border-width: $outerDiamondHeight $outerDiamondWidth $outerDiamondHeight 0;
        border-left-color: transparent;
        border-right-color: $borderColor;
      } 
    }
  }
  
  // ARROW 
  .arrow {
    width: $arrowSize; height: $arrowSize;
    border: 1px solid $borderColor;
    border-left: none;
    border-bottom: none;  
    position: absolute;
    top:50%; left: 52%;
    transform: translate(-50%, -50%) rotate(45deg);
    transition: $transition;
    &:after {
      content: "";
      width: 160%; border-top: 1px solid $borderColor;
      position: absolute;
      top: 0; right: 0;
      transform: rotate(-45deg);
      transform-origin: top right;
      transition: inherit;
    }
  }
  
  // HOVER EFFECT
  &:hover {

    .diamond {
      border: #ccc;
      &:after { border-left-color: $borderColor; }
      &.left:after {  border-right-color: $borderColor; }
    }
    .arrow {
      border-top: 1px solid $backgroundColor;
      border-right: 1px solid $backgroundColor;
      transform: translate(-50%, -50%) rotate(405deg);
      &:after {
        border-top: 1px solid $backgroundColor;
      }
    }
  }
  
}
</style>
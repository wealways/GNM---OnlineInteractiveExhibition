<template>
  <div class="page insideWrapper">
    <canvas class="coveringCanvas"></canvas>
    <div class="description ">
      <div>
        클림트 - 키스 
      </div>
      <div>
        원형, 네모, 직선과 곡선 등 기하학 문양과 함께<br> 
        금박 무늬 등 화려한 색체를 앞세운 클림트만의 화풍
      </div>
      <br>
      <div>
        여러분의 마우스를 통해<br>
        클림트의 화풍을 경험해보세요
      </div>
      <div class="hintBtn" v-if="!hintflag" @click="hintflag=true">
        힌트
      </div>
      <div v-if="hintflag">
        <div class="hintBtn" @click="hintflag=false">숨기기</div>
        그림위에 마우스를 올려놓고 <br>
        길게 눌러보세요. <br> 
        키스의 모든 색감을 볼 수 있습니다.
      </div>
    </div>
    <svg id="demo" xmlns="http://www.w3.org/2000/svg" x="0" y="0" left="0" width="0" height="0" viewBox="0 0 900 900" class="">
      <defs>
      <radialGradient id="maskGradient">
        <stop offset="50%" stop-color="#fff"/>
        <stop offset="100%" stop-color="#000"/>
      </radialGradient>
      <mask id="theMask">
      <circle id="masker" r="100" fill="url(#maskGradient)" cx="800" cy="450" />
      </mask>
      </defs>

        <image id="lines" xlink:href="https://i.ibb.co/jkqJsth/klimt-sketch.png" x="0" y="0" width="900" height="900"  class=""/>
        <g id="maskReveal" mask="url(#theMask)" class="discoball" > 
          <image id="regular" xlink:href="https://i.ibb.co/HzsVFPC/klimt.jpg" x="0" y="0" width="900" height="900" />
        </g>
        <!-- <circle id="ring" r="10" fill="none" stroke="#dc143c" stroke-width="2" cx="800" cy="450" /> -->
        <circle id="dot" r="4" fill="#dc143c" cx="800" cy="450" />
    </svg>

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
    
    <!-- <div style="width:800px;height:800px;background:red;">
    </div> -->
  </div>
</template>

<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/2.0.1/TweenLite.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/2.0.1/TimelineMax.min.js"></script>
<script>
import { gsap,TimelineMax } from 'gsap';
import anime from 'animejs/lib/anime.es.js';

export default {
  name:'KlimtInteractive',
  data(){
    return {
      hintflag:false,
    }
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

    // console.log(original)
    function mouseDbClick() {
      const original = document.querySelector('#maskReveal')
      original.classList.toggle('discoball')
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
      console.log(data)
      gsap.set("#demo", {x:w/2 - data.width/2});
      gsap.set("#demo", {y:h/2 - data.height/2});
    }


    // 폭죽
      var canvasEl = document.querySelector('.coveringCanvas');
      var ctx = canvasEl.getContext('2d');
      // this.vueCanvas = ctx;
      var numberOfParticules = 30;
      var pointerX = 0;
      var pointerY = 0;
      var tap = ('ontouchstart' in window || navigator.msMaxTouchPoints) ? 'touchstart' : 'mousedown';
      // var tap = ('ontouchstart' in window || navigator.msMaxTouchPoints) ? 'touchstart' : 'mousedown';
      // var colors = ['#FF1461', '#18FF92', '#5A87FF', '#FBF38C'];
      var colors = ['#FFDF00', '#D4AF37', '#CFB53B', '#C5B358', '#E6BE8A', '#996515'];
      var colors = ['#FAFAD2', '#EEE8AA', '#F0E68C', '#DAA520', '#FFD700', '#FFA500', '#FF8C00', '#CD853F', '#D2691E', '#8B4513'];

      function setCanvasSize() {
        canvasEl.width = window.innerWidth * 2;
        canvasEl.height = window.innerHeight * 2;
        canvasEl.style.width = window.innerWidth + 'px';
        canvasEl.style.height = window.innerHeight + 'px';
        canvasEl.getContext('2d').scale(2, 2);
      }

      function updateCoords(e) {
        pointerX = e.clientX || e.touches[0].clientX;
        pointerY = e.clientY || e.touches[0].clientY;
      }

      function setParticuleDirection(p) {
        var angle = anime.random(0, 360) * Math.PI / 180;
        var value = anime.random(50, 180);
        var radius = [-1, 1][anime.random(0, 1)] * value;
        return {
          x: p.x + radius * Math.cos(angle),
          y: p.y + radius * Math.sin(angle)
        }
      }

      function createParticule(x,y) {
        var p = {};
        p.x = x;
        p.y = y;
        p.color = colors[anime.random(0, colors.length - 1)];
        p.radius = anime.random(16, 32);
        p.endPos = setParticuleDirection(p);
        p.draw = function() {
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius, 0, 2 * Math.PI, true);
          ctx.fillStyle = p.color;
          ctx.fill();
        }
        return p;
      }

      function createCircle(x,y) {
        var p = {};
        p.x = x;
        p.y = y;
        p.color = '#FFF';
        p.radius = 0.1;
        p.alpha = .5;
        p.lineWidth = 6;
        p.draw = function() {
          ctx.globalAlpha = p.alpha;
          ctx.beginPath();
          ctx.arc(p.x, p.y, p.radius, 0, 2 * Math.PI, true);
          ctx.lineWidth = p.lineWidth;
          ctx.strokeStyle = p.color;
          ctx.stroke();
          ctx.globalAlpha = 1;
        }
        return p;
      }

      function renderParticule(anim) {
        for (var i = 0; i < anim.animatables.length; i++) {
          anim.animatables[i].target.draw();
        }
      }

      function animateParticules(x, y) {
        var circle = createCircle(x, y);
        var particules = [];
        for (var i = 0; i < numberOfParticules; i++) {
          particules.push(createParticule(x, y));
        }
        anime.timeline().add({
          targets: particules,
          x: function(p) { return p.endPos.x; },
          y: function(p) { return p.endPos.y; },
          radius: 0.1,
          duration: anime.random(1200, 1800),
          easing: 'easeOutExpo',
          update: renderParticule
        })
          .add({
          targets: circle,
          radius: anime.random(80, 160),
          lineWidth: 0,
          alpha: {
            value: 0,
            easing: 'linear',
            duration: anime.random(600, 800),  
          },
          duration: anime.random(1200, 1800),
          easing: 'easeOutExpo',
          update: renderParticule,
          offset: 0
        });
      }

      var render = anime({
        duration: Infinity,
        update: function() {
          ctx.clearRect(0, 0, canvasEl.width, canvasEl.height);
        }
      });

      frame.addEventListener('mousedown', function(e) {
        console.log('hi')
        render.play();
        updateCoords(e);
        animateParticules(pointerX, pointerY);
      }, false);

      // autoClick();
      setCanvasSize();
      // window.addEventListener('resize', setCanvasSize, false);


    //폭죽의 끝



    frame.addEventListener("mousedown", mouseHandler);
    frame.addEventListener("mouseup", mouseHandler);
    frame.addEventListener("mousemove", mouseMove);
    // frame.addEventListener("dblclick", mouseDbClick);

    newSize();
    frame.addEventListener("resize", newSize);
    
  },
  methods:{
  }
}
</script>

<style scoped>
.page{
  padding: 0;
  margin: 0 auto;
  font-family: "Signika", sans-serif;
  background: #262626;
  height: 968.5px;
  /* height: 100%; */
  width: 100%;
  overflow: hidden;
  color: white;
  z-index: 1;
  display: flex;
}
.description{
  margin-top: 3%;
  margin-left: 5%;
  min-width: 45%;
  background-color: transparent;
  z-index: 4;
}
.hintBtn{
  cursor: pointer;
  color:#fe3901;
  font-size: 1rem;
  z-index: 500;
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
  position: absolute;
  width:900px !important;
  height: 900px !important;
  left:20%;
}

#instructions {
  position: absolute;
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
  position: absolute;
  top: 0;
  left: 50%;
}

@-webkit-keyframes hue {
  from {
    -webkit-filter: hue-rotate(0deg);
  }
  
  to {
    -webkit-filter: hue-rotate(360deg);
  }
}
.discoball {
  -webkit-animation-timing-function: linear;
  -webkit-animation-duration: 1s;
  -webkit-animation-name: hue;
  -webkit-animation-iteration-count: infinite;
  -webkit-animation-direction: alternate;
  
  background: lightgrey;
  /* border-radius: 200px; */
  /*border: 0px solid #fff;*/
  /* height: 200px; */
  /* width: 200px; */
  /* box-shadow: 0 3px 200px -3px #fff; */
}



.insideWrapper{ 
    position:relative;}
.coveredImage{ 
    position:absolute; top:0px; left:0px;
}
.coveringCanvas{ 
    width:100%; height:100%;
    position:absolute; top:0px; left:0px;
    background-color: transparent;
    z-index:2;
}



</style>
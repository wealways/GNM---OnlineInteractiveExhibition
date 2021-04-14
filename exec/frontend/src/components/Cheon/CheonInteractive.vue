<template>
  <div class="page">
    <div class="exhibition">
        <div id="title">작품을 완성해 보세요</div>
      <div class="frame">
        <div id='puz'>
          <i class='first' @drop='drop($event)' @dragover='allowDrop($event)' ></i>
          <i class='secon' @drop='drop($event)' @dragover='allowDrop($event)'></i>
          <i class='third' @drop='drop($event)' @dragover='allowDrop($event)'></i>
          <i class='fourt' @drop='drop($event)' @dragover='allowDrop($event)'></i>
          <i class='fifth' @drop='drop($event)' @dragover='allowDrop($event)'></i>
          <i class='sixth' @drop='drop($event)' @dragover='allowDrop($event)'></i>
          <i class='seven' @drop='drop($event)' @dragover='allowDrop($event)'></i>
          <i class='eight' @drop='drop($event)' @dragover='allowDrop($event)'></i>
          <i class='ninth' @drop='drop($event)' @dragover='allowDrop($event)'></i>
        </div>
        <div id='puzz'>
          <i class='first' draggable='true' @dragstart='drag($event)'></i>
          <i class='secon' draggable='true' @dragstart='drag($event)'></i>
          <i class='third' draggable='true' @dragstart='drag($event)'></i>
          <i class='fourt' draggable='true' @dragstart='drag($event)'></i>
          <i class='fifth' draggable='true' @dragstart='drag($event)'></i>
          <i class='sixth' draggable='true' @dragstart='drag($event)'></i>
          <i class='seven' draggable='true' @dragstart='drag($event)'></i>
          <i class='eight' draggable='true' @dragstart='drag($event)'></i>
          <i class='ninth' draggable='true' @dragstart='drag($event)'></i>  
        </div>
      </div>
    </div>
    <div>
    <div class='interior'>
      <a class='btn' href="#open-modal">
        <span class='insidebtn' style="font-size:18px;">
          <p class='hint'>HINT</p>
          <q-icon name="mdi-lightbulb-on-outline" class='bulbicon'></q-icon>
        </span>
      </a>
    </div>
    <div id="open-modal" class="modal-window">
      <div class='relativeclass'>
        <a href="#" title="Close" class="modal-close">Close</a>
        <img class="gr" src="../../assets/저작권.jpg" alt="">
      </div>
    </div>
    </div>
    <div @click="goExhibition" class="nextbtn">
      <div class="diamond-container">
      <div class="diamond left"></div>
      <div class="diamond right"></div>
      <div class="arrow"></div>
      </div>
    </div>
  </div>
</template>

<script>

var img = ["https://i.ibb.co/cQFkpgd/cheon.png"]


export default {
  name:'CheonInteractive',
  data() {
    return {
      fullWidth: false,
    }
  },
  mounted(){
 
    this.randomize()

    const fp = document.querySelectorAll('#puz i')
    fp.forEach(function(el){
      el.addEventListener('click', function(){
        if(document.querySelector('.clicked')){
          var c = document.querySelector('.clicked')
          if(c.classList.contains(el.classList)) {
            el.classList.add('dropped')
            c.classList.add('done')
            c.classList.toggle('clicked')

            if(document.querySelectorAll('.dropped').length == 9) {
              document.querySelector('#puz').classList.add('allDone')
              document.querySelector('#puz').style.border = 'none'  
              document.querySelector('#puz').style.animation = 'allDone 1s linear forwards'

              setTimeout(function(){
                this.reload()
                this.randomize()            
              },1500)
            } 
          }
        }    
      })
    })
  },
  methods:{
    goExhibition(){
      this.$router.push({path:'cheons'})
    },
    
    randomize: function () {
      var root = document.documentElement
      root.style.setProperty('--image','url('+img[0]+')')
      
      var ul = document.querySelectorAll('#puzz i');
      for(var i=0;i<ul.length;i++){
        if (i%2 == 0) {
          // ul[i].style.left = Math.random()*(window.innerWidth-800) + 'px'
          ul[i].style.right = Math.random()*(window.innerWidth-900) + 'px'
          ul[i].style.top = Math.random()*(window.innerHeight-800) + 'px'
        }
        else {
          ul[i].style.left = Math.random()*(window.innerWidth-900) + 'px'
          ul[i].style.top = Math.random()*(window.innerHeight-800) + 'px'
        }
      }
    },

    reload: function () {
      var done = document.querySelectorAll('.done')
      done.forEach(function(e){
        e.classList.toggle('done')
      })
      var dropped = document.querySelectorAll('.dropped')
      dropped.forEach(function(e){
        e.classList.toggle('dropped')
      })
      var allDone = document.querySelector('.allDone')
      allDone.style = ''
      allDone.classList.toggle('allDone')
    },
    
    // desktop drag and drop
    allowDrop: function(ev) {
      ev.preventDefault();
    },

    drag: function(ev) {
      ev.dataTransfer.setData("text", ev.target.className);  
    },
   
    drop: function(ev) {
      ev.preventDefault();
      let data = ev.dataTransfer.getData("text")

      if(ev.target.className == data){
        ev.target.classList.add('dropped')
        document.querySelector('.'+data+"[draggable='true']").classList.add('done')

        if(document.querySelectorAll('.dropped').length == 9) {
          document.querySelector('#puz').classList.add('allDone')
          document.querySelector('#puz').style.border = 'none'  
          document.querySelector('#puz').style.animation = 'allDone 1s linear forwards'  

          setTimeout(function(){
            this.reload()
            this.randomize()        
          },1500)
        }    
      }  
    },
  },
}
</script>

<style scoped>
:root {
  --color:lightgray;
  --border-radius:10px;
  --image:url("https://i.ibb.co/cQFkpgd/cheon.png");
}
.map{
  position: fixed;
  bottom:40%;
  left: 20%;
  padding:10px;
  background-color: transparent;
  color: rgba(0,0,0,0.5);
  background: rgba(255, 251, 4, 0.3);
  border-radius: 50%;
}
.map:hover{
  color: rgba(0,0,0,0.8);
  background: rgba(247, 231, 7, 0.6);
  font-size:58px;
}
.relativeclass{
  position: relative;
  height: 60%;
}
.gr {
  margin-top:5%;
  max-width: 90%; 
  max-height:90%;
  height: auto;
}

.mapwrapper {
  overflow-y: hidden;
}
</style>
<style>
.page{
  padding: 0;
  margin: 0 auto;
  font-family: "Signika", sans-serif;
  background:  white;
  height: 980px;
  width: 100%;
  z-index: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.exhibition{
  position: relative;
  top: -15%;
}
#title{
  padding: 5%;
  text-align: center;
  font-size: 1.25rem;
  font-weight: 700;
  font-family: 'Noto Sans KR';
  animation-name: twinkling;
  animation-duration: 3s;
}
@keyframes twinkling{
  0% {color: black;}
  50%{color: white;}
  100% {color: black;}
}

.frame{
  border: 8px solid black;
  width: 506px;
  height: 500px;
  background: rgba(244, 248, 207, 0.719);
  box-shadow: 0px 0px 15px rgba(15, 15, 15, 0.171);
}

#puz, #puzz {
  position: relative;
  border-radius: var(--border-radius) ;    
  user-select:none;
}
#puz {
  width:306px;
  height:300px;
  position:relative;
  top:50%;
  left:50%;
  transform:translate(-50%,-50%);
  border:3px dashed lightgray; 
  overflow:hidden;
  background: white;
}
#puzz {
  left:0;
  top:0;
  border:0;
}

#puz i {
  float:left;
  width:100px;
  height:100px;
  outline:1px dashed lightgray;
}

#puzz i {
  position:absolute;
  width:100px;
  height:100px;
  background:var(--color);
  background-image:var(--image);
  background-size:300px 300px;
  cursor:move;
  box-shadow:0 0 10px rgba(0,0,0,.25);
}

.first {
  border-top-left-radius:var(--border-radius);
  background-position:left top !important;
}
.secon {
  background-position:center top !important;
}
.third {
  background-position:right top !important;
}
.fourt {
  background-position:left center !important;
}
.fifth {
  background-position:center center !important;
}
.sixth {  
  background-position:right center !important;
}
.seven {
  background-position:left bottom !important;
}
.eight {
  background-position:center bottom !important;
}
.ninth {
  border-bottom-right-radius:var(--border-radius);
  background-position:right bottom !important;
}

.clicked {
  box-shadow:0 0 0 4px gray !important;
}

.dropped {
  background:var(--color);
  background-image:var(--image);
  background-size:300px 300px;
}
.done {
  opacity:0;
  pointer-events:none;
}

.allDone {
  animation:allDone 1s linear forwards;
  border:3px solid lightgray !important;
}
.allDone i {
  outline:0 !important;
}

@keyframes allDone {
  50% { transform:translate(-50%,-50%) scale(1.2); }
}

#clicks {
  font-size:8px;
  font-family:monospace;
  position:absolute;
  bottom:5px;
  right:5px;
}

#rightarrow{
  position: absolute;
  top: 90%;
  right: 10%;
}
.nextbtn:hover {
  cursor: pointer;
}

</style>

<style lang="scss" scoped>
.modal-window {
  position: fixed;
  background-color: rgba(255, 255, 255, 0.25);
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 999;
  visibility: hidden;
  opacity: 0;
  pointer-events: none;
  transition: all 0.3s;
  &:target {
    visibility: visible;
    opacity: 1;
    pointer-events: auto;
  }
  & > div {
    width: 400px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 2em;
    background: white;
  }
  header {
    font-weight: bold;
  }
  h1 {
    font-size: 150%;
    margin: 0 0 15px;
  }
}

.modal-close {
  color: #aaa;
  line-height: 50px;
  font-size: 80%;
  position: absolute;
  right: 0;
  text-align: center;
  top: 0;
  width: 70px;
  text-decoration: none;
  &:hover {
    color: black;
  }
}
.modal-window {
  & > div {
    border-radius: 1rem;
  }
}

.btn {
  position: absolute;
  left:48%;
  top: 2%;
  padding: 0px 17px;
  border-radius: 1rem;
  color:#aaa;
  background-color: rgba(243, 207, 4, 0.479);
  text-decoration: none;
  height: 35px;
}
.insidebtn {
  display:flex;
}
.bulbicon {
  padding-top:7px;
  padding-bottom:7px;
  margin-left: 5px;
}
.hint {
  padding-top:6px;
  padding-bottom:6px;
  font-size: 15px;
  font-family: 'Noto Sans KR';
}
.btn:hover{
  background-color: rgba(243, 207, 4, 0.8);

}
// DIMENSIONS
$width: 150px; // Button With
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
  bottom:10%; right: 10%;
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
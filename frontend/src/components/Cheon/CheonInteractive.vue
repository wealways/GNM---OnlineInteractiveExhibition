<template>
  <div class="page">
    <div class="exhibition">
      <div id="title">작품을 완성해 보세요.</div>
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
    <div @click="goExhibition" class="nextbtn">
      <span style="font-size:50px;">
          <q-icon :to='"/cheons"' target="_blank" id="rightarrow" name="mdi-chevron-double-right"></q-icon>
      </span>
    </div>
  </div>
</template>

<script>

var img = ["https://i.ibb.co/cQFkpgd/cheon.png"]

export default {
  name:'CheonInteractive',
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
      // for (var i = ul.children.length; i >= 0; i--) {
      //   ul.appendChild(ul.children[Math.random() * i | 0]);    
      // }
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
  /* --image:url("../../assets/cheon_pic.png"); */
  --image:url("https://i.ibb.co/cQFkpgd/cheon.png");
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
  font-size: 2rem;
  font-weight: bolder ;
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
/*   border-top-right-radius:var(--border-radius); */
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
/*   border-bottom-left-radius:var(--border-radius); */
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
<template>
  <div class="page">
    <div class="description">
      천경자 인터렉티브 페이지
    </div>
    
      <div id='puz'>
        <i class='first' ondrop='drop(event)' ondragover='allowDrop(event)' ></i>
        <i class='secon' ondrop='drop(event)' ondragover='allowDrop(event)'></i>
        <i class='third' ondrop='drop(event)' ondragover='allowDrop(event)'></i>
        <i class='fourt' ondrop='drop(event)' ondragover='allowDrop(event)'></i>
        <i class='fifth' ondrop='drop(event)' ondragover='allowDrop(event)'></i>
        <i class='sixth' ondrop='drop(event)' ondragover='allowDrop(event)'></i>
        <i class='seven' ondrop='drop(event)' ondragover='allowDrop(event)'></i>
        <i class='eight' ondrop='drop(event)' ondragover='allowDrop(event)'></i>
        <i class='ninth' ondrop='drop(event)' ondragover='allowDrop(event)'></i>
      </div>
      <div id='puzz'>
        <i class='first' draggable='true' ondragstart='drag(event)'></i>
        <i class='secon' draggable='true' ondragstart='drag(event)'></i>
        <i class='third' draggable='true' ondragstart='drag(event)'></i>
        <i class='fourt' draggable='true' ondragstart='drag(event)'></i>
        <i class='fifth' draggable='true' ondragstart='drag(event)'></i>
        <i class='sixth' draggable='true' ondragstart='drag(event)'></i>
        <i class='seven' draggable='true' ondragstart='drag(event)'></i>
        <i class='eight' draggable='true' ondragstart='drag(event)'></i>
        <i class='ninth' draggable='true' ondragstart='drag(event)'></i>  
      </div>
    

  </div>
</template>

<script>
let img = ['https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3dd97bd9-f6f2-48a3-963e-104454bd460c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210329T024727Z&X-Amz-Expires=86400&X-Amz-Signature=88fff8efa8b89e7fac053fe3dc4a2b4c9d72813ef091b3547e45ac0f6f90db1f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22',
           'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3dd97bd9-f6f2-48a3-963e-104454bd460c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210329T024727Z&X-Amz-Expires=86400&X-Amz-Signature=88fff8efa8b89e7fac053fe3dc4a2b4c9d72813ef091b3547e45ac0f6f90db1f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22',
           'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3dd97bd9-f6f2-48a3-963e-104454bd460c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210329T024727Z&X-Amz-Expires=86400&X-Amz-Signature=88fff8efa8b89e7fac053fe3dc4a2b4c9d72813ef091b3547e45ac0f6f90db1f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22',
           'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3dd97bd9-f6f2-48a3-963e-104454bd460c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210329T024727Z&X-Amz-Expires=86400&X-Amz-Signature=88fff8efa8b89e7fac053fe3dc4a2b4c9d72813ef091b3547e45ac0f6f90db1f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22',
           'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3dd97bd9-f6f2-48a3-963e-104454bd460c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210329T024727Z&X-Amz-Expires=86400&X-Amz-Signature=88fff8efa8b89e7fac053fe3dc4a2b4c9d72813ef091b3547e45ac0f6f90db1f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22',
           'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3dd97bd9-f6f2-48a3-963e-104454bd460c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210329T024727Z&X-Amz-Expires=86400&X-Amz-Signature=88fff8efa8b89e7fac053fe3dc4a2b4c9d72813ef091b3547e45ac0f6f90db1f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22',
           'https://s3.us-west-2.amazonaws.com/secure.notion-static.com/3dd97bd9-f6f2-48a3-963e-104454bd460c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210329%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210329T024727Z&X-Amz-Expires=86400&X-Amz-Signature=88fff8efa8b89e7fac053fe3dc4a2b4c9d72813ef091b3547e45ac0f6f90db1f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22',
            ]
let old = 5 


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
    randomize: function () {
      let root = document.documentElement
      root.style.setProperty('--image','url('+img[old]+')')
      old++
      if(old > 5) {
        old = 0
      }  
      var ul = document.querySelectorAll('#puzz i');
      for(var i=0;i<ul.length;i++){
        ul[i].style.left = Math.random()*(window.innerWidth-100) + 'px'
        ul[i].style.top = Math.random()*(window.innerHeight-100) + 'px'
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
      console.log(ev)
      ev.dataTransfer.setData("text", ev.target.className);  
    },

    drop: function(ev) {
      ev.preventDefault();
      var data = ev.dataTransfer.getData("text")

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

<style>
.page{
  padding: 0;
  margin: 0 auto;
  font-family: "Signika", sans-serif;
  background:  #939597;
  height: 980px;
  width: 100%;
  overflow: hidden;
  color: rgb(255, 255, 255);
  z-index: 1;
  display: flex;
}

.description{
  margin-top: 3%;
  margin-left: 5%;
  min-width: 45%;
}
:root {
  --color:lightgray;
  --border-radius:10px;
  --image:url('https://media.gettyimages.com/vectors/cute-cartoon-dachshunds-in-love-vector-id865392634?s=2048x2048');
}


#puz, #puzz {
  position:absolute;
  border-radius:var(--border-radius) 0 var(--border-radius) 0;    
  user-select:none;
}
#puz {
  width:306px;
  height:300px;
  position:absolute;
  top:50%;
  left:50%;
  transform:translate(-50%,-50%);
  border:3px dashed lightgray;
  overflow:hidden;
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
</style>
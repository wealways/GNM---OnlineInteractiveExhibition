<template>
  <div data-role="page" id="home">
    <div class='ui-content'>
      <div class='icon-scroll'>
        <div class='scrolltext' style="color:white; font-family:'Cinzel">scroll</div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name:'MoneInteractive',
  methods:{
    handleScroll(event){
      let delta = event.deltaY
      if(delta>0){
        if(this.$route.path === '/monet') {
          this.$router.push({path:'/monets'})
        }
      }
    }
  },
  mounted(){
    window.addEventListener('wheel', this.handleScroll);
    let z = 2;
    $(document).on('mouseover', (e)=> {
      const mx = e.pageX;
      const my = e.pageY;
      z = z + 1;
      _wave(mx, my, z);
    });

    function _wave(i, j, k) {
      $('.ui-content').prepend(
        '<div class="wave-position water' + k + '" style="z-index:' + k + ';top:' + (j - 150) + 'px;left:' + (i - 150) + 'px;">' +
        '<div class="wave-body">' +
        '<div id="wave" class="wave wave5"></div>' +
        '<div id="wave" class="wave wave4"></div>' +
        '<div id="wave" class="wave wave3"></div>' +
        '<div id="wave" class="wave wave2"></div>' +
        '<div id="wave" class="wave wave1"></div>' +
        '<div id="wave" class="wave wave0"></div>' +
        '</div>' +
        '</div>'
      );
      setTimeout(() => {
        $('.water' + k).remove();
      }, 3000);
    }
  }
}
</script>
<style scoped>
.scrolltext{
  position: absolute;
  bottom:100%;
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
  content: '';
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
<style>
html {
    overflow: scroll;
    overflow-x: hidden;
}
::-webkit-scrollbar {
    width: 0;  /* Remove scrollbar space */
    background: transparent;  /* Optional: just make scrollbar invisible */
}
/* Optional: show position indicator in red */
::-webkit-scrollbar-thumb {
    background: #FF0000;
}
</style>
<style lang="sass" scoped>
html,body,#home,.ui-content
  margin: 0
  padding: 0
  height: 101vh
  width: 100vw
  cursor: pointer
</style>

<style lang="sass">
#home
  background: url("../../assets/waterlily3.jpeg") no-repeat
  background-attachment: fixed
  background-position: center center
  position: relative
.wave-position
  position: absolute
  width: 300px
  height: 300px
.wave-body
  position: relative
  width: 100%
  height: 100%
.wave
  position: absolute
  top: calc((100% - 15px)/2)
  left: calc((100% - 15px)/2)
  width: 15px
  height: 15px
  border-radius: 300px
  background: url("../../assets/waterlily3.jpeg") no-repeat
  background-attachment: fixed
  background-position: center center
.wave0
  z-index: 2
  background-size: auto 106%
  animation: w 1s forwards
.wave1
  z-index: 3
  background-size: auto 102%
  animation: w 1s .2s forwards
.wave2
  z-index: 4
  background-size: auto 104%
  animation: w 1s .4s forwards
.wave3
  z-index: 5
  background-size: auto 101%
  animation: w 1s .5s forwards
.wave4
  z-index: 6
  background-size: auto 102%
  animation: w 1s .8s forwards
.wave5
  z-index: 7
  background-size: auto 100%
  animation: w 1s 1s forwards
@keyframes w
  0%
    top: calc((100% - 15px)/2)
    left: calc((100% - 15px)/2)
    width: 15px
    height: 15px
  100%
    top: calc((100% - 300px)/2)
    left: calc((100% - 300px)/2)
    width: 300px
    height: 300px
  
</style>

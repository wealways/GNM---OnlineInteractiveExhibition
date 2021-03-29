<template>
  <div data-role="page" id="home">
    <div class='ui-content'></div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name:'MoneInteractive',
  mounted(){
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

<style lang="sass">
html,body,#home,.ui-content
  margin: 0
  padding: 0
  height: 100vh
  width: 100vw
  overflow: hidden
  cursor: pointer
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

<template>
  <div>
    <h1 id="monetname">Claude</h1>
    <h1 id="monetname2">Monet</h1>
    <span id="sentence">"물체가 지닌 고유한 색은 없다. 색은 빛에 따라서 변화할 뿐이다."</span>
    <img src="../../assets/mone.jpg" alt="monetface" id="bg">
    <div @click="realstart" class="nextbtn">
      <span style="font-size:50px;">
          <q-icon :to='"/monetphoto"' target="_blank" id="rightarrow" name="mdi-chevron-double-right"></q-icon>
      </span>
    </div>

  </div>
</template>

<script>
import $ from 'jquery'
export default {
  name:'MoneIntro',
  mounted(){
    var theWindow = $(window),
    $bg = $("#bg"),
    aspectRatio = $bg.width() / $bg.height();
    var imgWidth = $bg.width();

    function resizeBg() {
        var heightDifference = (theWindow.height() - $bg.height()) / 2;

        if ((theWindow.width() / theWindow.height()) < aspectRatio) {
            $bg.removeClass().addClass('bgheight');
            $bg.css("margin", heightDifference + "px 0 0 -" + imgWidth / 2 + "px");
        } else {
            $bg.removeClass().addClass('bgwidth');
            $bg.css("margin", heightDifference + "px 0 0 0");
        }
    }
    theWindow.resize(resizeBg).trigger("resize");
  },
  methods:{
    realstart(){
      this.$router.push({path:'monetphoto'})
    }
  }
}
</script>

<style scoped>
.nextbtn:hover {
  cursor: pointer;
}
body, html {
  overflow: hidden;
}
#monetname{
  position: absolute;
  top: 20%;
  left: 5%;
}
#monetname2{
  position: absolute;
  top: 30%;
  left: 5%;
}
#sentence{
  position: absolute;
  top: 70%;
  left: 4%;
}
#bg {
  position: fixed;
  top: 0;
  right: 0;
  height: 80vh;
}
#rightarrow{
  position: absolute;
  top: 50%;
  right: 4%;
}
</style>
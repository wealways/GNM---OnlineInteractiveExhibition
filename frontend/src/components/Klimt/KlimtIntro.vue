<template>
<<<<<<< HEAD
  <div>

    <h1 id="firstname">Gustav<br>Klimt</h1>
=======
  <div style="background-color:#28353c;">
    <h1 id="firstname" style="color:#fff;">Gustav<br>Klimt</h1>
>>>>>>> dcb941ddbd33f16216eeb3b7ae5169f5cf5939fa
    <img src="../../assets/images/klimtintro.png" alt="klimtface" id="bg">
    <span id="sentence" style="color:#fff;font-size:1rem;"></span>
    <div @click="realstart">
      <span style="font-size:50px;cursor:pointer;">
          <q-icon target="_blank" id="rightarrow" name="mdi-chevron-double-right" style="color:#eee8aa"></q-icon>
      </span>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'
import korTyping from '@/plugins/korTyping'
export default {
  name:'KlimtIntro',
  mounted(){
    korTyping('#sentence','" 예술은 당신의 생각들을 둘러싼 한 줄기 선입니다. "')
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
      this.$router.push({path:'klimtphoto'})
    }
  }
}
</script>

<style scoped>
body, html {
  overflow: hidden;
  height: 100%;
  width: 100%;
}
#firstname{
  position: absolute;
  text-align: right;
  top: 20%;
  right: 5%;
}
#sentence{
  position: absolute;
  top: 70%;
  right: 4%;
}
#bg {
  position: fixed;
  top: 0;
  left: 0;
  height: 80vh;
}
#rightarrow{
  position: absolute;
  top: 50%;
  right: 4%;
}
</style>
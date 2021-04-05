<template>
  <div>
    <h1 id="englishname">Cheon Gyeongja</h1>
    <h1 id="koreaname">천경자</h1>
    <span id="sentence">"내 과거를 열심히 살게 해 준 원동력은<br>'꿈'과 '사랑'과 '모정' 세 가지 요소였다."</span>
    <img src="../../assets/cheon.png" alt="cheonGyeongja" id="bg">
    <div @click="realstart" class="nextbtn">
      <span style="font-size:50px;">
          <q-icon :to='"/cheonphoto"' target="_blank" id="rightarrow" name="mdi-chevron-double-right"></q-icon>
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
      this.$router.push({path:'cheonphoto'})
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
#englishname{
  position: absolute;
  top: 20%;
  left: 3%;
  font-size: 3rem;
  color: rgba(192, 192, 192, 0.829);
  /* text-shadow: 5px 5px 5px lightgrey ; */
}
#koreaname{
  position: absolute;
  top: 30%;
  left: 5%;
  text-shadow: 5px 5px 5px lightgrey ;
}
#sentence{
  position: absolute;
  top: 70%;
  left: 10%;
  line-height: 180%;
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
  color: white;
}
</style>
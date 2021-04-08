<template>
  <div>
  <div style="background-color:#28353c;">
    <h1 id="firstname">Gustav<br>Klimt</h1>
  </div>
    <img src="../../assets/images/klimtintro.png" alt="klimtface" id="bg">
    <span id="sentence" style="color:#fff;font-size:1rem;"></span>
    <div @click="realstart" class="nextbtn">
      <div class="diamond-container">
       <div class="diamond left"></div>
       <div class="diamond right"></div>
       <div class="arrow"></div>
      </div>
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
@import url('https://fonts.googleapis.com/css2?family=Prata&display=swap');
body, html {
  overflow: hidden;
  height: 100%;
  width: 100%;
}
#firstname{
  font-family:'Playfair Display', serif;
  position: absolute;
  text-align: right;
  top: 20%;
  right: 5%;
  color:#FFD700;
  letter-spacing: 3px;
}
#sentence{
  text-align: left;
  position: absolute;
  top: 70%;
  right: 4%;
  width:345px;
  font-size: 18px;
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
  top:58%; right: 3%;
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
<template>
  <div class='intromone'>
    <h1 id="monetname">Claude</h1>
    <h1 id="monetname2">Monet</h1>
    <span id="sentence">"물체가 지닌 고유한 색은 없다. 색은 빛에 따라서 변화할 뿐이다."</span>
    <div id="bg"></div>
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
@import url('https://fonts.googleapis.com/css?family=Playfair+Display:400,400i,700,700i,900,900i');
.intromone {
  position: relative;
  height: 100vh;
  overflow: hidden;
}
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
  font-family: 'Playfair Display';
}
#monetname2{
  position: absolute;
  top: 35%;
  left: 5%;
  font-family: 'Playfair Display';
}
#sentence{
  position: absolute;
  top: 70%;
  left: 5%;
  font-size: 18px;
  font-weight: 600;
  color: rgba(0,0,0,0.7);
}
#bg {
  background-image: url('../../assets/mone.jpg');
  height: 70vh;
  width: 60vw;
  order: 2;
  align-self: flex-end;
  background-repeat: no-repeat;
  background-size: cover;
  position:relative;
  transform: translateX(70%);
}

</style>
<style lang="scss" scoped>
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
  width: $width;
  position: absolute;
  top:45%; right: 1%;
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
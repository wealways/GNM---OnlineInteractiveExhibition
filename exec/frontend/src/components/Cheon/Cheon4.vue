<template>
    <div class="cheon4">
    <img id="img4" class="cheon4_pic slide-in" src="../../assets/저작권.jpg" alt="내 슬픈 생애의 22페이지">
    <div id="title4" class="title slide-in"><h3>내 슬픈 <br>생애의 22페이지</h3></div>
    <div id="desc4" class="desc slide-in">
      자신의 과거와 현재에 걸치는 자서전적인 이미지를 작품에 담고 있습니다.<br>
      천경자가 결혼을 하고 첫 딸을 낳았던 1945년 당시 22살이었던 천경자의 나이와 관계가 있습니다.<br>
      그녀의 작품 중에는 자화상을 비롯한 여인상이 많습니다.
    </div>
    <div @click="nextstart" class="nextbtn">
    <div class="diamond-container">
      <div class="diamond left"></div>
      <div class="diamond right"></div>
      <div class="arrow"></div>
    </div>
    </div>
    <div @click="nextstart" class="nextbtn">
      <div class="diamond-container">
       <div class="diamond left"></div>
       <div class="diamond right"></div>
       <div class="arrow"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cheon4',
  methods: {
    nextstart() {
      this.$router.push('/specialgallery')
    }
  },
  computed:{
    page(){
      return this.$store.state.page.page
    }
  },
  watch:{
    'page':function(){
      const img = document.querySelector('#img4')
      const desc = document.querySelector('#desc4')
      const title = document.querySelector('#title4')
      if(this.page===4){
        setTimeout(function(){
          img.classList.add('active-image');
        },500)
        setTimeout(function(){
          desc.classList.add('active-desc');
          title.classList.add('active-title');
        },700)
      } else {
        img.classList.remove('active-image');
        desc.classList.remove('active-desc');
        title.classList.remove('active-title');
      }
    }
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&family=Noto+Serif+KR:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i');

.cheon4 {
  position: relative;
    background-color: #eaeaea; 
}
.cheon4_pic{
  position: absolute;
  height: 100vh;
  right: 10% ;
  opacity:0;
  z-index: 500;
}

.title > h3 {
  font-family: 'Noto Serif KR', serif;
}

.title{
  position: absolute;
  top: 10% ;
  left: 3% ;
  text-shadow: 0 0 15px rgba(143, 143, 143, 0.658);
  opacity:0;
}

.desc{
  position: absolute;
  top: 60%; 
  left: 3%;
  width: 40%;
  font-size: 15px;
  word-spacing: 2px;
  line-height:170%;
  opacity:0;
  z-index: 500;
}

.slide-in {
  opacity: 0;
  transition: all 1s;
}

#desc4.slide-in {
  transform: translateY(100%) scale(0.95);
}

.active-desc {
  opacity: 1 !important;
  transform: translateY(30%) scale(1) !important;
}

#title4.slide-in {
  transform: translateY(-100%) scale(0.95);
}

.active-title {
  opacity: 1 !important;
  transform: translateY(0%) scale(1) !important;
}

.active-image {
  opacity: 1 !important;
  transform: translateX(0%) scale(1) !important;
}

#img4.slide-in {
  transform: translateX(100%) scale(0.95);
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
  z-index:1000;
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
  z-index:1000;
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
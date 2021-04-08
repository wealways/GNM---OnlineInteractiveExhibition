<template>
  <div class='monepage4'>
    <div class="carousel-item__info" id="info">
      <div class="carousel-item__container">
      <h2 class="carousel-item__subtitle">파라솔을 든 여인</h2>
      <h1 class="carousel-item__title">Woman with a Parasol - Madame Monet and Her Son</h1>
      <p class="carousel-item__description">모네의 대표작 ‘파라솔을 든 여인’입니다. 언덕 위에서 파라솔을 들고 서 있는 아내 카미유의 자태를 그려낸 역작입니다. </p>
      </div>
    </div>
    <img id='parasol' class="carousel-item__image" src="@/assets/parasol.jpg">
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
    name:"Mone4",
    computed: {
      page(){
        return this.$store.state.page.page
      }
    },
    watch:{
      'page':function(){

        const info = document.querySelector('#info')

        if(this.page===4){
          setTimeout(function(){
            info.classList.add('active');
          },500)
        }else{
          info.classList.remove('active');
        }
      }
    },
    methods:{
      nextstart(){
        this.$router.push({path:'startklimt'})
      }
    }    
}
</script>

<style scoped>
.monepage4{
  width: 100vw;
  height: 100vh;
  display: flex;   
  overflow: hidden;
  position: relative;
}
#parasol{
  z-index:-1;
  position: absolute;
  height: 100vh;
  width: 44vw;
}
.carousel-item__info {
  height: 100%;
  width: 0%;
  display: flex;
  flex-direction: column;  
  right:0;
  margin-top:10%;
  margin-left:50%;
  padding: 0 40px;
  transform: translateX(50%);
  transition: 2s all ease-in-out;
  flex-basis: 60%;
  width: 40%;

}

.active{ 
transition: 1s all ease-in-out;
transform: translateX(-10%);
}

.carousel-item__subtitle {
    letter-spacing: 3px;
    font-size: 15px;
    text-transform: uppercase;
    margin-left: 6px;
    color: #2C2C2C;    
    font-weight: 700;
}

.carousel-item__title {
    margin: 15px 0 0 0;
    font-family: 'Playfair Display', serif;
    font-size: 44px;
    line-height: 45px;
    letter-spacing: 3px;
    font-weight: 700;
    color: #2C2C2C;
}

.carousel-item__description {
    margin-top: 35px;
    font-size: 14px;
    font-weight: 300;
    color: #2C2C2C;
    line-height: 22px;
    margin-bottom: 35px;
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
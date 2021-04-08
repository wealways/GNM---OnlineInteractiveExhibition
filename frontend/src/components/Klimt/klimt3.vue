<template>
  <div class="section">
    <div class="img-set">
      <img id="img30" class="img__none" src="@/assets/images/klimt/Gustav_Klimt_030.jpg" alt="더 트리 오브 라이프">
      <img id="img32" class="img__none" src="@/assets/images/klimt/Gustav_Klimt_032.jpg" alt="더 트리 오브 라이프">
      <img id="img31" class="img__none" src="@/assets/images/klimt/Gustav_Klimt_031.jpg" alt="더 트리 오브 라이프">
    </div>
    <div id="desc__thethree" class="description slide-in">
      <h4 class="desc-main__title">
        Expectation,The three of life, fullfilment
      </h4>
      <div class="desc-main__subtitle">기다림, 생명의 나무, 성취 <span style="font-size:1rem;">(1905 - 1909)</span></div>
      <div class="desc-main__description">
        3개의 작품으로 나눠져 있으나 사실 하나의 작품입니다.나무의 사방으로 뻗어나간 가지들은 복잡하기 그지없는 삶의 면면들을 표현하고 있고 그 안에 꿈꾸듯 서 있는 두 연인은 삶을 초월하여 체념한 듯 서로에게 집착하며 서 있습니다.
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
  name:'Klimt3',
  computed:{
    page(){
      return this.$store.state.page.page
    }
  },
  watch:{
    'page':function(){
      const img1 = document.querySelector('#img30')
      const img2 = document.querySelector('#img32')
      const img3 = document.querySelector('#img31')
      const desc = document.querySelector('#desc__thethree')
      if(this.page===3){
        setTimeout(function(){
          img1.classList.add('active')
        },400)
        setTimeout(function(){
          img2.classList.add('active')
        },800)
        setTimeout(function(){
          img3.classList.add('active')
        },1200)
        setTimeout(() => {
          desc.classList.add('active')
        }, 600);
      }else{
        img3.classList.remove('active')
        img2.classList.remove('active')
        img1.classList.remove('active')
        desc.classList.remove('active')
      }
    }
  },
  methods:{
    nextstart(){
      this.$router.push({path:'startcheon'})
    }
  } 

}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Prata&display=swap');
@import url('https://fonts.googleapis.com/css?family=Playfair+Display:400,400i,700,700i,900,900i');
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i');

.section{
  padding: 3rem 5rem;
  color:aliceblue;
  position: relative;
}
.img-set{
  display: flex;
  justify-content: center;
}
.img__none{
  opacity: 0;
  transition: all 1s;
}
.section img{
  width:22%;
  height:600px;
  padding: 0 1rem;
}
.active {
  opacity: 1 !important;
}
.description{
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 20%;
}
.desc-main__title{
  color:#FFD700;
  font-family:'Playfair Display', serif;
  letter-spacing: 3px;
}
.desc-main__subtitle{
  font-size: 1.5rem;
  margin:0.5rem 0;
}
.desc-main__description{
  line-height: 22px;
}
.slide-in {
  opacity: 0;
  transition: all 1s;
}
.active{
  opacity: 1 !important;
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
<template>
  <div class='monepage'>
    <div class='carousel'>
      <div class="carousel-item carousel-item--1">
        <div class="carousel-item__image"></div>
        <div class="carousel-item__info">
          <div class="carousel-item__container">
          <h2 class="carousel-item__subtitle">Waterlily</h2>
          <h1 class="carousel-item__title">수련</h1>
          <p class="carousel-item__description">Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from 'jquery';

export default {
    name:"Mone1",
    mounted(){
      $(function(){
        $('.carousel-item').eq(0).addClass('active');
        var total = $('.carousel-item').length;
        var current = 0;
        $('#moveRight').on('click', function(){
          var next=current;
          current= current+1;
          setSlide(next, current);
        });
        $('#moveLeft').on('click', function(){
          var prev=current;
          current = current- 1;
          setSlide(prev, current);
        });
        function setSlide(prev, next){
          var slide= current;
          if(next>total-1){
          slide=0;
            current=0;
          }
          if(next<0){
            slide=total - 1;
            current=total - 1;
          }
                $('.carousel-item').eq(prev).removeClass('active');
                $('.carousel-item').eq(slide).addClass('active');
            setTimeout(function(){

            },800);          
          console.log('current '+current);
          console.log('prev '+prev);
        }
      });
    }
}
</script>

<style>
/* .monepage{
    width: 100vw;
    height: 100vh;
    background: url("../../assets/waterlily3.jpeg") no-repeat
} */
</style>
<style scoped>
@import url('https://fonts.googleapis.com/css?family=Playfair+Display:400,400i,700,700i,900,900i');

@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i');


* {
  box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    display: flex;
    display: -webkit-flex;
    justify-content: center;
  -webkit-justify-content: center;
    align-items: center;
  -webkit-align-items: center;
}

body {
    background-color: #eaeaea;
}

.carousel {
    width: 100vw;
    height: 100vh;
    display: flex;   
    overflow: hidden;
  position: relative;
}

.carousel-item {
  visibility:visible;
    display: flex;
    width: 100%;
    height: 100%;
    align-items: center;
    justify-content: flex-end;
      -webkit-align-items: center;
    -webkit-justify-content: flex-end;
    position: relative;
    background-color: #fff;
    flex-shrink: 0;
   -webkit-flex-shrink: 0;
    position: absolute;
    z-index: 0;
  transition: 2s all linear;
}

.carousel-item__info {
  height: 100%;
  display: flex;
  justify-content: center;
  flex-direction: column;
  
    display: -webkit-flex;
  -webkit-justify-content: center;
  -webkit-flex-direction: column;
  
  order: 1;
  left: 0;
  margin: auto;
  padding: 0 40px;
  width: 40%;

}

.carousel-item__image {
    width: 60%;
    height: 100%;
    order: 2;
    align-self: flex-end;
    flex-basis: 60%;
  
      -webkit-order: 2;
    -webkit-align-self: flex-end;
    -webkit-flex-basis: 60%;
  
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
   position:relative;
  transform: translateX(100%);
  transition: 2s all ease-in-out;
}

.carousel-item__subtitle {
    font-family: 'Open Sans', sans-serif;
    letter-spacing: 3px;
    font-size: 10px;
    text-transform: uppercase;
    margin: 0;
    color: #7E7E7E;    
    font-weight: 700;
    transform: translateY(25%);
    opacity: 0;
    visibility: hidden;
    transition: 2s all ease-in-out;
}

.carousel-item__title {
    margin: 15px 0 0 0;
    font-family: 'Playfair Display', serif;
    font-size: 44px;
    line-height: 45px;
    letter-spacing: 3px;
    font-weight: 700;
    color: #2C2C2C;
    transform: translateY(25%);
    opacity: 0;
    visibility: hidden;
    transition: 2s all ease-in-out;
}

.carousel-item__description {
    transform: translateY(25%);
    opacity: 0;
    visibility: hidden;
    transition: 2s all ease-in-out;
    margin-top: 35px;
    font-family: 'Open Sans', sans-serif;
    font-size: 13px;
    color: #7e7e7e;
    line-height: 22px;
    margin-bottom: 35px;
}

.carousel-item--1 .carousel-item__image{
  background-image: url("../../assets/waterlily3.jpeg");
}

.carousel-item__btn {
    width: 35%;
    color: #2C2C2C;
    font-family: 'Open Sans', sans-serif;
    letter-spacing: 3px;
    font-size: 11px;
    text-transform: uppercase;
    margin: 0;
    width: 35%;
    font-weight: 700;
  text-decoration: none;
      transform: translateY(25%);
    opacity: 0;
    visibility: hidden;
    transition: 0.6s all ease-in-out;
}

.carousel__nav {
    position: absolute;
    right: 0;
    z-index: 2;
    background-color: #fff;
  bottom: 0;
}

.carousel__icon {
    display: inline-block;
    vertical-align: middle;
    width: 16px;
  fill: #5d5d5d;
}

.carousel__arrow {
    cursor: pointer;
    display: inline-block;
    padding: 11px 15px;
    position: relative;
}

.carousel__arrow:nth-child(1):after {
    content:'';
    right: -3px;
    position: absolute;
    width: 1px;
    background-color: #b0b0b0;
    height: 14px;
    top: 50%;
    margin-top: -7px;
}

.active{
   z-index: 1;
  display: flex;
  visibility:visible;
}

.active .carousel-item__subtitle, .active .carousel-item__title, .active .carousel-item__description,.active .carousel-item__btn{
    transform: translateY(0);
    opacity: 1;
  transition: 0.6s all ease-in-out;
    visibility: visible;
}



.active .carousel-item__image{ 
transition: 0.6s all ease-in-out;
transform: translateX(0);
}

</style>

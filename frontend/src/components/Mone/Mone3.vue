<template>
  <div class='monepage3'>
    <div class="carousel-item__info">
      <div class="carousel-item__container">
      <!-- <h2 class="carousel-item__subtitle"></h2> -->
      <h1 class="carousel-item__title">The Picnic</h1>
      <p class="carousel-item__description">선배 화가 ‘마네’에 대한 존경심과 그의 재능에 도전하고픈 의도에서 ‘마네’의 [풀밭 위의 점심 식사]와 똑같은 주제로 그린 ‘더 피크닉’ 입니다. </p>
      </div>
    </div>
    <img id='lunch' class="carousel-item__image" src="@/assets/thepicnic.jpg">
  </div>
</template>

<script>
export default {
    name:"Mone3",
}
</script>

<style>
.monepage3{
  width: 100vw;
  height: 100vh;
  display: flex;   
  overflow: hidden;
  position: relative;
}
#lunch{
  z-index:-1;
  position: absolute;
  top: 15%;
  left: 10%;
  height: 50vh;
  width: 40vw;
}
.carousel-item__info {
  height: 100%;
  width: 0%;
  display: flex;
  flex-direction: column;  
  /* justify-content: flex-end; */
  right:0;
  margin-top:20%;
  margin-left:50%;
  padding: 0 40px;
  width: 40%;

}

.carousel-item__subtitle {
    font-family: 'Open Sans', sans-serif;
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
    font-family: 'Open Sans', sans-serif;
    font-size: 13px;
    font-weight: 800;
    color: #2C2C2C;
    line-height: 22px;
    margin-bottom: 35px;
}
</style>
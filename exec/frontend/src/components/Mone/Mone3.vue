<template>
  <div class='monepage3'>
    <div class="carousel-item__info" id="carousel-item__info">
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
      computed: {
      page(){
        return this.$store.state.page.page
      }
    },
    watch:{
      'page':function(){
        const insang = document.querySelector('#lunch')
        const info = document.querySelector('#carousel-item__info')

        if(this.page===3){
          setTimeout(function(){
            insang.classList.add('active');
          },500)
          setTimeout(function(){
            info.classList.add('active2');
          },500)
        } else {
          insang.classList.remove('active');
          info.classList.remove('active2');
          
        }
      }
    }
}
</script>

<style scoped>
.monepage3{
  width: 100vw;
  height: 100vh;
  display: flex;   
  overflow: hidden;
  position: relative;
}
.active {
  transform: translateX(-5%);
  opacity: 1;
  transition: 0.6s all ease-in-out;
  visibility: visible;
}
.active2 {
  transform: translateX(5%);
  opacity: 1;
  transition: 0.6s all ease-in-out;
  visibility: visible;
} 
#lunch {
  z-index:-1;
  position: absolute;
  right: -5%;
  height: 85vh;
  width: 65vw;
}
.carousel-item__info {
  height: 100%;
  margin-right:68%;
  top:60%;
  left: 4%;
  width: 30vw;
  position: absolute;
}

.carousel-item__subtitle {
    letter-spacing: 3px;
    font-size: 15px;
    text-transform: uppercase;
    margin-left: 10%;
    color: #2C2C2C;    
    font-weight: 700;
}

.carousel-item__title {
    margin: 30px 0 0 0;
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
    font-weight: 100;
    color: #2C2C2C;
    line-height: 22px;
    margin-bottom: 35px;
}
</style>
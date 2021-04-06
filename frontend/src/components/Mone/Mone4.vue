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
  </div>
</template>

<script>
// import { gsap } from 'gsap';
export default {
    name:"Mone4",
    computed: {
      page(){
        return this.$store.state.page.page
      }
    },
    watch:{
      'page':function(){
        // const insang = document.querySelector('#insang')
        const info = document.querySelector('#info')

        if(this.page===4){
          console.log(this.page)
          setTimeout(function(){
            info.classList.add('active');
          },500)
        }
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
  /* justify-content: flex-end; */
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
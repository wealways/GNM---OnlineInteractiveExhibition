<template>
  <div class='monepage2'>
    <div class="carousel-item__info" id="carousel-item__info">
      <div class="carousel-item__container">
      <h2 class="carousel-item__subtitle">인상, 해돋이</h2>
      <h1 class="carousel-item__title">Impression, Sunrise</h1>
      <p class="carousel-item__description">어둠 속에서 해가 막 떠오르는 풍경을 담은 '인상, 해돋이' 에는 검은색이 전혀 사용되지 않았는데, 검은색을 쓰지 않고도 충분히 어둠을 표현한 실험적인 작품입니다. 밤은 검은색이라고 믿는 이들에게 색채는 빛의 문제일 뿐이라는 과학적 설득이 당장은 받아들여지기 어려웠다고 합니다.</p>
      </div>
    </div>
    <img id='insang' class="carousel-item__image" src="@/assets/insang.jpg">
  </div>
</template>

<script>
export default {
    name:"Mone2",
    computed: {
      page(){
        return this.$store.state.page.page
      }
    },
    watch:{
      'page':function(){
        const insang = document.querySelector('#insang')
        const info = document.querySelector('#carousel-item__info')

        if(this.page===2){
          setTimeout(function(){
            insang.classList.add('active');
            },500)
          setTimeout(function(){
            info.classList.add('active');
          },500)
        }else{
          insang.classList.remove('active');
          info.classList.remove('active');

        }
      }
    }
    
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Prata&display=swap');
@import url('https://fonts.googleapis.com/css?family=Playfair+Display:400,400i,700,700i,900,900i');
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i');

.monepage2{
  width: 100vw;
  height: 100vh;
  display: flex;   
  overflow: hidden;
  position: relative;
}
 
.active {
    transform: translateY(-5%);
    opacity: 1;
    transition: 0.6s all ease-in-out;
    visibility: visible;
} 
#insang{
  z-index:-1;
  position: absolute;
  top: 19%;
  left: 5%;
  height: 60vh;
  width: 50vw;
}

.carousel-item__info {
  height: 100%;
  width: 0%;
  right:6%;
  top:40%;
  margin-left:40%;
  padding: 0 40px;
  width: 40%;
  position: absolute;
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
  font-weight: 200;
  color: #2C2C2C;
  line-height: 22px;
  margin-bottom: 35px;
}
</style>

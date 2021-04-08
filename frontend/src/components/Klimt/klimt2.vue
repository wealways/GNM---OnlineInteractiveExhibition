<template>
  <div class="section">
    <img id="judith1-image" class="slide-in" src="@/assets/images/klimt/Judith_1_(cropped).jpg" alt="유디트">
    <div class="description">
      <div id="judith1-description">
        <h4 class="desc-main__title">Judith II - Salome</h4>
        <div class="desc-main__subtitle">유디트II <span style="font-size:0.8rem;">(1909)</span></div>
        <div class="desc-main__description">
        유대인의 문화에서 유디트는 훌륭하고 지혜로운 여인이지만,
        이 작품에서 드러나는 유디트는 공포의 대상으로 표현됩니다.
        </div>
      </div>
      <div id="judith2-description">
        <h4 class="desc-main__title">Judith </h4>
        <div class="desc-main__subtitle">유디트I <span style="font-size:0.8rem;">(1901)</span></div>
        <div class="desc-main__description">
          유디트의 일화는 ‘아름다운 여인의 대담한 살인 행동’이라는 측면에서
          여러 의미를 동시에 표출할 수 있는 드라마적 요소를 갖춘
          매우 흥미로운 주제로 당대 화가들에게 많은 영감을 줬습니다.
        </div>
      </div>
    </div>
    <img id="judith2-image" class="slide-in" src="@/assets/images/klimt/Judith_II.jpg" alt="유디트">

  </div>
</template>

<script>
export default {
  name:'Klimt2',
  computed:{
    page(){
      return this.$store.state.page.page
    }
  },
  watch:{
    'page':function(){
      const img1 = document.querySelector('#judith1-image')
      const description1 = document.querySelector('#judith1-description')
      const img2 = document.querySelector('#judith2-image')
      const description2 = document.querySelector('#judith2-description')
      if(this.page===2){
        setTimeout(function(){
          img1.classList.add('active');
          description2.classList.add('active-description');
        },500)
        setTimeout(function(){
          img2.classList.add('active');
          description1.classList.add('active-description');
        },700)
      }else{
        img1.classList.remove('active');
        img2.classList.remove('active');
        description1.classList.remove('active-description');
        description2.classList.remove('active-description');
      }
    }
  },

}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Prata&display=swap');
@import url('https://fonts.googleapis.com/css?family=Playfair+Display:400,400i,700,700i,900,900i');
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i');

.section{
  display: flex;
  flex-direction: row;
  padding: 3rem 5rem;
  color:aliceblue;
  justify-content:space-between;
}
#judith1-image{
  margin-top:8%;
  margin-left: 3rem;
  height:80%;
  padding: 0 1rem;
}
#judith1-description {
  margin-left:40%;
  opacity: 0;
  transition: all 1s;
}
#judith2-image{
  height:80%;
  margin-right: 3rem;
  padding: 0 1rem;
}
#judith2-description {
  margin-right:40%;
  opacity: 0;
  transition: all 1s;
}
.description{
  padding: 3rem 3rem;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.desc-main__title{
  color:#FFD700;
  font-family:'Playfair Display', serif;
  letter-spacing: 3px;
}
.desc-main__subtitle{
  font-size: 1.5rem;
  margin:1rem 0;
}
.desc-main__description{
  line-height: 22px;
}
.slide-in {
  opacity: 0;
  transition: all 1s;
}
#judith1-image.slide-in {
  transform: translateY(100%) scale(0.95);
}
#judith2-image.slide-in {
  transform: translateY(-100%) scale(0.95);
}
.active {
  opacity: 1;
  transform: translateY(0%) scale(1) !important;
}
.active-description{
  opacity: 1 !important;
}
</style>
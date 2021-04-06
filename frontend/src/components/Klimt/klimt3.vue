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

}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Prata&display=swap');
@import url('https://fonts.googleapis.com/css?family=Playfair+Display:400,400i,700,700i,900,900i');
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i');

.section{
  padding: 3rem 5rem;
  color:aliceblue;
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
  font-family:'Open Sans', sans-serif;
  font-size: 1.5rem;
  margin:0.5rem 0;
}
.desc-main__description{
  font-family:'Open Sans', sans-serif;
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
<template>
  <div class="section">
    <img id="judith1" class="slide-in" src="@/assets/images/klimt/Judith_1_(cropped).jpg" alt="유디트">
    <div class="description">
      <div>
        <h4>유디트II <span style="font-size:1rem;">(1909)</span></h4>
        Judith II (Salome)<br>
        유대인의 문화에서 유디트는 훌륭하고 지혜로운 여인이지만,
        이 작품에서 드러나는 유디트는 공포의 대상으로 표현됩니다.
      </div>
      <div>
        <h4>유디트I <span style="font-size:1rem;">(1901)</span></h4>
        Judith<br>
        유디트의 일화는 ‘아름다운 여인의 대담한 살인 행동’이라는 측면에서
        여러 의미를 동시에 표출할 수 있는 드라마적 요소를 갖춘
        매우 흥미로운 주제로 당대 화가들에게 많은 영감을 줬습니다.
      </div>
    </div>
    <img id="judith2" class="slide-in" src="@/assets/images/klimt/Judith_II.jpg" alt="유디트">

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
      const img1 = document.querySelector('#judith1')
      const img2 = document.querySelector('#judith2')
      if(this.page===2){
        console.log(this.page)
        setTimeout(function(){
          img1.classList.add('active');
        },500)
        setTimeout(function(){
          img2.classList.add('active');
        },1000)
      }else{
        img1.classList.remove('active')
        img2.classList.remove('active')
      }
    }
  },

}
</script>

<style scoped>
.section{
  display: flex;
  flex-direction: row;
  padding: 3rem 5rem;
  color:aliceblue;
  justify-content:space-between;
}
#judith1{
  margin-top:8%;
  margin-left: 5rem;
  height:80%;
  padding: 0 1rem;
}
#judith2{
  height:80%;
  margin-right: 5rem;
  padding: 0 1rem;
}
.description{
  padding: 3rem 3rem;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}
.slide-in {
  opacity: 0;
  transition: all 1s;
}
#judith1.slide-in {
  transform: translateY(100%) scale(0.95);
}
#judith2.slide-in {
  transform: translateY(-100%) scale(0.95);
}
.active {
  opacity: 1;
  transform: translateY(0%) scale(1) !important;
}
</style>
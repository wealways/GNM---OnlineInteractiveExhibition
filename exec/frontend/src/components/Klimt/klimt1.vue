<template>
  <div class="section">
    <img src="@/assets/images/klimt/Gustav_Klimt_046.jpg" alt="아델레 블로흐-바우어의 초상">
    <div class="description">
      <h3 class="desc-main__title">Portrait of Adele Bloch - Bauer I</h3>
      <div class="desc-main__subtitle">아델레 블로흐-바우어의 초상 <span style="font-size:1rem">(1907)</span></div>
      <div class="desc-main__description">
        "The Lady in Gold" 또는 "The Woman in Gold" 이라 불리는 만큼 아델라의 얼굴과 손, 어깨를 제외한 모든 부분은 금을 활용한 장식적인 무늬와 패턴을 사용하여
        매우 강렬한 인상을 남겼습니다.
        사실적인 부분이 많지 않아 오히려 아델라의 표정이 돋보이네요. 
      </div>
    </div>
  </div>
</template>

<script scoped>
export default {
  name:'Klimt1',
  computed:{
    page(){
      return this.$store.state.page.page
    }
  },
  watch:{
    'page':function(){
      if(this.page===1){
        /* 애니메이션 css 태그 */
        // console.log(this.page)
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
}
.section img{
  height:100%;
  padding: 1rem 1rem;
}
.description{
  margin:auto 0;
  padding: 3rem 3rem;
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
</style>
<template>
  <div class="section">
    <img src="@/assets/images/klimt/Gustav_Klimt_046.jpg" alt="아델레 블로흐-바우어의 초상">
    <div class="description">
      <h3>아델레 블로흐-바우어의 초상 <span style="font-size:1rem">(1907)</span></h3>
      Portrait of Adele Bloch-Bauer I (The Lady in Gold or The Woman in Gold)<br>
      아델라의 얼굴과 손, 어깨를 제외한 모든 부분은 금을 활용한 장식적인 무늬와 패턴을 사용하여
      매우 강렬한 인상을 남겼습니다.<br>
      사실적인 부분이 많지 않아 오히려 아델라의 표정이 돋보이네요. 
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
        console.log(this.page)
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
}
.section img{
  height:100%;
  padding: 1rem 1rem;
}
.description{
  margin:auto 0;
  padding: 3rem 3rem;
}
</style>
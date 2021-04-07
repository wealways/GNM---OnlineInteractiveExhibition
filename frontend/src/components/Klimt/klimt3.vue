<template>
  <div class="section">
    <img src="@/assets/images/klimt/Gustav_Klimt_030.jpg" alt="더 트리 오브 라이프">
    <img src="@/assets/images/klimt/Gustav_Klimt_032.jpg" alt="더 트리 오브 라이프">
    <img src="@/assets/images/klimt/Gustav_Klimt_031.jpg" alt="더 트리 오브 라이프">
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
      if(this.page===3){
        console.log(this.page)
      }
    }
  },

}
</script>

<style scoped>
.section{
  padding: 3rem 5rem;
}
.section img{
  width:20%;
  height:500px;
  padding: 0 1rem;
}
</style>
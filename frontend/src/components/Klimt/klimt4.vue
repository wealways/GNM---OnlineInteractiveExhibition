<template>
  <div class="section">
    클림트4
  </div>
</template>

<script>
export default {
  name:'Klimt4',
  computed:{
    page(){
      return this.$store.state.page.page
    }
  },
  watch:{
    'page':function(){
      if(this.page===4){
        console.log(this.page)
      }
    }
  },

}
</script>

<style scoped>

</style>
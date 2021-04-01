<template>
  <div class="body">
    <KlimtInteractive/>
  </div>
</template>


<script>


export default {
  name:'Klimt',
  components:{
    KlimtInteractive: () => import('@/components/Klimt/KlimtInteractive')
  },
  mounted: function (){
  }

}
</script>

<style scoped>
.body{
  padding:2rem;
  background-color: black;
  height: 100vh;

}

</style>
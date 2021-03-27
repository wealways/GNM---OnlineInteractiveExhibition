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
  }
  
}
</script>

<style>
</style>
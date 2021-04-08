<template>
  <div>
    <IconMap/>
    <CheonInteractive/>
  </div>
</template>

<script>
export default {
  name:'Cheon',
  components: {
    CheonInteractive: () => import('@/components/Cheon/CheonInteractive'),
    IconMap: () => import('@/components/IconMap/IconMap'),    
  }
}
</script>

<style>

</style>
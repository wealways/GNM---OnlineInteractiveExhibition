<template>
  <div class="body">
    <CheonInteractive/>
  </div>
</template>

<script>
export default {
  name:'Cheon',
  components: {
    CheonInteractive: () => import('@/components/Cheon/CheonInteractive')
  }
}
</script>

<style>

</style>
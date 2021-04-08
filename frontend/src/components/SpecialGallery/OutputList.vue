<template>
  <div class="container">
    <Output />
    <Output />
    <Output />
  </div>
</template>

<script>
import Output from '@/components/SpecialGallery/Output.vue'
export default {
  name: 'OutputList',
  components: {
    Output,
  },
}
</script>

<style scoped>
.container {
  align-self: center;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  flex-wrap: nowrap;
}
</style>
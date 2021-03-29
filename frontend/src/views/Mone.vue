<template>
  <div>
    <mone-interactive></mone-interactive>
    <PhotoUpload/>  
  </div>
</template>

<script>
import MoneInteractive from '../components/Mone/MoneInteractive.vue'
import PhotoUpload from '../components/PhotoUpload.vue'
export default {
    name:'Mone',
    components:{ PhotoUpload, MoneInteractive }
}
</script>

<style>

</style>
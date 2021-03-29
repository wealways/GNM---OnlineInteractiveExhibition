<template>
  <div>
      <PhotoUpload/>
      <q-btn :to='"/mone"' target="_blank">->skip</q-btn>
  </div>
</template>

<script>
import PhotoUpload from '../PhotoUpload'
export default {
    name:'MonetPhoto',
    components: { PhotoUpload }
}
</script>

<style>

</style>
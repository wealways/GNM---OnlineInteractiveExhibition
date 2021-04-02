<template>
  <div class='pause'>
    <IconMap/>
    <IconVoice/>
    <transition 
      name="fade"
      mode="out-in"
    >
      <router-view class="child-view"></router-view>
    </transition>
  </div>
</template>

<script>
import IconMap from '../IconMap/IconMap'
import IconVoice from '../IconMap/IconVoice'

export default {
  name: 'Mones',
  components: { IconMap, IconVoice }
}
</script>

<style scoped>
html, body {
  padding: 0;
  margin: 0;
}
</style>
<style>
.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.3s;
  transition-property: opacity;
  transition-timing-function: ease;
}

.fade-enter,
.fade-leave-active {
  opacity: 0
}
</style>
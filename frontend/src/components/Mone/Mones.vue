<template>
  <div class='pause'>
    <IconMap/>
    <IconVoice/>
    <transition 
      name="slide-fade"
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
.slide-fade-enter-active {
  transition: all .5s ease;
}

.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.slide-fade-leave-to {
  transform: translateX(-100px);
  opacity: 0;
}

.slide-fade-enter {
  transform: translateX(100px);
  opacity: 0;
}

</style>
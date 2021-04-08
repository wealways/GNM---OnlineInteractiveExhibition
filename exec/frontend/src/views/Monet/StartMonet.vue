<template>
  <div>
    <IconMap/>
    <IconVoice/>
    <MonetIntro/>
  </div>
</template>

<script>
import MonetIntro from '@/components/Mone/MoneIntro'

export default {
  name:'StartMonet',
  components: { 
    MonetIntro,
    IconMap: () => import('@/components/IconMap/IconMap'),
    IconVoice: () => import('@/components/IconMap/IconVoice'), 
  }
}
</script>

<style>

</style>
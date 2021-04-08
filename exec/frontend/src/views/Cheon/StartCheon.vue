<template>
  <div>
    <IconMap/>
    <IconVoice/>
    <CheonIntro/>
  </div>
</template>

<script>
import CheonIntro from '@/components/Cheon/CheonIntro'

export default {
  name:'StartCheon',
  components: { 
    CheonIntro, 
    IconMap: () => import('@/components/IconMap/IconMap'),
    IconVoice: () => import('@/components/IconMap/IconVoice'), 
  }
}
</script>

<style>

</style>
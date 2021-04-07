<template>
  <div>
    <IconMap mapColor="#eee8aa"/>
    <IconVoice voiceColor="#eee8aa"/>
      
    <KlimtIntro/>
  </div>
</template>

<script>
import KlimtIntro from '@/components/Klimt/KlimtIntro'
import IconMap from '@/components/IconMap/IconMap'
import IconVoice from '@/components/IconMap/IconVoice'
export default {
  name:'StartMonet',
  components: { KlimtIntro,IconMap,IconVoice }
}
</script>

<style scoped>
*{
  overflow: hidden;
  background-color: #28353c;
  height: 100vh;
  width: 100vw;
}
</style>
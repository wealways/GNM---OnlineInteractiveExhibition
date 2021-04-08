<template>
  <div>
    <IconMap mapColor="#608091"/>
    <IconVoice voiceColor="#608091"/>
      
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
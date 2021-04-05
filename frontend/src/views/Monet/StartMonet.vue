<template>
  <div>
    <Icons/>
    <MonetIntro/>
  </div>
</template>

<script>
import MonetIntro from '@/components/Mone/MoneIntro'
import Icons from '@/components/IconMap/Icons'

export default {
  name:'StartMonet',
  components: { MonetIntro,Icons }
}
</script>

<style>

</style>
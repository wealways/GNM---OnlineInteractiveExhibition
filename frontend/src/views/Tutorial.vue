<template>
  <q-layout>
    <Icon/>
    <Description/>
  </q-layout>
</template>
<script>
import Icon from '../components/Icon/Icon.vue'
import Description from '../components/Description/Description.vue'

export default {
  name: 'Tutorial',
  components: { Icon, Description }
}
</script>
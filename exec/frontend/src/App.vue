<template>
   <div id="q-app">
    <!-- <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="leftDrawerOpen = !leftDrawerOpen"
          aria-label="Menu"
          icon="menu"
        />

        <q-toolbar-title>
          Quasar App
        </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header> -->
    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'LayoutDefault',

  components: {
  },

  data () {
    return {
      leftDrawerOpen: false
    }
  }
}
</script>

<style>
* {
  font-family: 'Noto Sans KR';
}
</style>

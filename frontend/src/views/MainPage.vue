<template>
  <q-page class="flex flex-center">
    <full-page
      ref="fullpage"
      :options="options"
      id="fullpage"
      class="full-width"
    >
      <div class="full-width section">
        <h1>section1</h1>
      </div>
      <div class="full-width section">
        <h1>section1</h1>
      </div>
      <div class="full-width section">
        <h1>section1</h1>
      </div>
    </full-page>
    <q-page-sticky v-if="isScrolled" position="bottom-right" :offset="[25, 25]">
      <q-btn
        fab
        icon="keyboard_arrow_up"
        color="primary"
        @click="$refs.fullpage.api.moveTo(1)"
      />
    </q-page-sticky>
  </q-page>
</template>

<script>
export default {
  name: 'MainPage',
  data() {
    return {
      options: {
        navigation: true,
        onLeave: this.onLeave,
        licenseKey: "iTq67SN$c3"
      },
    };
  },
  methods: {
    componentsReady(){
      this.$refs.fullpage.init()
    }
  }
}
</script>

<style>
#section1 {
  background-position: center;
  background-size: unset;
  background-image: url("../assets/monemone.jpg");
}
</style>

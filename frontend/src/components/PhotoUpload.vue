<template>
  <div id="photo">
    <div>
      photoupload
    </div>
    <button @click='getSession'>click</button>  
  </div>
</template>

<script>
export default {
  name: 'PhotoUpload',
  methods:{
    getSession(){
      this.$store.dispatch('getsession/getSession')
    }
  }
}
</script>

<style>
#photo{
  position: absolute;
  top: 10%;
  
}
</style>
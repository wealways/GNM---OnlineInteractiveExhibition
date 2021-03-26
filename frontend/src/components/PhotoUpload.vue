<template>
  <div>
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

</style>
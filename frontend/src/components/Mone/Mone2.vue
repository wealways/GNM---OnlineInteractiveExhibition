<template>
  <div>
      <button @click="changerouter">change router</button>
  </div>
</template>

<script>
export default {
    name:"Mone2",
    methods:{
        changerouter(){
            this.$router.push({path:'/mones/mone3'})
        }
    }
}
</script>

<style>

</style>
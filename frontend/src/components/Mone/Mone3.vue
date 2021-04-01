<template>
  <div>
      <button @click="changerouter">change router</button>
  </div>
</template>

<script>
export default {
    name:"Mone3",
    methods:{
        changerouter(){
            this.$router.push({path:'/mones/mone4'})
        }
    }
}
</script>

<style>

</style>
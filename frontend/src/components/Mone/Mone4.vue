<template>
  <div>
      <button @click="changerouter">change router to klimt</button>
  </div>
</template>

<script>
export default {
    name:"Mone4",
    methods:{
        changerouter(){
            this.$router.push({path:'/startklimt'})
        }
    }
}
</script>

<style>

</style>
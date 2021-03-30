<template>
  <div>
      <button @click="gettest">테스트</button>
  </div>
</template>

<script>
import { getFile } from '@/api/getFile.js'
export default {
    name:'test',
    data(){
        return {
            imgUrl:""
        }
    },
    methods:{
        gettest(){
            const artist = 1;
            getFile(
                artist,
                (response) =>{
                    this.imgUrl = response;
                    console.log(this.imgUrl)
                },
                (error) => console.log(error)
            )
        }
    }
}
</script>

<style>

</style>
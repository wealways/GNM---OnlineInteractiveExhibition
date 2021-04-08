<template>
  <div>
      <button @click="gettest">테스트</button>
      <img :src=imgUrl alt="">
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
            getFile(
                (response) =>{
                    console.log(response)
                    this.imgUrl = response.data.input_image_1
                },
                (error) => console.log(error)
            )
        }
    }
}
</script>

<style>

</style>
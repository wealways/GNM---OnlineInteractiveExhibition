<template>
  <div class='monepage3'>
      <h1 class=desc>description3</h1>
      <button @click="changerouter">change router</button>
  </div>
</template>

<script>
import { gsap } from 'gsap';
export default {
    name:"Mone3",
    created(){
        window.addEventListener('scroll', this.handleScroll);
    },
    methods:{
        changerouter(){
            this.$router.push({path:'/mones/mone4'})
        },
         handleScroll(event){
            if(event){
                this.showdescription()
            }
        },
        showdescription(){
            let t1 = gsap.timeline();
            t1.from(
            ".desc",
            {
                yPercent: 100,
                ease: "power1.out",
                opacity: 0,
            },
            );
        }
    }
}
</script>

<style>
.monepage3{
    width: 100vw;
    height: 100vh;
    background: url("../../assets/thepicnic.jpg") no-repeat
}
</style>
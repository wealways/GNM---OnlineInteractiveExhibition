<template>
  <div class='monepage2'>
      <h1 class=desc>description2</h1>
  </div>
</template>

<script>
import { gsap } from 'gsap';
export default {
    name:"Mone2",
    created(){
        window.addEventListener('scroll', this.handleScroll);
    },
    methods:{
        changerouter(){
            this.$router.push({path:'/mones/mone3'})
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
.monepage2{
    width: 100vw;
    height: 100vh;
    background: url("../../assets/insang.jpg") no-repeat
}
</style>
<template>
  <div class='monepage4'>
      <h1 class=desc>description4</h1>
      <button @click="changerouter">change router to klimt</button>
  </div>
</template>

<script>
import { gsap } from 'gsap';
export default {
    name:"Mone4",
    created(){
        window.addEventListener('scroll', this.handleScroll);
    },
    methods:{
        changerouter(){
            this.$router.push({path:'/startklimt'})
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
.monepage4{
    width: 100vw;
    height: 100vh;
    background: url("../../assets/parasol.jpg") no-repeat
}
</style>
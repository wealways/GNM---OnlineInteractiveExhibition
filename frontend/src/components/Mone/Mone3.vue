<template>
  <div class='monepage3'>
      <h1 class=desc>description3</h1>
  </div>
</template>

<script>
import { gsap } from 'gsap';
export default {
    name:"Mone3",
    mounted(){
        let t1 = gsap.timeline();
        t1.from(
        ".desc",
        {
            yPercent: 100,
            ease: "power1.out",
            opacity: 0,
        },
        );
        var Counter = 0;
        function myFunction() {
            Counter = Math.ceil(window.scrollY);
        }
        window.onscroll = () => {
                myFunction();
                if (Counter > 0){
                    if (this.$route.path === '/mones/mone3') {
                        this.changerouter()
                    }
                }
                console.log(Counter)
        };
    },
    methods:{
        changerouter(){
            this.$router.push({path:'/mones/mone4'})
        },
    }
}
</script>

<style>
.monepage3{
    width: 100vw;
    height: 101vh;
    background: url("../../assets/thepicnic.jpg") no-repeat
}
</style>
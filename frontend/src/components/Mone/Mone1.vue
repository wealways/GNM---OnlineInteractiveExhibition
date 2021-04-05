<template>
  <div class='monepage'>
      <h1 class=desc>description</h1>
  </div>
</template>

<script>
import { gsap } from 'gsap';

export default {
    name:"Mone1",
    data(){
        return {
            scrollnum:0,
        }
    },
    mounted(){
        
        let t1 = gsap.timeline();
        t1.from(
        ".desc",
        {   
            delay: 1,
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
            if (Counter === 0){
                if (this.$route.path === '/mones/mone1') {
                    this.changerouter()
                }
            }
            console.log(Counter)
        };
    },
   
    methods:{
        changerouter(){
            this.$router.push({path:'/mones/mone2'})
        },
       

    }
}
</script>

<style>
.monepage{
    width: 100vw;
    height: 101vh;
    background: url("../../assets/waterlily3.jpeg") no-repeat
}
.desc {
    position: absolute;
    bottom: 10%;
    left: 40%;
}
</style>
<template>
  <div class='monepage'>
      <h1 class=desc>description</h1>
  </div>
</template>

<script>
import { gsap } from 'gsap';

export default {
    name:"Mone1",
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
    }
}
</script>

<style>
.monepage{
    width: 100vw;
    height: 100vh;
    background: url("../../assets/waterlily3.jpeg") no-repeat
}
.desc {
    bottom: 10%;
    left: 40%;
}
</style>
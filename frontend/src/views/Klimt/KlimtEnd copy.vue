<template>
  <div class="body">
    <div id="container">
      <section data-scroll-section>
        <Klimt1/>
        <Klimt2/>
        <Klimt3/>
        <Klimt4/>

      </section>
    </div>
  </div>
</template>


<script>
import { gsap } from 'gsap';
import { ScrollTrigger } from "gsap/ScrollTrigger";

gsap.registerPlugin(ScrollTrigger)

export default {
  name:'KlimtEnd',
  components:{
    Klimt1: () => import('@/components/Klimt/klimt1'),
    Klimt2: () => import('@/components/Klimt/klimt2'),
    Klimt3: () => import('@/components/Klimt/klimt3'),
    Klimt4: () => import('@/components/Klimt/klimt4'),
  },
  mounted: function (){
    const width = document.body.offsetWidth    
    const height = document.body.offsetHeight
    const sections = document.querySelectorAll('section')
    sections.forEach(section => {
      section.style.width = width
      section.style.height = height
    } )
    let container = document.getElementById("container");
      gsap.to(container, {
        xPercent: -100,
        ease: "none",
        scrollTrigger: {
          trigger: container,
          pin: true,
          scrub: 1,
          snap:false,
          end: () => "+=" + container.offsetWidth
        }
      })
  }

}
</script>

<style scoped>

section {
  padding : 0 !important;

}
/* html, body {
  overflow-y: hidden;
  position: fixed;
} */
</style>
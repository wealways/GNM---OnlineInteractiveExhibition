<template>
  <div class="container">
    <section>
      <IconMap mapColor="#eee8aa"/>
      <IconVoice voiceColor="#eee8aa"/>
      <Klimt1 id="klimt1" class="content"/>
      <Klimt2 id="klimt2" class="content"/>
      <Klimt3 id="klimt3" class="content"/>
    </section>
<<<<<<< HEAD:frontend/src/views/Klimt/KlimtEnd.vue
    <audio data-key="tada" src="@/assets/audio/tada.mp3"></audio>
    <audio data-key="timo" src="@/assets/audio/timo.mp3"></audio>
    <audio data-key="wow" src="@/assets/audio/wow.mp3"></audio>
    <audio data-key="bye" src="@/assets/audio/bye.mp3"></audio>
=======
>>>>>>> dcb941ddbd33f16216eeb3b7ae5169f5cf5939fa:frontend/src/views/Klimt/Klimts.vue
  </div>
</template>


<script>
export default {
  name:'KlimtEnd',
  components:{
    IconMap: () => import('@/components/IconMap/IconMap'),
    IconVoice: () => import('@/components/IconMap/IconVoice'),
    Klimt1: () => import('@/components/Klimt/klimt1'),
    Klimt2: () => import('@/components/Klimt/klimt2'),
    Klimt3: () => import('@/components/Klimt/klimt3'),
  },
  data(){
    return {
      page:1
    }
  },
  watch:{
  },
  mounted: function (){
    
    // horizontal scroll 
    const container = document.querySelector('.container')
    const section = document.getElementsByTagName('section')
    const sectionPageWidth = section[0].clientWidth/3
    window.addEventListener('wheel', function(e)
    {
      e.preventDefault();
      let delta = e.deltaY
      if(delta>0){
        if(container.scrollLeft>sectionPageWidth*1){
          this.page=3
          return;
        }
        if(0<=container.scrollLeft && container.scrollLeft<sectionPageWidth*1){
          container.scrollLeft = sectionPageWidth*1
          this.$store.dispatch('page/pageChange',2)
        }else{
          container.scrollLeft=sectionPageWidth*2
          this.$store.dispatch('page/pageChange',3)
        }
      }else{
        if(container.scrollLeft<sectionPageWidth*1){
          this.$store.dispatch('page/pageChange',1)
          return;
        }
        if(0<=container.scrollLeft && container.scrollLeft<=sectionPageWidth*1){
          container.scrollLeft =0
          this.$store.dispatch('page/pageChange',1)
        }else{
          container.scrollLeft=sectionPageWidth*1
          this.$store.dispatch('page/pageChange',2)
        }
      }
    }.bind(this), {capture: false,passive: false});


  },
  methods:{
  }

}
</script>

<style scoped>
*{
  margin:0;
  padding:0;
  box-sizing: border-box;
  scroll-behavior: smooth;
}
.container{
  width:100vw;
  height:100vh;
  overflow-x: scroll;
  overflow-y:hidden;
  background-color: #28353c;
}
.container::after{
  content: '';
  position: absolute;
  top:0;
  left:0;
  width:100%;
  height: 100%;
  z-index: -10;
}
.container section{
   width:300vw;
   display: flex;
   flex-direction: row;
}

.container section .content {
  width:100vw;
  height:100vh;
}


::-webkit-scrollbar{
  display:none;
}
</style>
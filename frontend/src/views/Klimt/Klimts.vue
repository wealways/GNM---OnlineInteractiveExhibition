<template>
  <div class="container">
    <section>
      <IconMap mapColor="aliceblue"/>
      <IconVoice voiceColor="aliceblue"/>
      <Klimt1 id="klimt1" class="content"/>
      <Klimt2 id="klimt2" class="content"/>
      <Klimt3 id="klimt3" class="content"/>
      <Klimt4 id="klimt4" class="content"/>
    </section>
    <!-- <audio data-key="tada" src="@/assets/audio/tada.mp3"></audio>
    <audio data-key="timo" src="@/assets/audio/timo.mp3"></audio>
    <audio data-key="wow" src="@/assets/audio/wow.mp3"></audio>
    <audio data-key="bye" src="@/assets/audio/bye.mp3"></audio> -->
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
    Klimt4: () => import('@/components/Klimt/klimt4'),
  },
  data(){
    return {
      page:1
    }
  },
  watch:{
  },
  mounted: function (){
    // 음성 안내
    function playSound(audio) {
      if(!audio) return;
      audio.currentTime = 0; 
      audio.play(); 

    }
    const audio = document.querySelector("audio[data-key=tada]")
    playSound(audio)

    // horizontal scroll 
    const container = document.querySelector('.container')
    const section = document.getElementsByTagName('section')
    const sectionPageWidth = section[0].clientWidth/4
    window.addEventListener('wheel', function(e)
    {
      e.preventDefault();
      let delta = e.deltaY
      if(delta>0){
        if(container.scrollLeft>sectionPageWidth*2){
          this.page=4
          return;
        }
        if(0<=container.scrollLeft && container.scrollLeft<sectionPageWidth*1){
          container.scrollLeft = sectionPageWidth*1
          this.$store.dispatch('page/pageChange',2)
          const audio = document.querySelector("audio[data-key=timo]")
          playSound(audio)
        }else if(sectionPageWidth*1<=container.scrollLeft && container.scrollLeft<sectionPageWidth*2){
          container.scrollLeft=sectionPageWidth*2
          this.$store.dispatch('page/pageChange',3)
          const audio = document.querySelector("audio[data-key=wow]")
          playSound(audio)
        }else{
          container.scrollLeft=sectionPageWidth*3
          this.$store.dispatch('page/pageChange',4)
          const audio = document.querySelector("audio[data-key=bye]")
          playSound(audio)
        }
      }else{
        if(container.scrollLeft<sectionPageWidth*1){
          this.$store.dispatch('page/pageChange',1)
          return;
        }
        if(0<=container.scrollLeft && container.scrollLeft<=sectionPageWidth*1){
          container.scrollLeft =0
          this.$store.dispatch('page/pageChange',1)
          const audio = document.querySelector("audio[data-key=tada]")
          playSound(audio)
        }else if(sectionPageWidth*1<container.scrollLeft && container.scrollLeft<=sectionPageWidth*2){
          container.scrollLeft=sectionPageWidth*1
          this.$store.dispatch('page/pageChange',2)
          const audio = document.querySelector("audio[data-key=timo]")
          playSound(audio)
        }else{
          container.scrollLeft=sectionPageWidth*2
          this.$store.dispatch('page/pageChange',3)
          const audio = document.querySelector("audio[data-key=wow]")
          playSound(audio)
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
   width:400vw;
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
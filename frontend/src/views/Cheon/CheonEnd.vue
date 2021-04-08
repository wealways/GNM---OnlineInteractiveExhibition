<template>
  <div class="container">
    <div id="_progress"></div>
    <section>
      <IconMap mapColor/>
      <IconVoice voiceColor/>
      <Cheon1 class="content"/>
      <Cheon2 class="content"/>
      <Cheon3 class="content"/>
      <Cheon4 class="content"/>
    </section>
    <!-- <audio data-key="tada" src="@/assets/audio/tada.mp3"></audio>
    <audio data-key="timo" src="@/assets/audio/timo.mp3"></audio>
    <audio data-key="wow" src="@/assets/audio/wow.mp3"></audio>
    <audio data-key="bye" src="@/assets/audio/bye.mp3"></audio> -->
  </div>
</template>


<script>

export default {
  name:'CheonEnd',
  components:{
    IconMap: () => import('@/components/IconMap/IconMap'),
    IconVoice: () => import('@/components/IconMap/IconVoice'),
    Cheon1: () => import('@/components/Cheon/Cheon1'),
    Cheon2: () => import('@/components/Cheon/Cheon2'),
    Cheon3: () => import('@/components/Cheon/Cheon3'),
    Cheon4: () => import('@/components/Cheon/Cheon4'),
  },
  data(){
    return {
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
      if(this.$route.name==='Cheons'){

        e.preventDefault();
  
        let scrollBottom = 4;
        let scrollLeft = 1;
        
  
  
        let delta = e.deltaY
        if(delta>0){
          if(container.scrollLeft>sectionPageWidth*3){
            this.page=4
            scrollLeft = 4
            return;
          }
          if(0<=container.scrollLeft && container.scrollLeft<sectionPageWidth*1){
            container.scrollLeft = sectionPageWidth*1
            scrollLeft = 2
            this.$store.dispatch('page/pageChange',2)
            const audio = document.querySelector("audio[data-key=timo]")
            playSound(audio)
          }else if(sectionPageWidth*1<=container.scrollLeft && container.scrollLeft<sectionPageWidth*2){
            container.scrollLeft=sectionPageWidth*2
            scrollLeft = 3
            this.$store.dispatch('page/pageChange',3)
            const audio = document.querySelector("audio[data-key=wow]")
            playSound(audio)
          }else{
            container.scrollLeft=sectionPageWidth*3
            scrollLeft = 4
            this.$store.dispatch('page/pageChange',4)
            const audio = document.querySelector("audio[data-key=bye]")
            playSound(audio)
          }
        }else{
          if(container.scrollLeft<sectionPageWidth*1){
            scrollLeft = 1
            this.$store.dispatch('page/pageChange',1)
            return;
          }
          if(0<=container.scrollLeft && container.scrollLeft<=sectionPageWidth*1){
            container.scrollLeft =0
            scrollLeft = 1
            this.$store.dispatch('page/pageChange',1)
            const audio = document.querySelector("audio[data-key=tada]")
            playSound(audio)
          }else if(sectionPageWidth*1<container.scrollLeft && container.scrollLeft<=sectionPageWidth*2){
            container.scrollLeft=sectionPageWidth*1
            scrollLeft = 2
            this.$store.dispatch('page/pageChange',2)
            const audio = document.querySelector("audio[data-key=timo]")
            playSound(audio)
          }else{
            container.scrollLeft=sectionPageWidth*2
            scrollLeft = 3
            this.$store.dispatch('page/pageChange',3)
            const audio = document.querySelector("audio[data-key=wow]")
            playSound(audio)
          }
        }
        let scrollPercent = scrollLeft / scrollBottom * 100 + "%";
        document.getElementById("_progress").style.setProperty("--scroll", scrollPercent);
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
}
.container::after{
  content: '';
  position: absolute;
  top:0;
  left:0;
  width:100%;
  height: 100%;
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


#_progress {
  --scroll: 0%;
  background: linear-gradient(to right,#7E7E7E var(--scroll),lightgrey 0);
  position: fixed;
  right: 35%;
  width: 30%;
  height: 5px;
  bottom :15px;
  z-index: 10000000;
  }

</style>
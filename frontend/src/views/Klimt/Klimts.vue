<template>
  <div class="container">
    <div id="_progress"></div>
    <section>
      <IconMap mapColor="#eee8aa"/>
      <IconVoice voiceColor="#eee8aa"/>
      <Klimt1 id="klimt1" class="content"/>
      <Klimt2 id="klimt2" class="content"/>
      <Klimt3 id="klimt3" class="content"/>
    </section>
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

      let scrollBottom = 3;
      let scrollPage = 1;

      let delta = e.deltaY
      if(delta>0){
        if(container.scrollLeft>sectionPageWidth*1){
          this.page = 3
          scrollPage = 3
          return;
        }
        if(0<=container.scrollLeft && container.scrollLeft<sectionPageWidth*1){
          container.scrollLeft = sectionPageWidth*1
          scrollPage = 2
          this.$store.dispatch('page/pageChange',2)
        }else{
          container.scrollLeft=sectionPageWidth*2
          scrollPage = 3
          this.$store.dispatch('page/pageChange',3)
        }
      }else{
        if(container.scrollLeft<sectionPageWidth*1){
          scrollPage = 1
          this.$store.dispatch('page/pageChange',1)
          return;
        }
        if(0<=container.scrollLeft && container.scrollLeft<=sectionPageWidth*1){
          container.scrollLeft =0
          scrollPage = 1
          this.$store.dispatch('page/pageChange',1)
        }else{
          container.scrollLeft=sectionPageWidth*1
          scrollPage = 2
          this.$store.dispatch('page/pageChange',2)
        }
      }
      console.log(scrollPage)
      let scrollPercent = scrollPage / scrollBottom * 100 + "%";
      console.log(scrollPercent)
      document.getElementById("_progress").style.setProperty("--scroll", scrollPercent);
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
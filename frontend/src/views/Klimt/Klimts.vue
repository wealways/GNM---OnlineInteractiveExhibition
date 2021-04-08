<template>
  <div class="container">
    <div id="_progress"></div>
    <section>
      <IconMap mapColor="#608091"/>
      <IconVoice v-if="page!==1" voiceColor="#608091"/>
      <Klimt1 id="klimt1" class="content"/>
      <Klimt2 id="klimt2" class="content"/>
      <Klimt3 id="klimt3" class="content"/>
    </section>
  </div>
</template>


<script>
export default {
  name:'Klimts',
  components:{
    IconMap: () => import('@/components/IconMap/IconMap'),
    IconVoice: () => import('@/components/IconMap/IconVoice'),
    Klimt1: () => import('@/components/Klimt/klimt1'),
    Klimt2: () => import('@/components/Klimt/klimt2'),
    Klimt3: () => import('@/components/Klimt/klimt3'),
  },
  data(){
    return {
      
    }
  },
  computed:{
    page(){
      return this.$store.state.page.page
    }
  },
  watch:{
  },
  mounted: function (){
    
    // horizontal scroll 
    const container = document.querySelector('.container')
    const section = document.getElementsByTagName('section')
    const sectionPageWidth = section[0].clientWidth/3
    // let now = container.scrollLeft
    let scrollPage = 1;
    window.addEventListener('wheel', function(e)
    {
      if(this.$route.name==='Klimts'){
        e.preventDefault();
        let scrollBottom = 3;
        
        let delta = e.deltaY
        if(delta>0){
          if(container.scrollLeft>sectionPageWidth*2){
            scrollPage = 3
            return;
          }
          if(0<=container.scrollLeft && container.scrollLeft<sectionPageWidth*1){
            container.scrollLeft = sectionPageWidth*1
            scrollPage = 2
            this.$store.dispatch('page/pageChange',2)
           
          }else {
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
           
          }else if(sectionPageWidth*1<container.scrollLeft && container.scrollLeft<=sectionPageWidth*2){
            container.scrollLeft=sectionPageWidth*1
            scrollPage = 2
            this.$store.dispatch('page/pageChange',2)
            
          }
        }

        //   if(now === 0 ){
        //     container.scrollLeft = sectionPageWidth*1
        //     now += sectionPageWidth
        //     scrollPage = 2
        //     this.$store.dispatch('page/pageChange',2)
        //   }else if(now === sectionPageWidth*1){
        //     container.scrollLeft=sectionPageWidth*2
        //     now += sectionPageWidth
        //     scrollPage = 3
        //     this.$store.dispatch('page/pageChange',3)
        //   }else{
        //     now = sectionPageWidth*2
        //   }
        // }else{
          
        //   if(now===sectionPageWidth*2){
        //     container.scrollLeft = sectionPageWidth*1
        //     now -= sectionPageWidth
        //     scrollPage = 2
        //     this.$store.dispatch('page/pageChange',2)
        //   }else if(now===sectionPageWidth*1){
        //     container.scrollLeft = 0
        //     now -= sectionPageWidth
        //     scrollPage = 1
        //     this.$store.dispatch('page/pageChange',1)
        //   }else{
        //     now = 0
        //   }
        // }
        let scrollPercent = scrollPage / scrollBottom * 100 + "%";
        document.getElementById("_progress").style.setProperty("--scroll", scrollPercent);
      }
      
    }.bind(this), {passive: false,useCapture :true});


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
  --scroll: 33%;
  background: linear-gradient(to right,#7E7E7E var(--scroll),lightgrey 0);
  position: fixed;
  right: 35%;
  width: 30%;
  height: 5px;
  bottom :15px;
  z-index: 10000000;
  }

</style>
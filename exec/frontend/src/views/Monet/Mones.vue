<template>
  <div class="container">
    <div id="_progress"></div>
    <IconMap/>
    <IconVoice/>
    <section>
      <Mone1 class="content"/>
      <Mone2 class="content"/>
      <Mone3 class="content"/>
      <Mone4 class="content"/>
    </section>
  </div>
</template>

<script>
export default {
  name:'Mones',
  components:{
    IconMap: () => import('@/components/IconMap/IconMap'),
    IconVoice: () => import('@/components/IconMap/IconVoice'),
    Mone1: () => import('@/components/Mone/Mone1'),
    Mone2: () => import('@/components/Mone/Mone2'),
    Mone3: () => import('@/components/Mone/Mone3'),
    Mone4: () => import('@/components/Mone/Mone4'),
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

    const sectionPageWidth = section[0].clientWidth/4

     window.addEventListener('wheel', function(e)
    {
      if(this.$route.name==='Monets'){

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
           
          }else if(sectionPageWidth*1<=container.scrollLeft && container.scrollLeft<sectionPageWidth*2){
            container.scrollLeft=sectionPageWidth*2
            scrollLeft = 3
            this.$store.dispatch('page/pageChange',3)
            
          }else{
            container.scrollLeft=sectionPageWidth*3
            scrollLeft = 4
            this.$store.dispatch('page/pageChange',4)
            
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
           
          }else if(sectionPageWidth*1<container.scrollLeft && container.scrollLeft<=sectionPageWidth*2){
            container.scrollLeft=sectionPageWidth*1
            scrollLeft = 2
            this.$store.dispatch('page/pageChange',2)
            
          }else{
            container.scrollLeft=sectionPageWidth*2
            scrollLeft = 3
            this.$store.dispatch('page/pageChange',3)
            
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
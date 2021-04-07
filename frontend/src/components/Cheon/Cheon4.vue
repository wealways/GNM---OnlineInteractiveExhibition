<template>
    <div class="cheon4">
    <img id="img4" class="cheon4_pic slide-in" src="../../assets/sad22page.png" alt="내 슬픈 생애의 22페이지">
    <div id="title4" class="title slide-in"><h3>내 슬픈 <br>생애의 22페이지</h3></div>
    <div id="desc4" class="desc slide-in">
      자신의 과거와 현재에 걸치는 자서전적인 이미지를 작품에 담고 있습니다.
      천경자가 결혼을 하고 첫 딸을 낳았던 1945년 당시 22살이었던 천경자의 나이와 관계가 있습니다.
      그녀의 작품 중에는 자화상을 비롯한 여인상이 많습니다.
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cheon4',
  computed:{
    page(){
      return this.$store.state.page.page
    }
  },
  watch:{
    'page':function(){
      const img = document.querySelector('#img4')
      const desc = document.querySelector('#desc4')
      const title = document.querySelector('#title4')
      if(this.page===4){
        setTimeout(function(){
          img.classList.add('active-image');
        },500)
        setTimeout(function(){
          desc.classList.add('active-desc');
          title.classList.add('active-title');
        },700)
      } else {
        img.classList.remove('active-image');
        desc.classList.remove('active-desc');
        title.classList.remove('active-title');
      }
    }
  },
  



}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&family=Noto+Serif+KR:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i');





.cheon4 {
  position: relative;
    background-color: #eaeaea; 
}
.cheon4_pic{
  position: absolute;
  height: 100vh;
  right: 10% ;
  opacity:0;
  z-index: 500;
}

.title > h3 {
  font-family: 'Noto Serif KR', serif;
}

.title{
  position: absolute;
  top: 10% ;
  left: 3% ;
  text-shadow: 0 0 15px rgba(143, 143, 143, 0.658);
  opacity:0;
}

.desc{
  position: absolute;
  top: 60%; 
  left: 3%;
  width: 40%;
  font-size: 1rem;
  word-spacing: 5px;
  line-height:170%;
  font-family: 'Open Sans', sans-serif;
  opacity:0;
  z-index: 500;
}



.slide-in {
  opacity: 0;
  transition: all 1s;
}




#desc4.slide-in {
  transform: translateY(100%) scale(0.95);
}

.active-desc {
  opacity: 1 !important;
  transform: translateY(30%) scale(1) !important;
}


#title4.slide-in {
  transform: translateY(-100%) scale(0.95);
}

.active-title {
  opacity: 1 !important;
  transform: translateY(0%) scale(1) !important;
}


.active-image {
  opacity: 1 !important;
  transform: translateX(0%) scale(1) !important;
}

#img4.slide-in {
  transform: translateX(100%) scale(0.95);
}



</style>
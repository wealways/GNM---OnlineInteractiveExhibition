<template>
    <div class="cheon3">
      <img id="img" class="cheon3_pic slide-in" src="../../assets/저작권.jpg" alt="고(孤)">
      <div id="title" class="title slide-in"><h3>고(孤)</h3></div>
      <div id="desc3" class="desc slide-in">
        이 작품은 과거의 문헌에 실렸던 사진을 보면 원래 화관과 나비가 지금과는 미묘하게 달랐습니다.<br>
        후에 꽃의 수를 줄이고 디테일한 부분에서도 수정을 거친 작품입니다.<br>
        천경자 작가의 완벽주의적 성향을 확인할 수 있습니다
      </div>
    </div>
</template>

<script>
export default {
  name: 'Cheon3',
  computed:{
    page(){
      return this.$store.state.page.page
    }
  },
  watch:{
    'page':function(){
      const img = document.querySelector('#img')
      const desc = document.querySelector('#desc3')
      const title = document.querySelector('#title')
      if(this.page===3){
        setTimeout(function(){
          img.classList.add('active-image');
        },600)
        setTimeout(function(){
          desc.classList.add('active-desc');
          title.classList.add('active-title');
        },700)
      } else {
        img.classList.remove('active-image');
        title.classList.remove('active-title');
        desc.classList.remove('active-desc');
      }
    }
  },
  
  
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&family=Noto+Serif+KR:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i');


.cheon3{
  position: relative;
  z-index: -1;
  background-color: #eaeaea; 
}
.cheon3_pic{
  position: absolute;
  left: 13%;
  height: 100vh;
  opacity: 0;
}
.title{
  position: absolute;
  top: 65%; 
  left: 42%; 
  text-shadow: 0 0 15px rgba(143, 143, 143, 0.658);
  opacity: 0;
}

.title > h3 {
  font-family: 'Noto Serif KR', serif;
}

.desc{
  position: absolute;
  top: 55%; 
  width: 40%;
  font-size: 14px;
  word-spacing: 5px;
  line-height:170%;
  left: 47%;
  opacity: 0;
  z-index: 10;
  line-break: strict;
}




.slide-in {
  opacity: 0;
  transition: all 1s;
}




#desc3.slide-in {
  transform: translateY(-100%) scale(0.95);
}

.active-desc {
  opacity: 1 !important;
  transform: translateY(4%) scale(1) !important;
}


#title.slide-in {
  transform: translateY(100%) scale(0.95);
}

.active-title {
  opacity: 1 !important;
  transform: translateY(4%) scale(1) !important;
}


.active-image {
  opacity: 1 !important;
  transform: translateX(0%) scale(1) !important;
}

#img.slide-in {
  transform: translateX(-100%) scale(0.95);
}


</style>
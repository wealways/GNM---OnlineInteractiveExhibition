<template>
  <div class="cheon2">
    <img class="cheon2_pic slide-in" src="../../assets/저작권.jpg" alt="ecology" >
    <div class="desc slide-in" id="desc">
      <div class="title"><h3>생태</h3></div>
      <div class="description ">
        <p>[생태]를 그렸을 때 천경자는 폭우처럼 쏟아진 불행에 흠뻑 젖은 상태였습니다.</p>
        <p>집안이 몰락했고, 첫 번째 남편과 이혼했습니다.</p>
        <p>세상은 자신의 그림을 무시했습니다.</p>
        <p>어느 날 독을 품고 끊임없이 꿈틀거리는 뱀을 보자 응어리가 풀어지는 듯 했습니다.</p>
        <p>구렁텅이 같은 삶에 저항해야겠다는 의지가 생겼고</p>
        <p>뱀을 스케치한 결과 ‘생태’가 탄생했습니다.</p>
      </div>  

    </div>
  </div>
</template>

<script>
export default {
  name: 'Cheon2',
  computed:{
    page(){
      return this.$store.state.page.page
    }
  },
  watch:{
    'page':function(){
      const img = document.querySelector('.cheon2_pic')
      const description = document.querySelector('#desc')
      if(this.page===2){
        setTimeout(function(){
          img.classList.add('active');
          description.classList.add('active-description');
        },500)
      }else{
        img.classList.remove('active');
        description.classList.remove('active-description');
      }
    }
  },

}
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&family=Noto+Serif+KR:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i,800,800i');



img {
  float: left;
}
.cheon2{
  position: relative; 
  z-index: -1; 
  background-color: #eaeaea;

}

.cheon2_pic{
  width: 70%;
  position: absolute;
  font-size: 150%;
  text-shadow: 0 0 15px rgba(143, 143, 143, 0.658);
  position:absolute;
  left: 8%; 
}


.title{
  top: 10%;
  right: 15%;
  writing-mode: vertical-rl;
  position: absolute;
  font-size: 150%;
  text-shadow: 0 0 15px rgba(143, 143, 143, 0.658);
}

.title > h3 {
  font-family: 'Noto Serif KR', serif;
}


.desc {
  opacity: 0;
  width: 100%;
  height: 100%;

}

.description{
  top: 10%; 
  right: 5%;
  position: absolute;
  font-size: 1rem;
  writing-mode: vertical-lr;
  text-orientation: mixed;
  line-height: 200%;
  transition: all 1s;
}

.description > p {
  font-size: 15px;
}

.active {
  opacity: 1 !important;
}
.active-description{
  opacity: 1 !important;
  transform: translateY(0%) scale(1) !important;
}

.slide-in {
  opacity: 0;
  transition: all 1s;
}

#desc.slide-in {
  transform: translateY(-100%) scale(0.95);
}
.title{
  top: 10%;
  right: 15%;
  writing-mode: vertical-rl;
  position: absolute;
  text-shadow: 0 0 15px rgba(143, 143, 143, 0.658);
}
.description{
  top: 10%; 
  right: 5%;
  position: absolute;
  font-size: 1rem;
  writing-mode: vertical-lr;
  text-orientation: mixed;
  line-height: 200%;
}
</style>

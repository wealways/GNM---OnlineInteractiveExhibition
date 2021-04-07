<template>
    <div class="cheon3">
      <img class="cheon3_pic" src="../../assets/kingGo.jpg" alt="고(孤)">
      <div class="title"><h1>고(孤)</h1></div>
      <div class="description">
        <p>이 작품은 과거의 문헌에 실렸던 사진을 보면 원래 화관과 나비가 지금과는 미묘하게 달랐습니다. </p>
        <p>후에 꽃의 수를 줄이고 디테일한 부분에서도 수정을 거친 작품입니다.</p> 
        <p>천경자 작가의 완벽주의적 성향을 확인할 수 있습니다.</p>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Cheon3',
}
</script>

<style scoped>
.cheon3{
  position: relative;
  background-color: #F2F2F2;
  z-index: -1; 
}
.cheon3_pic{
  position: absolute;
  left: 13%;
  height: 100vh;
}
.title{
  position: absolute;
  top: 65%; 
  left: 47%; 
  text-shadow: 0 0 15px rgba(143, 143, 143, 0.658);
}
.description{
  position: absolute;
  top: 35%; 
  font-size: 1rem;
  left: 47%;
}
</style>
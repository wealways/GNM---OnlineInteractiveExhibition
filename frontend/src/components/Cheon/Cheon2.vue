<template>
  <div class="cheon2">
    <img class="cheon2_pic" src="../../assets/ecology.png" alt="ecology" >
      <div class="title"><h1>생태</h1></div>
      <div class="description">
      <p>'생태'를 그렸을 때 천경자는 폭우처럼 쏟아진 불행에 흠뻑 젖은 상태였습니다. </p>
      <p>집안이 몰락했고, 첫 번째 남편과 이혼했습니다.</p> 
      <p>세상은 자신의 그림을 무시했습니다.</p> 
      <p>어느 날 독을 품고 끊임없이 꿈틀거리는 뱀을 보자 응어리가 풀어지는 듯 했습니다.</p>
      <p>구렁텅이 같은 삶에 저항해야겠다는 의지가 생겼고</p>
      <p>뱀을 스케치한 결과 ‘생태’가 탄생했습니다.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cheon2',
 
}
</script>

<style scoped>

img {
  float: left;
}
.cheon2{
  position: relative; 
  z-index: -1; 
}
.cheon2_pic{
  width: 70%;
  height: 100vh;
}
.title{
  top: 10%;
  right: 15%;
  writing-mode: vertical-rl;
  position: absolute;
  font-size: 150%;
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

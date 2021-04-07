<template>
    <div class="cheon4">
    <img class="cheon4_pic" src="../../assets/sad22page.png" alt="내 슬픈 생애의 22페이지">
    <div class="title"><h1>내 슬픈 <br>생애의 22페이지</h1></div>
    <div class="description">
      <p>자신의 과거와 현재에 걸치는 자서전적인 이미지를 작품에 담고 있습니다.</p> 
      <p>천경자가 결혼을 하고 첫 딸을 낳았던 1945년 당시 22살이었던 천경자의 나이와 관계가 있습니다.</p> 
      <p>그녀의 작품 중에는 자화상을 비롯한 여인상이 많습니다.</p> 
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cheon4',
}
</script>

<style scoped>
.cheon4 {
  position: relative;
}
.cheon4_pic{
  position: absolute;
  height: 100vh;
  right: 10% ;
}
.title{
  position: absolute;
  top: 10% ;
  left: 3% ;
  text-shadow: 0 0 15px rgba(143, 143, 143, 0.658);
}
.description{
  position: absolute;
  top: 60%; 
  left: 3%;
  font-size: 1rem;

}
</style>
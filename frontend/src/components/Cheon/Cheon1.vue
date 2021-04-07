<template>
  <div class="cheon1">
    <img class="cheon1_pic" src="../../assets/GilryeSister.jpg" alt="ecology">
    <div class="title" ><h1>길례언니</h1></div>
    <div class="description">
      <p>그녀의 작품 중에는 자화상을 비롯한</p>
      <p>여인상이 많습니다.</p> 
      <p>가난 때문에 타지에서 간호부로 일하면서</p>
      <p>동생들을 책임지는 가장이었던 길례 언니는</p>
      <p>화가가 소학교 시절 동경했던 선배입니다.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Cheon1',
}
</script>

<style scoped>
.cheon1{
  position: relative;
  text-align: center;
}
.cheon1_pic{
  height: 100vh;
  animation: fadein 3s;
  /* -webkit-animation: fadein 3s; */
}

.title{
  position: absolute;
  top: 20% ;
  margin: 3% ;
  text-shadow: 0 0 15px rgba(143, 143, 143, 0.658);
}
@-webkit-keyframes fadein { /*Safari and Chrome */
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
.description {
  position: absolute;
  top: 60%;
  right: 8%;
  text-align: left;
  font-size: 1rem;
}

</style>

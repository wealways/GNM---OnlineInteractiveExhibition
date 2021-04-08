<template>
  <div class="container">
    <figure>
    <div class="frame">
      <img :src="changedImage" alt="img01">
    </div>
    <figcaption>
      <div class="description">
        <p><strong>{{artist}}</strong> 작가의 화풍으로 변환된 사진입니다</p>
      </div>
    </figcaption>
    </figure>
  </div>
</template>

<script>
export default {
  name: 'Output',
  props:{
    changedImage:String,
    artist:String
  }
}
</script>

<style scoped>
/* 사진 밖 프레임 */
.frame {
  -webkit-box-sizing: content-box;
	-moz-box-sizing: content-box;
	box-sizing: content-box;
  position: relative;
  border: 12px solid #b4a79a;
  box-shadow: 0 10px 7px -5px rgba(0,0,0,0.3);
}

/* 사진 */
.frame img {
  display: block;
  margin: 0 auto;
  border: 15px solid #ececec;
}

/* 사진 설명 */
.container figcaption {
	min-width: 80px;
  max-width: 140px;
	display: flex;
	font-size: 10px;
	background: #ececec;
	color: #444;
	padding: 5px;
	margin-top: 20px;
	position: relative;
	text-align: left;
	cursor: -webkit-zoom-in; 
	box-shadow: 0 1px 2px rgba(0,0,0.5,0.5);
}

.container figcaption div {
  width: 90%;
	display: flex;
	margin: 0 2px;
  font-size: 10px;
  word-break: break-all;
}
/* 작품 설명 내용 */
.description p {
  margin: 0;
  /* font-size: 18px; */
}
</style>
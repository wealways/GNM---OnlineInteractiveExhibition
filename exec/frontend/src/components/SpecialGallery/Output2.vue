<template>
  <div class="container">
    <figure>
      <div class="frame paint" id="paint">
        <img src="@/assets/monet.jpg" alt="img01">
      </div>
      <figcaption>
        <div class="description">
          <button><strong>천경자</strong> 작가의 화풍으로 변환된 사진입니다</button>
        </div>
      </figcaption>
    </figure>
    <figure class="big bigframe" id="bigframe">
      <div class="frame bigimage" id="bigimage">
        <img src="@/assets/monet.jpg" alt="img01">
      </div>
      <figcaption>
        <div class="description">
          <button><strong>천경자</strong> 작가의 화풍으로 변환된 사진입니다</button>
        </div>
      </figcaption>
    </figure>
  </div>
</template>

<script>
export default {
  name: 'Output',
  mounted: function () {
    const paint = document.querySelector('.paint')
    const bigframe = document.querySelector('.bigframe')
    const bigimage = document.querySelector('.bigimage')
    paint.addEventListener('click', function() {
      bigframe.classList.add('zoom')
      bigframe.classList.remove('big')
    })
      bigimage.addEventListener('click', function() {  
      bigframe.classList.remove('zoom')
      bigframe.classList.add('big')
    })

  }
}
</script>

<style scoped>


.big {
  display: none;
}

.zoom {
  animation:move 3s;
  position: absolute;
  top:25%;
  left: 30%;
  z-index : 3;
  animation-fill-mode: forwards;
}


@keyframes move{
0%{
 transform: scale(1) rotate(0deg);
}
  100%{
   transform: scale(1.8) rotate(0.1deg);

  }

}

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
	/* position: relative; */
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
<template>
  <div class="container">
    <!-- <div style="" id="stop">
    </div> -->
    <figure>
      <div class="frame paint" id="paint" style="cursor: pointer;">
        <img :src="changedImage" alt="img01">
      </div>
      <figcaption>
        <div class="description">
          <p><strong>{{artist}}</strong> 작가의 화풍으로 <br>변환된 사진입니다</p>
        </div>
      </figcaption>
    </figure>
    
    <figure class="big bigframe" :id="artist">
      <div class="frame bigimage" id="bigimage">
        <img :src="changedImage" alt="img01">
      </div>
      <div class="btn__save" @click="downloadImg">
        <q-btn class="btn" label="저장" size="10px"/>
      </div>
    </figure>
  </div>
</template>

<script>
export default {
  name: 'Output',
  props:{
    changedImage:String,
    artist:String
  },
  mounted: function () {
    const paints = document.querySelectorAll('.paint')
    const bigframes = document.querySelectorAll('.bigframe')
    paints.forEach((paint,idx)=>{
      const bigframe = bigframes[idx]
      const bigimage = bigframe.querySelector('.bigimage')
      paint.addEventListener('click', function() {
        bigframe.classList.add('zoom')

        const div = document.createElement("div")
        div.setAttribute("style", "background-color: #000; width: 100vw; height: 100vh; position: static; z-index:1; opacity: 0.2;")
        div.setAttribute("id","stop")
        const target = document.getElementsByClassName("container")[0]
        target.before(div)

        bigframe.setAttribute('style', "left :"+ (window.innerWidth-bigframe.getBoundingClientRect().width)/2 + "px");

        bigframe.classList.remove('big')
      })
        bigimage.addEventListener('click', function() {  
        const stop = document.querySelector('#stop')
        stop.parentNode.removeChild(stop)
        bigframe.classList.remove('zoom')
        bigframe.classList.add('big')
      })
    })
  },
  methods:{
    dataURLtoBlob(dataurl) {
      var arr = dataurl.split(','),
        mime = arr[0].match(/:(.*?);/)[1],
        bstr = atob(arr[1]),
        n = bstr.length,
        u8arr = new Uint8Array(n);
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
      }
      return new Blob([u8arr], {
        type: mime
      });
    },

    downloadImg() {
      var image = new Image();
      image.crossOrigin = "anonymous";
      console.log(this.changedImage)
      image.src = this.changedImage;
      var fileName = image.src.split("/").pop();
      image.onload = function() {
        var canvas = document.createElement('canvas');
        canvas.width = this.width;
        canvas.height = this.height;
        canvas.getContext('2d').drawImage(this, 0, 0);
        if (typeof window.navigator.msSaveBlob !== 'undefined') {
          window.navigator.msSaveBlob(this.dataURLtoBlob(canvas.toDataURL()), fileName);
        } else {
          var link = document.createElement('a');
          link.href = canvas.toDataURL();
          link.download = fileName;
          link.click();
        }
      };
    }
  }
}
</script>

<style scoped>
.btn__save{
  display: flex;
  justify-content: flex-end;
}
.btn {
  margin: 3% 0;
  border-radius: 78px;
  background: #e0e0e0;
  box-shadow:  21px 21px 53px #b5b5b5,
            -21px -21px 53px #ffffff;
  background-color: #ececec;
  color: #695c4c;
  cursor: pointer;
}
/* .btn:hover {
  background-color: #f000;
} */
/* #stop{
  height:100vh;
  width:100vw;
  z-index:-2;
  position:absolute;
  background-color:#4d4d4d;
  opacity: 0.2;
  top:0;
  left:0;
} */
.bigframe{
  margin:0;
  cursor: pointer;
}

.big {
  display: none;
}

.zoom {
  animation:move 3s;
  position: absolute;
  top:20%;
  /* left: 35%; */
  /* top: 50%;
  left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  margin:0; */
  z-index : 4;
  animation-fill-mode: forwards;
}


@keyframes move{
0%{
 transform: scale(1) rotate(0deg);
}
  100%{
   transform: scale(1.5) rotate(0.1deg);

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
  max-height: 30vh;
  max-width: 40vw;
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
    /* cursor: -webkit-zoom-in;  */
    box-shadow: 0 1px 2px rgba(0,0,0.5,0.5);
}

.container figcaption div {
  /* width: 90%; */
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
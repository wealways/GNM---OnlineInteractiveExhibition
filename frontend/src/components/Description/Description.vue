<template>
  <div>
    <div class="imsrk2">
      Let's start!
    </div>
    <div class='blank'></div>
    <div class='info' style="font-size:25px;">
      <div class='map_description'>
          평면도입니다. 현 위치를 알 수 있고 다른 층을 클릭하여 이동할 수 있습니다.
      </div>
      <div class='voice_description'>
          음성 설명
      </div>
      <!-- <div class='text_description'>
          텍스트 설명
      </div> -->
      <div class='next_button'>
        <button>next</button>
      </div>
    </div>
    <Icon/>
  </div>
</template>

<script>
import { gsap } from 'gsap';
import Icon from '../Icon/Icon.vue'

export default {
  name: 'Description',
  components: { Icon },
  mounted: function(){
      let tl = gsap.timeline();
      tl.from(
        ".imsrk2",
        {
          xPercent: -100,
          duration: 1,
          ease: "power1.out",
          opacity: 0,
        },
      );
      tl.from(
        ".blank",
        {
          xPercent: -100,
          duration: 0.2,
          ease: "power1.out",
          opacity: 0,
        },
      );
    
      tl.from(
        ".map_description",
        {
          xPercent: -100,
          duration: 1,
          ease: "power1.out",
          opacity: 0,
        },
      );
      tl.from(
        ".voice_description",
        {
          xPercent: -100,
          duration: 1,
          ease: "power1.out",
          opacity: 0,
        },
      );
      tl.from(
        ".text_description",
        {
          xPercent: -100,
          duration: 1,
          ease: "power1.out",
          opacity: 0,
        },
      );
      tl.from(
        ".next_button",
        {
          xPercent: -100,
          duration: 0.5,
          ease: "power1.out",
          opacity: 0,
        },
      );                  
  }
}
</script>

<style scoped>

.info {
  font-family: 'Noto Sans KR';
  font-weight: 900;
}
.blank {
  background: -webkit-gradient(linear, left top, left bottom, from(white), to(white));
  background: linear-gradient(to bottom, white, white);
  position: absolute;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}
.imsrk2 {
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  color: blac;
  font-size: 72px;
  font-weight: 900;
  z-index: -1;
  color: #2d2d2d;
  font-family: "Roboto", sans-serif;
  letter-spacing: -4px;
  line-height: 1;
}
.next_button {
  position: absolute;
  left: 45%;
  top: 45%;
  font-size: 72px;
  font-weight: 800;
  font-family: 'Roboto';
}
button {
  background-color: transparent;
  border: 0;
  outline: 0;
}
button:hover {
  color: orange;
}
.map_description {
  position: absolute;
  left: 3%;
  top: 12%;
}
.voice_description {
  position: absolute;
  right: 10%;
  bottom: 14%;
}
.text_description {
  position: absolute;
  right: 10%;
  bottom: 7%;
}
</style>
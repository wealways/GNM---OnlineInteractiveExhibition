<template>
  <div>
    <div class="imsrk2">
      Let's start!
    </div>
    <div class='blank'></div>
    <div class='info' style="font-size:20px;">
      <div class='map_description'>
        평면도입니다. 현 위치를 알 수 있고 다른 층을 클릭하여 이동할 수 있습니다.
      </div>
      <div class='voice_description'>
        음성 설명
      </div>
      <div class='next_button'>
        <div class="wrapper">
          <div class="link_wrapper">
            <router-link :to='"/mappage"'>NEXT</router-link>
            <div class="icon">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 268.832 268.832">
                <path d="M265.17 125.577l-80-80c-4.88-4.88-12.796-4.88-17.677 0-4.882 4.882-4.882 12.796 0 17.678l58.66 58.66H12.5c-6.903 0-12.5 5.598-12.5 12.5 0 6.903 5.597 12.5 12.5 12.5h213.654l-58.66 58.662c-4.88 4.882-4.88 12.796 0 17.678 2.44 2.44 5.64 3.66 8.84 3.66s6.398-1.22 8.84-3.66l79.997-80c4.883-4.882 4.883-12.796 0-17.678z"/>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
    <IconMap/>
    <IconVoice/>
  </div>
</template>

<script>
import { gsap } from 'gsap';
import IconMap from '@/components/IconMap/IconMap.vue'
import IconVoice from '@/components/IconMap/IconVoice.vue'

export default {
  name: 'Description',
  components: { IconMap, IconVoice },
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
          duration: 0.8,
          ease: "power1.out",
          opacity: 0,
        },
      );
      tl.from(
        ".next_button",
        {
          xPercent: -100,
          duration: 0.7,
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
  top: 14%;
}
.voice_description {
  position: absolute;
  right: 13%;
  bottom: 9%;
}
.text_description {
  position: absolute;
  right: 10%;
  bottom: 7%;
}

.wrapper{
  position: fixed;
  top: 55%;
  left: 55%;
  transform: translate(-20%, -10%);
}

.link_wrapper{
  position: relative;
}

a{
  font-size:22px;
  display: block;
  width: 250px;
  height: 50px;
  line-height: 50px;
  font-weight: bold;
  text-decoration: none;
  background: #333;
  text-align: center;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: 1px;
  border: 3px solid #333;
  transition: all .35s;
}

.icon{
  width: 50px;
  height: 50px;
  border: 3px solid transparent;
  position: absolute;
  transform: rotate(45deg);
  right: 0;
  top: 0;
  z-index: -1;
  transition: all .35s;
}

.icon svg{
  width: 30px;
  position: absolute;
  top: calc(50% - 15px);
  left: calc(50% - 15px);
  transform: rotate(-45deg);
  fill: #2ecc71;
  transition: all .35s;
}

a:hover{
  width: 200px;
  border: 3px solid #2ecc71;
  background: transparent;
  color: #2ecc71;
}

a:hover + .icon{
  border: 3px solid #2ecc71;
  right: -25%;
}
</style>
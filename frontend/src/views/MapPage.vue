<template>
  <div class='container'>
    <div class='mymap'>
      <div class="layer-container stacked-top">
          <div @click='gotomone' class="layer first-layer blue-layer"></div>
          <div @click='gotoklimt' class="layer second-layer green-layer"></div>
          <div @click='gotocheon' class="layer third-layer red-layer"></div>
          <div @click='gotospecial' class="layer fourth-layer red-layer"></div>
          <div @click='gotoguestbook' class="layer fifth-layer red-layer"></div>
      </div>
      <div class='right_side'>
          <div class='artist'>{{ explain }}</div>
          <div class='go_button' style='margin-top:20px;'>
              <q-btn 
                  :to='"/startmonet"' 
                  target="_blank" 
                  v-show="explain==='모네'" 
                  align="around" 
                  class="btn-fixed-width" 
                  color="teal-10" 
                  label="1층 가기" 
                  icon="lightbulb_outline"
              />
              <q-btn
                  :to='"/startklimt"' 
                  target="_blank"  
                  v-show="explain==='클림트'" 
                  align="around" 
                  class="btn-fixed-width" 
                  color="teal-10" 
                  label="2층 가기" 
                  icon="lightbulb_outline" 
              />
              <q-btn
                  :to='"/startcheon"' 
                  target="_blank"  
                  v-show="explain==='천경자'" 
                  align="around" 
                  class="btn-fixed-width" 
                  color="teal-10" 
                  label="3층 가기" 
                  icon="lightbulb_outline" 
              />
              <q-btn
                  :to='"/specialgallery"' 
                  target="_blank"  
                  v-show="explain==='특별전시관'" 
                  align="around" 
                  class="btn-fixed-width" 
                  color="teal-10" 
                  label="특별전시관" 
                  icon="lightbulb_outline" 
              />
              <q-btn
                  :to='"/guestbook"' 
                  target="_blank"  
                  v-show="explain==='방명록'" 
                  align="around" 
                  class="btn-fixed-width" 
                  color="teal-10" 
                  label="방명록 가기" 
                  icon="lightbulb_outline" 
              />
          </div>
      </div>
      <div class='choose'>전시회 안내도</div>
      <div class='choose2'>Exhibition Map</div>
    </div>
    <router-link :to='"/startmonet"'>
      <button class="learn-more">
        <span class="circle" aria-hidden="true">
          <span class="icon arrow"></span>
        </span>
        <span class="button-text">바로 입장하기</span>
      </button>
    </router-link>
  </div>
</template>

<script>

export default {
  name:'MapPage',
  data(){
      return{
          explain: 'LOBBY'
      }
  },
  methods:{
      gotomone(){
          this.explain = "모네"
      },
      gotoklimt(){
          this.explain = "클림트"
      },
      gotocheon(){
        this.explain = "천경자"
      },
      gotospecial(){
        this.explain = "특별전시관"
      },
      gotoguestbook(){
        this.explain = "방명록"
      }
  },

}
</script>
<style lang="scss" scoped>
span {
  font-family: 'Noto Sans KR';
}
.container {
  overflow-y: hidden;
}
.choose{
  font-family: 'Noto Sans KR';
  font-weight: 600;
  position:absolute;
  top: 15%;
  left: 10%;
  font-size: 20px;
}
.choose2{
  font-family: 'Noto Sans KR';
  font-weight: 600;
  position:absolute;
  top: 11%;
  left: 10%;
  font-size: 20px;
}
.right_side {
    position: absolute;
    height: 40vh;
    font-family: 'Noto Sans KR';
    font-weight: 600;
    left: 10%;
    bottom: 5%;
}

.artist {
  position: absolute;
  bottom: 10%;
  font-size: 24px;
}

.mymap {
  background-color: #FCF9F2;
  border-radius: 15px;
  color: #464646;
  position: absolute;
  width: 50vw;
  height: 80vh;
  left: 6%;
  top: 10%;
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
}
.layer-container {
    width: 200px;
    height: 330px;
    position: absolute;
    top: 64%;
    right: 30%;
    margin: -100px -100px 50px -200px;
    perspective: 2000px;
    transform-style: preserve-3d;
}

.layer {
    width: 200px;
    height: 200px;
    position: absolute;
    transition: all 0.5s ease-in-out;
    cursor: pointer;
    opacity: 0.95;
}

.layer:hover {
  opacity: 1;
  background-color: #2A433B;
}

.first-layer {
    transform: rotateX(45deg) rotateZ(25deg) translateZ(0);
    background: #696969;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 5;

}

.second-layer {
    transform: rotateX(45deg) rotateZ(25deg) translateZ(50px);
    background:#7D7D7D;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 4;

}

.third-layer {
    transform: rotateX(45deg) rotateZ(25deg) translateZ(100px);
    background:#9E9E9E;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 3;
}

.fourth-layer {
    transform: rotateX(45deg) rotateZ(25deg) translateZ(150px);
    background: #BDBDBD;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 2;
}

.fifth-layer {
    transform: rotateX(45deg) rotateZ(25deg) translateZ(200px);
    background: #D3D3D3;
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 1;
}

.marker {
  transition: all 0.5s ease-in-out;
  opacity: 0.75;
}

.marker:hover {
  opacity: 1.0;
}

/* A N I M A T I O N S */

@keyframes stack-move-top-3d{
   0%{
       transform: rotateX(45deg) rotateZ(45deg) translateZ(100px);
    }
    50%{
        transform: rotateX(45deg) rotateY(90deg) rotateZ(45deg) translate3d(-50px,100px,170px);
    }
    
   100%{
        transform: rotateX(45deg) rotateZ(45deg) translateZ(200px);
    }
}

.animate{
   animation: stack-move-top-3d 1.5s ease-in-out ;
}
    
/* for bottom-layer*/
    
.bottom.animate{
  animation: bottom-move-top-3d 1.5s ease-in-out;
}
     
@keyframes bottom-move-top-3d {
   0%{
       transform: rotateX(45deg) rotateZ(45deg) translateZ(0px);
    } 
 
    50%{
        transform: rotateX(45deg) rotateY(90deg) rotateZ(45deg) translate3d(-50px,100px,170px);
    }
    
   100%{
        transform: rotateX(45deg) rotateZ(45deg) translateZ(200px);
    }
}

.highlight {
  opacity: 1.0;
}

.fade {
  opacity: 0.15;
}

</style>
<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Mukta:700');

$bg: #f3f8fa;
$white: #fff;
$black: #282936;

@mixin transition($property: all, $duration: 0.45s, $ease: cubic-bezier(0.65,0,.076,1)) {
  transition: $property $duration $ease;
}

button {
  position: absolute;
  right: 13%;
  bottom: 45%;
  display: inline-block;
  cursor: pointer;
  outline: none;
  border: 0;
  vertical-align: middle;
  text-decoration: none;
  background: transparent;
  padding: 0;
  font-size: inherit;
  font-family: inherit;
  &.learn-more {
    width: 12rem;
    height: auto;
    .circle {
      @include transition(all, 0.45s, cubic-bezier(0.65,0,.076,1));
      position: relative;
      display: block;
      margin: 0;
      width: 3rem;
      height: 3rem;
      background: $black;
      border-radius: 1.625rem;
      .icon {
        @include transition(all, 0.45s, cubic-bezier(0.65,0,.076,1));
        position: absolute;
        top: 0;
        bottom: 0;
        margin: auto;
        background: $white;
        &.arrow {
          @include transition(all, 0.45s, cubic-bezier(0.65,0,.076,1));
          left: 0.625rem;
          width: 1.125rem;
          height: 0.125rem;
          background: none;
          &::before {
            position: absolute;
            content: '';
            top: -0.25rem;
            right: 0.0625rem;
            width: 0.625rem;
            height: 0.625rem;
            border-top: 0.125rem solid #fff;
            border-right: 0.125rem solid #fff;
            transform: rotate(45deg);
          }
        }
      }
    }
    .button-text {
      @include transition(all, 0.45s, cubic-bezier(0.65,0,.076,1));
      position: absolute;
      top: 0;
      left: 6px;
      right: 0;
      bottom: 0;
      padding: 0.75rem 0;
      margin: 0 0 0 1.85rem;
      color: $black;
      font-weight: 700;
      line-height: 1.6;
      text-align: center;
      text-transform: uppercase;
    }
  }
  &:hover {
    .circle {
      width: 100%;
      .icon {
        &.arrow {
        background: $white;
        transform: translate(1rem, 0);
        }
      }
    }
    .button-text {
      color: $white;
    }
  }
}

</style>
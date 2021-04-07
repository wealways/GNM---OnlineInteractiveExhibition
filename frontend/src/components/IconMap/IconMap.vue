<template>
  <div>
    <div @click="fullWidth = true">
      <span style="font-size:40px;">
        <q-icon class='map' name="mdi-map-legend"></q-icon>
      </span>
    </div>
    <q-dialog
      v-model="fullWidth"
    >
      <q-card class="mapwrapper" style="width: 900px; max-width: 80vw; height: 500px; max-height: 80vh;" >
        <q-card-section class='q-pt-none mapback'>
          <Floors/>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import Floors from '../IconMap/Floors'
export default {
  name:'IconMap',
  components: { Floors },
  props:{
    mapColor:String,
  },
  data() {
    return {
      fullWidth: false,
    }
  },
  mounted(){
    if(this.mapColor !==null){
      document.querySelector('.map').style.color=this.mapColor
    }
  }
}
</script>

<style scoped>

.mapback {
  height: 80%;
}

.mapwrapper {
  background-color: #FCF9F2;
  overflow-y: hidden;
  border-radius: 15px;
  color: #464646;
}


.close-btn{
  top:20px;
  right:20px;
  position: absolute;
  z-index: 100;
  /* background-color: teal; */
  background-color: #fe2901;
  color:white;
  font-size: 1.2rem;
}

.map {
  position: absolute;
  z-index: 9999;
  left: 3%;
  top: 4%;
  padding:10px;
  background-color: transparent;
  color: rgba(0,0,0,0.5);
  background: rgba(0,0,0, 0.1);
  border-radius: 50%;
}

.map:hover {
  color: rgba(0,0,0,0.8);
  background: rgba(0,0,0, 0.2);
  font-size:42px;
}

</style>
// <style lang="scss" scoped>
// $toggler-size: 40px;
// $toggler-color: white;
// $toggler-transition: transform .5s, top .5s;

// $item-count: 6;
// $item-size: $toggler-size * 2;
// $item-color: white;
// $item-transition: .5s;

// @mixin size ($width, $height: $width) {
//   width: $width;
//   height: $height;
// }

// @mixin absolute-center {
//   position: absolute;
//   display: block;
//   top: 0;
//   bottom: 0;
//   right: 0;
//   left: 0;
//   margin: auto;
// }

// @mixin line {
//   @include size($toggler-size, $toggler-size/8);
//   display: block;
//   z-index: 1;
//   border-radius: $toggler-size/16;
//   background: rgba($toggler-color, 0.7);
//   transition: $toggler-transition;
// }
// .menu-item a {
//   display: block;
//   width: inherit;
//   height: inherit;
//   line-height: $item-size;
//   color: rgba($item-color, 0.7);
//   background: rgba(white, 0.2);
//   border-radius: 50%;
//   text-align: center;
//   text-decoration: none;
//   font-size: $item-size/2;
//   pointer-events: none;
//   transition: .2s;
  
//   &:hover {
//     box-shadow: 0 0 0 $item-size/40 rgba(white, 0.3);
//     color: $item-color;
//     background: rgba(white, 0.3);
//     font-size: $item-size/1.8;
//   }
// }
// </style>
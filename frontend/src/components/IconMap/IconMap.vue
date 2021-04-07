<template>
  <div>
    <div @click="fullWidth = true">
      <span style="font-size:50px;">
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
  top: 5%;
  background-color: transparent;
}

.map {
  z-index:900;
  position: absolute;
  left: 3%;
  top: 4.3%;
  background-color: transparent;
}
.map:hover {
  color: red !important;
}
</style>
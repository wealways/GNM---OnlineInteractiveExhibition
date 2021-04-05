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
  /* background-color: #FCF9F2; */
  /* color:pink !important; */
}

.map {
  position: absolute;
  left: 3%;
  top: 4.3%;
  background-color: transparent;
}
.map:hover {
  color: red !important;
}
</style>
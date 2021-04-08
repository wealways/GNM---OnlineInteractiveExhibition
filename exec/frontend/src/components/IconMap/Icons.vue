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
      <q-card style="width: 900px; max-width: 80vw; height: 500px; max-height: 80vh;" class="mapwrapper">
        <q-card-section class='q-pt-none mapback'>
          <Floors/>
           <q-btn icon="close" flat round dense v-close-popup class="close-btn"/>
        </q-card-section>
      </q-card>
    </q-dialog>
  
    <span style='font-size:45px;'>
      <div @click='voiceOnOff'>
        <q-icon v-if="voice" class='voice' name="mdi-account-tie-voice"></q-icon>
        <q-icon v-else class='voice-off' name="mdi-account-tie-voice-off"></q-icon>
      </div>
    </span>
  </div>
</template>

<script>
import Floors from '../IconMap/Floors'
export default {
  name:'Icons',
  components: { Floors },
  data(){
    return { 
      voice: true,
      fullWidth: false,
    }
  },
  methods: {
    voiceOnOff(){
      if(this.voice===true){
        this.voice = false;
      } else {
        this.voice = true;
      }
    }
  }
}
</script>

<style scoped>

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


.mapback {
  height: 80%;
}
.map {
  position: absolute;
  z-index: 9999;
  left: 3%;
  top: 5%;
  background-color: transparent;
}
.voice{
  z-index: 96;
  position: fixed;
  bottom: 13%;
  right: 5%;
}
.voice:hover{
  z-index: 97;
  color: red;
}
.voice-off:hover{
  z-index: 98;
  color:red;
}
.voice-off{
  z-index: 99;
  position: absolute;
  z-index: 9999;
  bottom: 10%;
  right: 5%;
}
.map:hover {
  color: red;
}
</style>
<template>
  <div>
    <button @click="fullWidth = true">
      <span style="font-size:50px;">
        <q-icon class='map' name="mdi-map-legend"></q-icon>
      </span>
    </button>
    <q-dialog
      v-model="fullWidth"
    >
      <q-card style="width: 900px; max-width: 80vw; height: 500px; max-height: 80vh;">
        <q-card-section class='q-pt-none mapback'>
          <Floors/>
        </q-card-section>
        <q-card-actions align="right" class="bg-white text-teal">
        </q-card-actions>
      </q-card>
    </q-dialog>
  
    <span style='font-size:45px;'>
      <button @click='voiceOnOff'>
        <q-icon v-if="voice" class='voice' name="mdi-account-tie-voice"></q-icon>
        <q-icon v-else class='voice-off' name="mdi-account-tie-voice-off"></q-icon>
      </button>
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
.mapback {
  height: 80%;
}
.map {
  position: absolute;
  left: 3%;
  top: 5%;
  background-color: transparent;
}
.voice{
  position: absolute;
  bottom: 13%;
  right: 5%;
}
.voice-off{
  position: absolute;
  bottom: 13%;
  right: 5%;
}
button:hover {
  color: red;
}
</style>
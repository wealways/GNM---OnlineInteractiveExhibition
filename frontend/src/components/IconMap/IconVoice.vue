<template>
  <div>
    <span style='font-size:45px;'>
      <div @click='voiceOnOff'>
        <q-icon id="voice-color" v-if="voice" class='voice' name="mdi-account-tie-voice"></q-icon>
        <q-icon id="voice-color" v-else class='voice-off' name="mdi-account-tie-voice-off"></q-icon>
      </div>
    </span>
  </div>
</template>

<script>
export default {
  name:'IconVoice',
  props:{
    voiceColor:String,
  },
  data(){
    return {
      voice: true,
    }
  },
  mounted() {
    if(this.voiceColor){
      document.querySelector('#voice-color').style.color=this.voiceColor
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
.voice{
  position: absolute; 
  bottom: 13%;
  right: 5%;
}
.voice:hover{
  color: red !important;
}
.voice-off:hover{
  color:red !important;
}
.voice-off{
  position: absolute;
  bottom: 13%;
  right: 5%;
}
</style>
<template>
  <div>
    <span style='font-size:45px;'>
      <div @click='voiceOnOff'>
        <q-icon v-if="voice" class='voice' name="mdi-account-tie-voice"></q-icon>
        <q-icon v-else class='voice-off' name="mdi-account-tie-voice-off"></q-icon>
      </div>
    </span>
  </div>
</template>

<script>
export default {
  name:'IconVoice',
  data(){
    return {
      voice: true,
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
  color: red;
}
.voice-off:hover{
  color:red;
}
.voice-off{
  position: absolute;
  bottom: 13%;
  right: 5%;
}
</style>
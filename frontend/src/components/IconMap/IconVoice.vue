<template>
  <div>
    <span style='font-size:32px;'>
      <div @click='voiceOnOff'>
        <q-icon id="voice-color" v-if="voice" class='voice' name="mdi-account-tie-voice"></q-icon>
        <q-icon id="voice-color" v-else class='voice-off' name="mdi-account-tie-voice-off"></q-icon>
      </div>
    </span>
    <!--클림트-->
    <audio data-key="klimt1" src="@/assets/audio/klimt/klimt1.mp3"></audio>
    <audio data-key="klimt2" src="@/assets/audio/klimt/klimt2.mp3"></audio>
    <audio data-key="klimt3" src="@/assets/audio/klimt/klimt3.mp3"></audio>
    <audio data-key="klimt4" src="@/assets/audio/klimt/klimt4.mp3"></audio>
    <!--monet-->
    <audio data-key="monet1" src="@/assets/audio/monet/monet1.mp3"></audio>
    <audio data-key="monet2" src="@/assets/audio/monet/monet2.mp3"></audio>
    <audio data-key="monet3" src="@/assets/audio/monet/monet3.mp3"></audio>
    <audio data-key="monet4" src="@/assets/audio/monet/monet4.mp3"></audio>
    <audio data-key="monet5" src="@/assets/audio/monet/monet5.mp3"></audio>
    <!--cheon-->
    <audio data-key="cheon1" src="@/assets/audio/cheon/cheon1.mp3"></audio>
    <audio data-key="cheon2" src="@/assets/audio/cheon/cheon2.mp3"></audio>
    <audio data-key="cheon3" src="@/assets/audio/cheon/cheon3.mp3"></audio>
    <audio data-key="cheon4" src="@/assets/audio/cheon/cheon4.mp3"></audio>
    <audio data-key="cheon5" src="@/assets/audio/cheon/cheon5.mp3"></audio>
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
      voice: false,
      audio:null,
    }
  },
  computed:{
    page(){
      return this.$store.state.page.page
    }
  },
  watch:{
    'page':function(){
      this.voice=false
      if(this.audio!==null){
        this.audio.pause();
        this.audio.currentTime = 0;
      }
    }
  },
  mounted() {
    if(this.voiceColor){
      document.querySelector('#voice-color').style.color=this.voiceColor
    }
  },
  methods: {
    voiceOnOff(){
      
      // 음성 시작 함수
      function playSound(audio) {
        if(!audio) return;
        audio.currentTime = 0; 
        setTimeout(function(){
          audio.play()
            .then(function(){
            }).catch((err)=>{
              console.log(err)
            })
        },300)
      }

      // 어떤 안내를 내보낼 지 체크하는 곳
      var audio
      const routeName = this.$route.name
      if(/Start/.exec(routeName)){
        // 작가소개
        if(routeName==='StartKlimt'){
          audio = document.querySelector("audio[data-key=klimt1]")
        }else if(routeName==='StartMonet'){
          audio = document.querySelector("audio[data-key=monet1]")
        }else{
          audio = document.querySelector("audio[data-key=cheon1]")
        }
      }else if(/s$/.exec(routeName)){

        // 쩌리페이지
        if(routeName==='Klimts'){
          if(this.page===1){
            return;
          }else if(this.page===2){
            audio = document.querySelector("audio[data-key=klimt3]")
          }else if(this.page===3){
            audio = document.querySelector("audio[data-key=klimt4]")
          }else{
            return;
          }
        }else if(routeName==='Monets'){
          if(this.page===1){
            audio = document.querySelector("audio[data-key=monet2]")
          }else if(this.page===2){
            audio = document.querySelector("audio[data-key=monet3]")
          }else if(this.page===3){
            audio = document.querySelector("audio[data-key=monet4]")
          }else{
            audio = document.querySelector("audio[data-key=monet5]")
          }
        }else{
          if(this.page===1){
            audio = document.querySelector("audio[data-key=cheon5]")
          }else if(this.page===2){
            audio = document.querySelector("audio[data-key=cheon2]")
          }else if(this.page===3){
            audio = document.querySelector("audio[data-key=cheon3]")
          }else{
            audio = document.querySelector("audio[data-key=cheon4]")
          }
        }
      }else{

        //인터렉티브
        if(routeName==='Klimt'){
          audio = document.querySelector("audio[data-key=klimt2]")
        }else if(routeName==='Monet'){
          return;
        }else{
          return;
        }
      }
      this.audio = audio

      // 실제 버튼 동작
      if(this.voice===true){
        audio.pause();
        audio.currentTime = 0;
        this.voice = false;
      } else {
        playSound(audio)
        this.voice = true;
      }
    }
  }

}
</script>

<style scoped>
.voice{
  position: absolute; 
  z-index:100;
  position: absolute;
  bottom: 7%;
  right: 4.5%;
  padding:15px;
  color: rgba(0,0,0,0.5);
  background: rgba(0,0,0, 0.1);
  border-radius: 50%;
}
.voice:hover{
  color: rgba(0,0,0,0.8);
  background: rgba(0,0,0, 0.2);
  font-size:42px;
  cursor:pointer;
}
.voice-off:hover{
  color: rgba(0,0,0,0.8);
  background: rgba(0,0,0, 0.2);
  cursor: pointer;
}
.voice-off{
  z-index: 100;
  position: absolute;
  bottom: 7%;
  right: 4.5%;
  padding:15px;
  color: rgba(0,0,0,0.5);
  background: rgba(0,0,0, 0.1);
  border-radius: 50%;
}
</style>
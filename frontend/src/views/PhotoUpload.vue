<template>
  <div class="main">
      <IconMap/>
      <div style="min-height:30px"></div>
      <header v-if="nowRoute==='MonetPhoto'">Claude Monet</header>
      <header v-else-if="nowRoute==='KlimtPhoto'">Klimt</header>
      <header v-else>cheon</header>
      <section>
        <div class="avatar-upload">
          <div class="avatar-preview">
            <div id="imagePreview">
            </div>
          </div>
          <div class="avatar-edit">
            <input type='file' id="imageUpload" accept=".png, .jpg, .jpeg"/>
            <label for="imageUpload" @click='getSession'>
              <span class='uldbutton' style="font-size:30px">
                <q-icon name="mdi-upload"></q-icon>
                <div style="font-size:13px;">Upload Picture</div>  
              </span>
            </label>
          </div>
        </div>
      </section>
      <footer>
        <div>
          <div class="content text-center">
            <div v-if="nowRoute==='MonetPhoto'">아름다운 색을 가진 사진을 올려주세요</div>
            <div v-else-if="nowRoute==='KlimtPhoto'">클림트는 클림트야</div>
            <div v-else>천경자는 천경자야</div>
          </div>
          <div class="please-upload text-center">
            Please Upload a picture
          </div>
        </div>
        <q-btn flat target="_blank" id="skipbtn" @click="urlUpload">
          <span style='font-size:3rem;'>
            <q-icon name="mdi-chevron-double-right"></q-icon>
          </span>
        </q-btn>
      </footer>
      
  </div>
</template>

<script>
import $ from 'jquery'
import { fileUpload } from "@/api/fileUpload.js"

export default {
    name:'PhotoUpload',
    components: {
      IconMap: () => import('@/components/IconMap/IconMap')
    },
    data(){
      return {
        uploadFile:"",
        imgUrl:"",
        imgUrl_:"",
        tempUrl:''
      }
    },
    computed:{
      nowRoute() {
        return this.$route.name
      }
    },
    methods:{
      goToNext() {
        let nextRoute

        if (this.nowRoute==='MonetPhoto'){
          nextRoute = 'mone';
        }else if(this.nowRoute==='KlimtPhoto') {
          nextRoute = 'Klimt';
        }else {
          nextRoute = 'Cheon';
        }
        this.$router.push({path:nextRoute})
      },
      getSession(){
        this.$store.dispatch('getsession/getSession')
      },
      urlUpload(){
        if (this.uploadFile==="") {
          alert("특별전시회 이용에 제한이 됩니다.");
          this.goToNext()
        }else{
          let artist
          if (this.nowRoute==='MonetPhoto'){
            artist = 1;
          }else if(this.nowRoute==='KlimtPhoto') {
            artist =2 ;
          }else {
            artist = 3;
          }
          const formData = new FormData();
          formData.append("image", this.uploadFile);
          fileUpload(artist,formData)
            .then((res)=>{
              console.log(res.data)
              this.imgUrl_ = res.data;
              console.log('여기여기')
            })
            .catch((err)=>{
              console.log(err)
            })
          this.goToNext()
        }
      }
    },
    mounted(){
      let temp = this;
      function readURL(input) {
        if (input.files && input.files[0]) {
          var reader = new FileReader();
          reader.onload = function(e) {
            $('#imagePreview').css('background-image', 'url('+e.target.result +')');
            $('#imagePreview').css('height', '500px');
            $('#imagePreview').hide();
            $('#imagePreview').fadeIn(650);
          }
            reader.readAsDataURL(input.files[0]);
        }
    }
      $("#imageUpload").change(function() {
        readURL(this);
        temp.uploadFile = this.files[0];
        // console.log(this.uploadFile)
      });
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif:ital@1&display=swap');
@font-face {
    font-family: 'IBMPlexSansKR-Regular';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_20-07@1.0/IBMPlexSansKR-Regular.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}
@import url('https://fonts.googleapis.com/css2?family=Prata&display=swap');




.main {
  height: 100vh;
  background: #ECE5E1;
  font-family: "Open Sans", sans-serif;
}
header {
  border-top: solid 2px #424242;
  border-bottom: solid 2px #424242;
  min-height: 70px;
  padding: 1rem 10rem;
  font-family: 'Noto Serif', serif;
  font-size: 1.5rem;
  font-weight: 500;
}
h1 {
  font-size: 20px;
  text-align: center;
  margin: 20px 0 20px;
}
h1 small {
  display: block;
  font-size: 15px;
  padding-top: 8px;
  color: gray;
}
.avatar-upload {
  /* position: relative; */
  display:flex;
  justify-content: center;
  margin: 60px auto;
}
.avatar-upload .avatar-edit {
  position: absolute;
  display:block;
  /* top: 30%;
  right: 10%; */
  transform: translate(500%,200%);
}
.avatar-upload .avatar-edit input {
  display: none;
}
.avatar-upload .avatar-edit input + label {

  display: flex;
  justify-content: center;
  align-items: center;
  top: 50%;
  width: 100px;
  height: 100px;
  padding-left: 10%;
  border-radius: 100%;
  background: #ffffff;
  border: 1px solid transparent;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.12);
  cursor: pointer;
  font-weight: normal;
  transition: all 0.2s ease-in-out;
}
.uldbutton {
  display: flex;
}
.avatar-upload .avatar-edit input + label:hover {
  background: #f1f1f1;
  border-color: #d6d6d6;
}
.avatar-upload .avatar-edit input + label:after {
  color: #757575;
  position: absolute;
  top: 10px;
  left: 0;
  right: 0;
  text-align: center;
  margin: auto;
}
.avatar-upload .avatar-preview {
  min-width: 850px;
  min-height: 530px;
  
  /* position: relative;
  left: 50%;
  top: 50%; */
  /* transform: translateX(-50%) translateY(20%); */
  /* border-radius: 100%; */
  border: 13px solid #f8f8f8;
  box-shadow: 0px 7px 13px 0px rgba(0, 0, 0, 0.1);
}
.avatar-upload .avatar-preview > div {
  width: 100%;
  /* height: 100%; */
  /* border-radius: 100%; */
  background-size:cover;
  background-repeat: no-repeat;
  background-position: center;
}
footer{
  display: flex;
  justify-content: center;
}
footer>div:nth-child(1){
  width:800px;
}
footer .content {
  font-family: 'IBMPlexSansKR-Regular';
  font-size:1.1rem;
}
footer .please-upload {
  font-family: 'Prata', serif;
  font-size: 3.2rem;
  font-weight: 500;
  margin: 10px 0;
}
#skipbtn {
    position: absolute;
    transform: translate(500%,0);
    /* bottom: 20%;
    right: 10%; */
}

</style>
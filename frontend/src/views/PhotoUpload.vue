<template>
  <div class="main">
    <IconMap/>
    <div style="min-height:30px"></div>
    <div class="container">
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
            <div v-else>증명사진 같은 사진을 올려주세요</div>
          </div>
          <div class="please-upload text-center">
            Please Upload a picture
          </div>
        </div>
        <div @click="showNotif" class="nextbtn">
          <div class="diamond-container">
          <div class="diamond left"></div>
          <div class="diamond right"></div>
          <div class="arrow"></div>
          </div>
        </div>
      </footer>
    </div>
      
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
      showNotif () {
        if(this.uploadFile!==""){
          this.urlUpload()
          return
        }
        this.$q.notify({
        message: '특별전시회 이용에  <strong style="color: red">제한</strong>이 됩니다.',
        html: true,
        type: 'warning',
        position:'center',
        actions: [
          { label: 'OK', color: 'primary', handler: () => { this.urlUpload() } }
        ]
      })
      },
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
.container{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: calc(100vh - 150px);
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
  min-width: 40%;
  min-height: 400px;
  
  /* position: relative;
  left: 50%;
  top: 50%; */
  /* transform: translateX(-50%) translateY(20%); */
  /* border-radius: 100%; */
  border: 13px solid #f8f8f8;
  box-shadow: 0px 7px 13px 0px rgba(0, 0, 0, 0.1);
}
.avatar-upload .avatar-preview:hover .avatar-edit input + label {
  background: #f1f1f1;
  border-color: #d6d6d6;
}
.avatar-upload .avatar-preview > div {
  width: 100%;
  /* height: 100%; */
  /* border-radius: 100%; */
  background-size:contain;
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

<style lang="scss" scoped>
// DIMENSIONS
$width: 150px; // Button With
$outerDiamondHeight: $width / 3; //Button Height
$outerDiamondWidth: $width / 2;
$innerDiamondHeight: $outerDiamondHeight - 1;
$innerDiamondWidth: $outerDiamondWidth - 1;
$arrowSize: $width / 6;

// COLORS
$borderColor: #333;
$backgroundColor: white;

//TRANSITION
$transition: all 0.25s ease;

.diamond-container {
  z-index:1000;
  width: $width;
  position: absolute;
  bottom:10%; right: 10%;
  transform: translate(-10%);
  cursor: pointer;
  
  // CLEARFIX
  &:after {
    content:'';
    display: table;
    height: 0;
    clear: both;
  }
  
  // DIAMOND BUTTON - LEFT&RIGHT
  .diamond {
    position: relative;
    width: $outerDiamondWidth;
    height: $outerDiamondHeight*2;
    float: left;
    overflow: hidden;

    &:after, &:before {
      border: solid transparent;
      content: ' ';
      position: absolute;
      width: 0%; height: 0%;
      transition: $transition;
    }

    &:after {
      border-width: $innerDiamondHeight 0 $innerDiamondHeight $innerDiamondWidth;
      border-left-color: $backgroundColor;
      top: 1px; left: -1px;
    }
    &:before {
      border-width: $outerDiamondHeight 0 $outerDiamondHeight $outerDiamondWidth;
      border-left-color: $borderColor;
    }

    &.left {
      &:after {
        border-width: $innerDiamondHeight $innerDiamondWidth $innerDiamondHeight 0;
        border-left-color: transparent;
        border-right-color: $backgroundColor;
        left: 2px;
      }
      &:before {
        border-width: $outerDiamondHeight $outerDiamondWidth $outerDiamondHeight 0;
        border-left-color: transparent;
        border-right-color: $borderColor;
      } 
    }
  }
  
  // ARROW 
  .arrow {
    width: $arrowSize; height: $arrowSize;
    border: 1px solid $borderColor;
    border-left: none;
    border-bottom: none;  
    position: absolute;
    top:50%; left: 52%;
    transform: translate(-50%, -50%) rotate(45deg);
    transition: $transition;
    &:after {
      content: "";
      width: 160%; border-top: 1px solid $borderColor;
      position: absolute;
      top: 0; right: 0;
      transform: rotate(-45deg);
      transform-origin: top right;
      transition: inherit;
    }
  }
  
  // HOVER EFFECT
  &:hover {

    .diamond {
      border: #ccc;
      &:after { border-left-color: $borderColor; }
      &.left:after {  border-right-color: $borderColor; }
    }
    .arrow {
      border-top: 1px solid $backgroundColor;
      border-right: 1px solid $backgroundColor;
      transform: translate(-50%, -50%) rotate(405deg);
      &:after {
        border-top: 1px solid $backgroundColor;
      }
    }
  }
  
}
</style>
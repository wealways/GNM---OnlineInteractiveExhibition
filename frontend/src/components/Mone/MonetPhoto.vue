<template>
  <div>
      <div>아름다운 색을 가진 사진을 올려주세요</div>
      <div class="avatar-upload">
        <div class="avatar-edit">
            <input type='file' id="imageUpload" accept=".png, .jpg, .jpeg"/>
            <label for="imageUpload" @click='getSession'>
              <span style="font-size:20px">
                <q-icon name="mdi-upload"></q-icon>  
              </span>
            </label>
        </div>
        <div class="avatar-preview">
            <div id="imagePreview">
            </div>
        </div>
      </div>
      <q-btn :to='"/mone"' target="_blank" id="skipbtn" @click="urlUpload">NEXT</q-btn>
  </div>
</template>

<script>
import $ from 'jquery'
import { fileUpload } from "@/api/fileUpload.js";

export default {
    name:'MonetPhoto',
    data(){
      return {
        uploadFile:"",
        imgUrl:"",
        imgUrl_:""
      }
    },
    methods:{
      getSession(){
        this.$store.dispatch('getsession/getSession')
      },
      urlUpload(){
        if (this.uploadFile==="") {
          alert("이미지를 업로드 해주세요");
          return false;
        } else {
          const artist = 1;
          const formData = new FormData();
          console.log(this.uploadFile)
          formData.append("image", this.uploadFile);
          console.log(formData)
          fileUpload(
            artist,
            formData,
            (response)=>{
              if (response.data === null) return;
              console.log(response.data)
              this.imgUrl_ = response.data;
            },
            (error) => console.log(error)
          )
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
#skipbtn {
    position: absolute;
    bottom: 20%;
    right: 10%;
}
body {
  background: whitesmoke;
  font-family: "Open Sans", sans-serif;
}
.container {
  max-width: 960px;
  margin: 30px auto;
  padding: 20px;
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
  position: relative;
  max-width: 205px;
  margin: 50px auto;
}
.avatar-upload .avatar-edit {
  position: absolute;
  right: 12px;
  z-index: 1;
  top: 10px;
}
.avatar-upload .avatar-edit input {
  display: none;
}
.avatar-upload .avatar-edit input + label {
  display: inline-block;
  width: 34px;
  height: 34px;
  margin-bottom: 0;
  border-radius: 100%;
  background: #ffffff;
  border: 1px solid transparent;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.12);
  cursor: pointer;
  font-weight: normal;
  transition: all 0.2s ease-in-out;
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
  width: 192px;
  height: 192px;
  position: relative;
  border-radius: 100%;
  border: 6px solid #f8f8f8;
  box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.1);
}
.avatar-upload .avatar-preview > div {
  width: 100%;
  height: 100%;
  border-radius: 100%;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
}

</style>
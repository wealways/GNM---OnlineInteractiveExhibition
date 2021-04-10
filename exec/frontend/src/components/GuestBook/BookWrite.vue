<template>
  <div>
    <button @click="changeFlag(true)" class="custom-btn btn-8 write-sz write"><span class="button-title">WRITE</span></button>
    <q-dialog v-model="flag" persistent>
      <q-card style="min-width: 680px">
        <q-form
          @submit="onSubmit"
          class="q-gutter-md"
        >
          <div class="form-top">
            <q-card-section class="form-header">
              <div v-if="!onModify" class="text-h6" style="margin-top:50px;"></div>
              <div v-if="onModify" class="text-h6">수정</div>
            </q-card-section>
          </div>
          <div class="form-body">
            <div class="form-name-password">
              <div class="q-mr-md q-ml-md q-mb-xs">
                <q-input
                  :input-class="{'form-nickname':true}"
                  no-error-icon
                  v-model="nickname" 
                  label="이름" 
                  color="teal-5" 
                  class="q-pt-none"
                  :rules="[ val => val && val.length > 1 && val.length <10 || '2~9글자를 입력해주세요']"
                >
                </q-input>
              </div>
              <div v-if="!onModify" class="q-mr-md q-ml-md q-mb-xs">
                <q-input
                  no-error-icon
                  v-model="password" 
                  type="password" 
                  label="임시비밀번호" 
                  color="teal-5" 
                  class="q-pt-none"
                  :rules="[ val => val && val.length > 4 && val.length<10 || '5~9자리 비빌번호']"
                >
                </q-input>
              </div>
              <div v-if="onModify" class="q-mr-md q-ml-md q-mb-xs">
                <q-input
                  v-model="password"
                  no-error-icon
                  type="password" 
                  label="기존 비밀번호 재입력" 
                  class="q-pt-none"
                  :rules="[ val => val && val.length > 4 && val.length<10 || '5~9자리 비빌번호']"
                >
                </q-input>
              </div>
            </div>
            <div class="q-mr-md q-ml-md q-mb-xs">
              <q-input
                filled
                color="teal-10"
                bg-color="grey-1"
                v-model="article"
                dense
                no-error-icon
                type="textarea"
                label="방명록"
                style="min-heigth: 400px"
                :rules="[ val => val && val.length > 0 && val.length<100 || '100자 이내']"
              >
              </q-input>
            </div>
          </div>
          <div v-if="onModify" class="form-image ">
            <div class="row q-mr-md q-ml-md q-mb-xs justify-center">
              <img class="col-5" :src="image" alt="">
            </div>
            <p class="q-mt-sm q-mr-md q-ml-md q-mb-xs" style="color:#000; text-align:center;">이미지를 변경할 수 없습니다.</p>
          </div>
          <div v-if="!onModify" class="form-image">
            <div class="q-mr-md q-ml-md q-mb-xs">
              이미지 선택란
            </div>
             <div class="row q-mr-md q-ml-md q-mb-xs">
              <q-radio class="col-3 q-pl-sm  q-mr-auto q-ml-auto" v-for="(image,idx) in selectableImages" :key="idx" color="teal-5" v-model="selectImgIdx" :val="idx" :label="artistName[idx]"/>
            </div>
            <div class="row q-mr-md q-ml-md q-mb-xs">
              <img
                class="col-3 q-mr-auto q-ml-auto"
                v-for="(image,idx) in selectableImages"
                :key="idx"
                :src="image"
                @click="selectImgIdx = String(idx)"
                style="object-fit: cover;"
              >
            </div>            
          </div>
          <q-card-actions align="right" class="text-primary">
            <q-btn type="submit" label="Submit" class="custom-btn submit-btn sub-can-sz"/>
            <q-btn @click="onReset" flat label="Cancel" class="custom-btn cancel-btn sub-can-sz"/>
          </q-card-actions>
        </q-form>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name:'BookWrite',
  data() {
    return {
      nickname:null,
      article:null,
      password: null,
      image:null,
      selectImgIdx:"0",
      artistName:['Monet','Klimt','천경자']
    }
  },
  computed:{
    ...mapGetters('guestbook',[
      'modal_flag',
      'on_modfiy',
    ]),
    flag:{
      get(){
        return this.modal_flag
      },
      set(newValue){ 
        return this.$store.dispatch('guestbook/changeFlag',newValue)
      }
    },
    onModify:{
      get(){
        return this.on_modfiy
      },
      set(newValue){
        return this.$store.dispatch('guestbook/changeOn',newValue)
      }
    },
    userArticle(){
      return this.$store.state.guestbook.user_article
    },
    selectableImages(){
      return this.$store.state.guestbook.selectable_images
    }

  },
  watch: {
    onModify:'modifyFetch'
  },
  created(){
    // this.fetchImg()
  },
  methods: {
    bgImg(img){
      const data = `{backgroundImage : url(${img})};width:100px`
      return data
    },
    modifyFetch(){
      if(this.onModify){
        this.nickname = this.userArticle.user_nickname
        this.article = this.userArticle.guestbook_comment
        this.image = this.userArticle.guestbook_image
      }
    },
    changeFlag(newFlag){
      this.flag = newFlag
      // 세션에 매핑되는 이미지 가져오기 (미완성)
      // this.$store.dispatch('guestbook/getImages',false)
    },
    onSubmit () {
      let data = {
        user_nickname: this.nickname,
        guestbook_comment : this.article,
        guestbook_image : this.selectableImages[parseInt(this.selectImgIdx)],
        guestbook_password : this.password
      }
      if(this.onModify){
        data.guestbook_image=this.image
        this.$store.dispatch('guestbook/modifyArticle',{article_id:this.userArticle.id,data})
      }else{
        this.$store.dispatch('guestbook/createArticle',data)
      }
      this.onReset()
    },
    onReset () {
      this.flag = false
      if(this.onModify){
        this.onModify = false
      }
      this.nickname = null
      this.article = null
      this.password = null
    },
  }
}
</script>

<style scoped>

.button-title {
  text-align:center;
  letter-spacing: 3px;
  font-weight: bold;
}


/* button sizes */

.write-sz {
  width: 130px;
  height: 40px;
}

.sub-can-sz {
  width : 100px;
  height :40px;
  margin : 0 10px;
}


.custom-btn {
  border-radius: 5px;
  padding: 10px 25px;
  font-weight: 500;
  background: transparent;
  cursor: pointer;
  position: relative;
  display: inline-block;
   box-shadow:inset 2px 2px 2px 0px rgba(255,255,255,.5),
   7px 7px 20px 0px rgba(0,0,0,.1),
   4px 4px 5px 0px  rgba(0,0,0,.1);
  outline: none;
}
/*  colors */
/*  write button */
.custom-btn:hover{
  transition: all 0.5s ease;
  box-shadow: 2px 2px 2px 0px rgba(255,255,255,.3),
            inset 7px 7px 20px 0px rgba(0,0,0,.1),
            inset 4px 4px 5px 0px  rgba(0,0,0,.1);
}


.btn-8 {
  color:#2A433B;
  background-color: #FCF9F2;
  line-height: 42px;
  padding: 0;
  border: none;
}
.btn-8 span {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
}
.btn-8:before,
.btn-8:after {
  position: absolute;
  content: "";
  right: 0;
  bottom: 0;
  transition: all 0.3s ease;
}
.btn-8:before{
   height: 0%;
   width: 2px;
}
.btn-8:after {
  width: 0%;
  height: 2px;
}
.btn-8:hover:before {
  height: 100%;
}
.btn-8:hover:after {
  width: 100%;
}
.btn-8:hover{
  background: transparent;
}

.btn-8 span:before,
.btn-8 span:after {
  position: absolute;
  content: "";
  left: 0;
  top: 0;
  transition: all 0.3s ease;
}
.btn-8 span:before {
  width: 2px;
  height: 0%;
}
.btn-8 span:after {
  height: 2px;
  width: 0%;
}
.btn-8 span:hover:before {
  height: 100%;
}
.btn-8 span:hover:after {
  width: 100%;
}



/* submit button color */


.submit-btn {
  color: #fff;
  background-color: #2a433b;
  background-image: #2a433b;
  line-height: 42px;
  padding: 0;
  border: none;
}
.submit-btn span {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
}
.submit-btn:before,
.submit-btn:after {
  position: absolute;
  content: "";
  right: 0;
  bottom: 0;
  transition: all 0.3s ease;
}
.submit-btn:before{
   height: 0%;
   width: 2px;
}
.submit-btn:after {
  width: 0%;
  height: 2px;
}
.submit-btn:hover:before {
  height: 100%;
}
.submit-btn:hover:after {
  width: 100%;
}
.submit-btn:hover{
  /* 호버 바탕색 */
  background:#A0D6C8;
}
.submit-btn span:hover{
  /* 버튼글씨 색깔 */
  color: #2a433b;
}
.submit-btn span:before,
.submit-btn span:after {
  position: absolute;
  content: "";
  left: 0;
  top: 0;
  transition: all 0.3s ease;
}
.submit-btn span:before {
  width: 2px;
  height: 0%;
}
.submit-btn span:after {
  height: 2px;
  width: 0%;
}
.submit-btn span:hover:before {
  height: 100%;
}
.submit-btn span:hover:after {
  width: 100%;
}



/* cancel button  */

.cancel-btn {
  color: #2a433b;
  background-color: #E4E8E7;
  background-image:  #E4E8E7;
  color: #2a433b;
  line-height: 42px;
  padding: 0;
  border: none;
}
.cancel-btn span {
  position: relative;
  display: block;
  width: 100%;
  height: 100%;
}
.cancel-btn:before,
.cancel-btn:after {
  position: absolute;
  content: "";
  right: 0;
  bottom: 0;
  transition: all 0.3s ease;
}
.cancel-btn:before{
   height: 0%;
   width: 2px;
}
.cancel-btn:after {
  width: 0%;
  height: 2px;
}
.cancel-btn:hover:before {
  height: 100%;
}
.cancel-btn:hover:after {
  width: 100%;
}
.cancel-btn:hover{
  background: #6b968a;
}
.cancel-btn span:hover{
  color: #2a433b;
}
.cancel-btn span:before,
.cancel-btn span:after {
  position: absolute;
  content: "";
  left: 0;
  top: 0;
  transition: all 0.3s ease;
}
.cancel-btn span:before {
  width: 2px;
  height: 0%;
}
.cancel-btn span:after {
  height: 2px;
  width: 0%;
}
.cancel-btn span:hover:before {
  height: 100%;
}
.cancel-btn span:hover:after {
  width: 100%;
}

form{
  padding:30px 60px;
}
.form-header{
  padding-top:0;
  padding-bottom: 0;
}
.form-body{
  margin-top: 0;
}
.form-body > .form-name-password {
  display: flex;
}
.form-body > .form-name-password>div:nth-child(1){
  width: 50%;
}
.form-body > .form-name-password>div:nth-child(2){
  width: 50%;
}
.form-image{
  margin-top:6px;
}
</style>
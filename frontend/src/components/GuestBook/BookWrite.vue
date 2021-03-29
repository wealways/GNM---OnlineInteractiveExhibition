<template>
  <div>
    <q-btn label="방명록 작성" color="primary" @click="changeFlag(true)" />
    <q-dialog v-model="flag" persistent>
      <q-card style="min-width: 680px">
        <q-form
          @submit="onSubmit"
          class="q-gutter-md"
        >
          <div class="form-top">
            <q-card-section class="form-header">
              <div v-if="!onModify" class="text-h6">작성</div>
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
          <div v-if="onModify" class="form-image">
            <div class="row q-mr-md q-ml-md q-mb-xs">
              <img class="col-5" :src="image" alt="">
            </div>
            <p class="q-mt-sm q-mr-md q-ml-md q-mb-xs" style="color:#000">이미지를 변경할 수 없습니다.</p>
          </div>
          <div v-if="!onModify" class="form-image">
            <div class="q-mr-md q-ml-md q-mb-xs">
              이미지 선택란
            </div>
            <div class="row q-mr-md q-ml-md q-mb-xs">
              <q-radio class="col-3 q-ml-md " v-model="selectImgIdx" val="0" label="모네" />
              <q-radio class="col-3 q-ml-md" v-model="selectImgIdx" val="1" label="천경자" />
              <q-radio class="col-3 q-ml-md" v-model="selectImgIdx" val="2" label="클림트" />
            </div>
            <div class="row q-mr-md q-ml-md q-mb-xs">
              <img
                class="col-3 q-mr-md"
                v-for="(image,idx) in selectableImages"
                :key="idx"
                :src="image"
                @click="selectImgIdx = String(idx)"
              >
            </div>
            <!-- </div> -->
            
          </div>
          <q-card-actions align="right" class="text-primary">
            <q-btn type="submit" color="primary" label="Submit"/>
            <q-btn @click="onReset" flat label="Cancel"/>
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
      selectImgIdx:"0"
    }
  },
  computed:{
    ...mapGetters('guestbook',[
      'modal_flag',
      'on_modfiy',
      // 'user_article'
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
      console.log(img)
      const data = `{backgroundImage : url(${img})};width:100px`
      return data
    },
    // srcImg(img){
    //   console.log(img)
    //   return `url(${require(img)})`
    // },
    modifyFetch(){
      if(this.onModify){
        this.nickname = this.userArticle.user_nickname
        this.article = this.userArticle.guestbook_comment
        this.image = this.userArticle.guestbook_image
        // this.password = this.userArticle.guestbook_password
      }
    },
    changeFlag(newFlag){
      this.flag = newFlag
      // 세션에 매핑되는 이미지 가져오기 (미완성)
      this.$store.dispatch('guestbook/getImages',false)
    },
    onSubmit () {
      let data = {
        user_nickname: this.nickname,
        guestbook_comment : this.article,
        guestbook_image : this.selectableImages[parseInt(this.selectImgIdx)],
        guestbook_password : this.password
      }
      if(this.onModify){
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

<style>
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
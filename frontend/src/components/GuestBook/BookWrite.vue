<template>
  <div>
    <q-btn label="방명록 작성" color="primary" @click="changeFlag(true)" />
    <div v-if="flag">여기</div>
    <q-dialog v-model="flag" persistent>
      <q-card style="min-width: 680px">
        <q-form
          @submit="onSubmit"
          class="q-gutter-md"
        >
          <q-card-section>
            <div v-if="!onModify" class="text-h6">작성</div>
            <div v-if="onModify" class="text-h6">수정</div>
          </q-card-section>
          <div class="form-top">
            <div class="q-mr-md q-ml-md q-mb-md">
              <q-input
               v-model="nickname" 
               label="이름 (2~9 자리)" 
               class="q-pt-none"
               :rules="[ val => val && val.length > 1 && val.length <10 || '2~9글자를 입력해주세요']"
              >
              </q-input>
            </div>
            <div v-if="!onModify" class="q-mr-md q-ml-md q-mb-md">
              <q-input
                v-model="password" 
                type="password" 
                label="임시비밀번호 (5~9 자리)" 
                class="q-pt-none"
                :rules="[ val => val && val.length > 4 && val.length<10 || '5~9자리 비빌번호']"
               >
              </q-input>
            </div>
            <div v-if="onModify" class="q-mr-md q-ml-md q-mb-md">
              <q-input
                v-model="password" 
                type="password" 
                label="기존 비밀번호 재입력 (5~9 자리)" 
                class="q-pt-none"
                :rules="[ val => val && val.length > 4 && val.length<10 || '5~9자리 비빌번호']"
               >
              </q-input>
            </div>
          </div>
          <div class="form-body">
            <div class="q-mr-md q-ml-md q-mb-md">
              <q-input
                v-model="article"
                type="textarea"
                label="방명록 (100자이내)"
                style="min-heigth: 400px"
                :rules="[ val => val && val.length > 0 && val.length<100 || '100자 이내']"
              >
              </q-input>
            </div>
          </div>
          <div class="form-image">
            <div class="q-mr-md q-ml-md q-mb-md">
              이미지 선택란
            </div>
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
      image:null
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
    }
  },
  watch: {
    onModify:'modifyFetch'
  },
  methods: {
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
    },
    onSubmit () {
      let data = {
        user_nickname: this.nickname,
        guestbook_comment : this.article,
        guestbook_image : this.image,
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

</style>
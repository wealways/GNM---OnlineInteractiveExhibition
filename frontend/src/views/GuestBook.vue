<template>
  <q-layout>
    <h1>방명록</h1>
    <q-btn label="방명록 작성" color="primary" @click="prompt = true" />
    <q-dialog v-model="prompt" persistent>
      <q-card style="min-width: 680px">
        <q-form
          @submit="onSubmit"
          @reset="onReset"
          class="q-gutter-md"
        >
          <q-card-section>
            <div class="text-h6">작성</div>
          </q-card-section>
          <div class="form-top">
            <div class="q-mr-md q-ml-md q-mb-md">
              <q-input
               v-model="nickname" 
               label="이름" 
               class="q-pt-none"
               :rules="[ val => val && val.length > 1 && val.length <10 || '2~9글자를 입력해주세요']"
              >
              </q-input>
            </div>
            <div class="q-mr-md q-ml-md q-mb-md">
              <q-input
               v-model="password" 
               type="password" 
               label="임시비밀번호" 
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
                label="후기"
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
            <q-btn type="submit" color="primary" label="Submit" v-close-popup />
            <q-btn type="reset" flat label="Cancel" v-close-popup />
          </q-card-actions>
        </q-form>
      </q-card>
    </q-dialog>
    <q-page-container>
      <q-page>
        <!-- page content -->
      </q-page>
  </q-page-container>
  </q-layout>
</template>

<script>
import * as articleApi from '@/api/v1/guestbook'

export default {
  name: 'GuestBook',
  data() {
    return {
      prompt: false,
      nickname:null,
      article:null,
      password: null,
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      articleApi.GetArticles()
      .then((res)=>{
        console.log(res)
      })
      .catch((err)=>
      console.log(err))
    },
    onSubmit () {
      const data = {
        "user_nickname": this.nickname,
        "guestbook_comment" : this.article,
        // guestbook_image : '',
      }

      articleApi.CreateArticle(data)
      .then((res)=>{
        console.log(res)
      })
      .catch((err)=>{
        console.log(err)
      })
      this.onReset()
    },
    onReset () {
      this.nickname = null
      this.article = null
      this.password = null
      this.accept = false
    }
  }
}
</script>

<style scoped>
.form-top{
  display: flex;
}
</style>
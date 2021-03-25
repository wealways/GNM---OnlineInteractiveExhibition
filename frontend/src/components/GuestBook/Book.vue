<template>
  <div>
    <div class="book book--border-line" @click="prompt = true">
      <q-card class="my-card">
        <q-img
          :src="article.guestbook_image"
          basic
          id="q-img__image"
        >
        </q-img>
      </q-card>
      <div class="card-description text-subtitle2 column justify-center">
        <strong class="text-center">{{article.guestbook_comment}}</strong>
        <span class="user-nickname text-caption text-right">
          by {{article.user_nickname}}
        </span>
      </div>
    </div>
    <q-dialog v-model="prompt">
        <div class="row" style="min-width: 940px;">
          <q-img
            :src="article.guestbook_image"
            basic
            class="col-8"
            :ratio="1"
          >
          </q-img>
          <div class="card-img-description col-4 p-3">
            <div class="card-img-header">
              <h2>CAT</h2>
            </div>
            <div class="card-img-body">
              <p>{{article.guestbook_comment}}</p>
              <p>by {{article.user_nickname}}</p>
            </div>
            <p>{{date}}</p>
            <div>
              <button @click="modifyBtn=true">수정</button>
              <q-dialog v-model="modifyBtn">
                <q-card style="min-width: 350px">
                  <q-card-section class="q-pt-none">
                    <q-input
                    v-model="temppassword"
                    type="password"  
                    label="비밀번호 확인" 
                    class="q-pt-none"
                    :rules="[ val => val && val.length > 4 && val.length<10 || '5~9자리 비빌번호']"
                    >
                    </q-input>
                  </q-card-section>
                  <div class="row justify-end q-mb-xs">
                    <q-btn @click="modifyArticle" label="수정" color="warning" v-close-popup />
                    <q-btn @click="onReset" flat label="취소" v-close-popup />
                  </div>
                </q-card>
              </q-dialog>
              <button @click="deleteBtn = true">삭제</button>
              <q-dialog v-model="deleteBtn">
                <q-card style="min-width: 350px">
                  <q-card-section class="q-pt-none">
                    <q-input
                    v-model="temppassword"
                    type="password"  
                    label="비밀번호" 
                    class="q-pt-none"
                    :rules="[ val => val && val.length > 4 && val.length<10 || '5~9자리 비빌번호']"
                    >
                    </q-input>
                  </q-card-section>
                  <div class="row justify-end q-mb-xs">
                    <q-btn @click="deleteArticle" label="삭제" color="negative" v-close-popup />
                    <q-btn @click="onReset" flat label="취소" v-close-popup />
                  </div>
                </q-card>
              </q-dialog>
            </div>
          </div>
        </div>
      </q-dialog>
  </div>
</template>

<script>
import timeForToday from '@/plugins/timeForToday'

export default {
  name:'Book',
  data() {
    return {
      prompt:false,
      deleteBtn:false,
      modifyBtn:false,
      temppassword:''
    }
  },
  props:{
    article:Object
  },
  created() {
    
  },
  computed: {
    date() {
      return timeForToday(this.article.created_date)
    },
    dialogPrompt() {
      return this.$store.guestbook.dialogPrompt
    }
  },
  methods: {
    deleteArticle() {
      const params = {
        id:this.article.id,
        password:String(this.temppassword)
      }
      this.$store.dispatch('guestbook/deleteArticle',params)
      this.prompt=false
      this.deleteBtn=false
      this.temppassword=''
    },
    modifyArticle(){
      const data = {
        id:this.article.id,
        guestbook_password:this.temppassword
      }
      this.$store.dispatch('guestbook/confirmPassword',data)
      this.prompt=false
      this.modifyBtn=false
      this.temppassword=''
    },
    onReset() {
      this.temppassword=''
    },
  }
}
</script>

<style>
p{
  position:initial !important;
}
.book{
  font-family: sans-serif;
  margin-bottom: 0.5rem;
  /* transition: transform 0.5s ease; */
  border: solid 1px #fff;
  position: relative;
  display: inline-block;
  cursor: pointer;
  width: 100%;
}
.my-card{
  margin: 0.5rem;
}

.book:after {
  content: '';
  display: block;
  position: absolute;
}
.book:before {
  content: '';
  display: block;
  position: absolute;
}
.book--border-line {
  background: none;
  border: 0;
  box-sizing: border-box;
  box-shadow: inset 0 0 0 2px transparent;
  padding: 8px;
}
.book--border-line:after,
.book--border-line:before {
  box-sizing: border-box;
  border: 1px solid transparent;
  width: 0;
  height: 0;
}
.book--border-line:after {
  top: 0;
  left: 0;
  -webkit-transition: border-color 0s ease-in 0.8s, width 0.2s ease-in 0.6s, height 0.2s ease-in 0.4s;
  transition: border-color 0s ease-in 0.8s, width 0.2s ease-in 0.6s, height 0.2s ease-in 0.4s;
}
.book--border-line:before {
  bottom: 0;
  right: 0;
  -webkit-transition: border-color 0s ease-in 0.4s, width 0.2s ease-in 0.2s, height 0.2s ease-in;
  transition: border-color 0s ease-in 0.4s, width 0.2s ease-in 0.2s, height 0.2s ease-in;
}
.book--border-line:hover:after,
.book--border-line:hover:before {
  width: 100%;
  height: 100%;
}
.book--border-line:hover:after {
  border-top-color: #e64040;
  border-right-color: #e64040;
  -webkit-transition: width 0.2s ease-out, height 0.2s ease-out 0.2s;
  transition: width 0.2s ease-out, height 0.2s ease-out 0.2s;
}
.book--border-line:hover:before {
  border-bottom-color: #e64040;
  border-left-color: #e64040;
  -webkit-transition: border-color 0s ease-out 0.4s, width 0.2s ease-out 0.4s, height 0.2s ease-out 0.6s;
  transition: border-color 0s ease-out 0.4s, width 0.2s ease-out 0.4s, height 0.2s ease-out 0.6s;
}

.card-description{
  width: 100%;
  margin-top:25px;
  margin-bottom: 25px;
  
}
#q-img__image>div:nth-child(2)::after, #q-img__image>div:nth-child(2)::after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: inherit;
  background-size: cover !important;
  transform-origin: center !important;
  transition: transform 0.4s ease-in !important;
}

.book--border-line:focus #q-img__image>div:nth-child(2)::after,.book--border-line:hover #q-img__image>div:nth-child(2):after {
  transform: scale(1.1) !important;
  
}


.card-img-description{
  background: #000;
  padding:2rem;
}
.card-img-description p{
  color: #fff;
}
.card-img-header{
  writing-mode: tb-rl;
  transform: rotate(-180deg);

}
.card-img-body{
  margin-top: 5rem;
  padding: 2rem;
}
.card-img-body> p:nth-child(1){
  font-size:1.5rem;
  word-break:break-all;
  min-height: 30%;
}
.card-img-body> p:nth-child(2){
  text-align: right;
  word-break:break-all;
}
</style>
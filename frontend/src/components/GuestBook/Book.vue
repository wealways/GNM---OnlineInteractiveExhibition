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
        <span class="user-nickname text-caption text-right">
          {{article.user_nickname}}
        </span>
      </div>
    </div>
    <q-dialog v-model="prompt" class='cardback'>
        <div class="row" style="min-width: 1080px;">
          <q-img
            :src="article.guestbook_image"
            basic
            class="col-8"
            style="max-height:800px"
          >
          </q-img>

          <div class="card-img-description col-4 column">
            <div class="card-img-header">
            </div>
            <div class="card-img-body col column justify-center ">
              <div class="" style="display:block; text-align:center;">{{article.guestbook_comment}}</div>
              <div class="column justify-end items-end" style="display:inline">
                <span style="margin-right: 5px;">by</span>
                <span>{{article.user_nickname}}</span>
              </div>
            </div>
            <div class="card-img-footer">
              <p style="color:rgba(63, 44, 3, 0.637); margin-bottom:10px;" class='writedate'>{{date}}</p>
              <q-fab padding="8px" text-color="white" icon="keyboard_arrow_left" direction="left" style="width:15%; margin-bottom:10px;" class="more-btn">
                <q-fab-action padding="8px" class="upd-btn" @click="modifyBtn=true" icon="mdi-square-edit-outline" label-position="bottom" label-style="font-size:12px;"/>
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
                      <q-btn @click="modifyArticle" label="수정" color="teal-9" v-close-popup />
                      <q-btn @click="onReset" flat label="취소" v-close-popup />
                    </div>
                  </q-card>
                </q-dialog>
                <q-fab-action padding="8px"  class="del-btn" @click="deleteBtn = true" icon="mdi-delete-outline" label-position="bottom" label-style="font-size:12px;color:#fff;"/>
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
                      <q-btn @click="deleteArticle" label="삭제" color="teal-10" v-close-popup />
                      <q-btn @click="onReset" flat label="취소" v-close-popup/>

                    </div>
                  </q-card>
                </q-dialog>
              </q-fab>
              <!-- <div>
                <button @click="modifyBtn=true">수정</button>
                <button @click="deleteBtn = true">삭제</button>
              </div> -->
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
  position: relative;
  display: inline-block;
  cursor: pointer;
  width: 100%;
  border-radius: 10px;
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
.book:hover{
  box-shadow:  
  -5px -5px 5px rgba(255,255,255,0.2), 5px 5px 5px rgba(0,0,0,0.1),
  inset -8px -8px 8px rgba(255,255,255,0.2), inset 8px 8px 8px rgba(0,0,0,0.1);
  transition: 1s
}

.card-description{
  width: 100%;
  margin-top:8px;
  margin-bottom: 8px;
  
}
.card-description > .user-comment{
  padding:0 8px;
}
.card-description > .user-nickname{
  padding: 0 8px;
  font-family: 'Noto Sans KR';
  font-weight: 700;
  font-size:13px;
}


#q-img__image>div:nth-child(2)::after, #q-img__image>div:nth-child(2)::after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: inherit;
  background-size:contain;
  transform-origin: center !important;
  transition: transform 0.4s ease-in !important;
}

.book--border-line:focus #q-img__image>div:nth-child(2)::after,
.book--border-line:hover #q-img__image>div:nth-child(2):after {
  transform: scale(1.1) !important;
}

/* buttons */


.more-btn {
  background-color: #DECBA7;
  color: white;
}

.del-btn {
  background-color: #b49d71;
  color: white;
}

.upd-btn {
  background-color: #b49d71;
  color: white;
}


.card-img-description{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: #F5F4F2;
  padding: 2rem 2rem 1rem;
  position: relative;
}
.card-img-description p{
  color: #fff;
}
.card-img-header{
  writing-mode: tb-rl;
  transform: rotate(-180deg);

}
.card-img-body{
  color:rgba(63, 44, 3, 0.637);
  /* margin: auto 0px; */
  padding: 1.6rem;
  min-height: 230px;
  position:relative;
  margin:0;
  box-shadow: -8px -8px 8px rgba(255,255,255,0.2), 8px 8px 8px rgba(0,0,0,0.1),
  inset -8px -8px 8px rgba(255,255,255,0.2), inset 8px 8px 8px rgba(0,0,0,0.1);;
  border-radius: 10px;  
  outline-offset: 3px;
}
.card-img-body> div:nth-child(1){
  font-size:1.5rem;
  word-break:break-all;
  margin-right:0;
  margin-bottom:0;
  font-family: 'Noto Serif KR';
  font-weight:300;
  font-size: 15px;
  height: 120px;
  margin-bottom: 60px;
  margin-top: 40px;
  line-height: 185%;
}
.card-img-body> div:nth-child(2){
  text-align: right;
  word-break:break-all;
  margin-bottom:0;
  right: 10%;
  font-weight: 800;
}
.card-img-footer{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items:center;
  margin-top: 30px;
}
.card-img-footer>p{
  margin:0px;
  font-weight: 800;
}
</style>
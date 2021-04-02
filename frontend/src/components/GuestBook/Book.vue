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
        <!-- <strong class="user-comment text-center">{{article.guestbook_comment}}</strong> -->
        <span class="user-nickname text-caption text-right">
          {{article.user_nickname}}
        </span>
      </div>
    </div>
    <q-dialog v-model="prompt">
        <div class="row" style="min-width: 1080px;">
          <q-img
            v-if="article.guestbook_image"
            :src="article.guestbook_image"
            basic
            class="col-8"
            style="max-height:800px"
          >
          </q-img>
          <!-- 이미지 없을때 기본그림 설정 -->
          <img v-if!="article.guestbook_image"
            src="../../assets/mone.jpg" 
            class="col-8"
            style="max-height:800px; min-height:500px;"/>

          <div class="card-img-description col-4 column justify-between">
            <div class="card-img-header">
              <!-- <h2>CAT</h2> -->
            </div>
            <div class="card-img-body col justify-center items-center col-9">
              <div class="col-10" style="display:block; text-align:center;">{{article.guestbook_comment}}</div>
              <div class="col-2">
                <span>by </span>
                {{article.user_nickname}}
              </div>
            </div>
            <div class="card-img-footer col-2">
              <p style="color:#2a433b;">{{date}}</p>
              <q-fab padding="10px" text-color="white" icon="keyboard_arrow_left" direction="left" style="width:15%;" class="more-btn">
                <q-fab-action padding="6px" class="upd-btn" @click="modifyBtn=true" label="수정" label-position="bottom" label-style="font-size:12px;"/>
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
                <q-fab-action padding="6px"  class="del-btn" @click="deleteBtn = true" label="삭제" label-position="bottom" label-style="font-size:12px;color:#fff;"/>
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
                      <q-btn @click="deleteArticle" label="삭제" color="red-6" v-close-popup />
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
::selection{
  background: #fe3901;
  color:#fff
}
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
  /* padding: 8px; */
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
  border-top-color: #fe3901;
  border-right-color: #fe3901;
  -webkit-transition: width 0.2s ease-out, height 0.2s ease-out 0.2s;
  transition: width 0.2s ease-out, height 0.2s ease-out 0.2s;
}
.book--border-line:hover:before {
  border-bottom-color: #fe3901;
  border-left-color: #fe3901;
  -webkit-transition: border-color 0s ease-out 0.4s, width 0.2s ease-out 0.4s, height 0.2s ease-out 0.6s;
  transition: border-color 0s ease-out 0.4s, width 0.2s ease-out 0.4s, height 0.2s ease-out 0.6s;
}

.card-description{
  width: 100%;
  margin-top:10px;
  margin-bottom: 10px;
  
}
.card-description > .user-comment{
  padding:0 8px;
}
.card-description > .user-nickname{
  padding: 0 8px;
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

/* buttons */


.more-btn {
  background-color: #DECBA7;
  color: white;
}

.del-btn {
  background-color: #fe3901;
  color: white;
}

.upd-btn {
  background-color: #2a433b;
  color: white;
}


.card-img-description{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background: #F5F4F2;
  padding: 1rem 2rem;
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
  color:#2a433b;
  margin: auto 0px;
  padding: 1rem;
  min-height: 220px;
  position:relative;
  margin:0;
  border: solid 2.2px #DECBA7;
  outline: solid 1px #DECBA7;
  /* height:87%; */
  outline-offset: 15px;
}
.card-img-body> div:nth-child(1){
  font-size:1.5rem;
  word-break:break-all;
  margin-right:0;
  margin-bottom:0;
  
}
.card-img-body> div:nth-child(2){
  text-align: right;
  word-break:break-all;
  margin-top: 20px;
  margin-right:0 !important;
  margin-bottom:0;
  right: 10%;
  position:absolute;
  /* top:0; */
}
.card-img-footer{
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items:center;
}
.card-img-footer>p{
  margin:0px;
}
</style>
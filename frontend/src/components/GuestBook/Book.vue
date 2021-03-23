<template>
  <div>
    <div class="book book--border-line" @click="prompt = true">
      <q-card class="my-card">
        <q-img
          :src="article.guestbook_image"
          basic
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
        <q-card style="min-width: 820px;">
          <q-img
            :src="article.guestbook_image"
            basic
            :ratio="1"
          >
          </q-img>
        </q-card>
      </q-dialog>
  </div>
</template>

<script>
import timeForToday from '@/plugins/timeForToday'

export default {
  name:'Book',
  data() {
    return {
      prompt:false
    }
  },
  props:{
    article:Object
  },
  created() {
    
  },
  computed: {
    date(){
      return timeForToday(this.article.created_date)
    },
  },
  methods: {
  }
}
</script>

<style scope>
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
</style>
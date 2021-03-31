<template>
  <div>
    <!-- <Icons/> -->
    <div class="guestbook-header row justify-between items-center">
      <h3>GUESTBOOK</h3>
      <BookWrite/>
    </div>
    <q-page-container class="guestbook-body">
      <q-page>
        <q-infinite-scroll @load="onLoad" :offset="350">
          <masonry :cols="{ default: 3, 576: 1 }" :gutter="15" style="padding:12px 15px;">
            <Book v-for="(article, idx) in articles" :key="idx" :article="article" />
          </masonry>
          <template v-slot:loading>
            <div class="row justify-center q-my-md">
              <q-spinner-dots color="deep-orange" size="30px" />
            </div>
          </template>
        </q-infinite-scroll>
        <div v-if="endFlag" class="end-text row items-center">
          <div @click="goUp" style="cursor:pointer;">
            목록의 끝입니다☺
          </div>
          <div></div>
        </div>
      </q-page>
    </q-page-container>
  </div>
</template>

<script>
import * as articleApi from '@/api/v1/guestbook'

export default {
  name: 'GuestBook',
  components: {
    Book: () => import('@/components/GuestBook/Book'),
    BookWrite: () => import('@/components/GuestBook/BookWrite'),
    // Icons: () => import('@/components/IconMap/Icons'),
  },
  computed:{
    articles() {
      return this.$store.state.guestbook.articles
    }
  },
  data() {
    return {
      //masonry + infinity
      page: 1,
      endFlag:false
    }
  },
  created() {
    this.emptyArticles()
  },
  methods: {
    goUp(){
      window.scrollTo(0,0)
    },
    onLoad (index, done) {
      const EACH_LEN = 15;
      const params = {
        "page":String(this.page),
        "articles_per_page":String(EACH_LEN)
      }
      articleApi
        .GetArticles(params)
        .then((res) => {
          setTimeout(() => {
            if (res.data.length) {
              this.page += 1;
              this.$store.dispatch('guestbook/getArticles',res.data)
              // this.articles = this.articles.concat(res.data);
              console.log(res.data.length)
              done();
            } else{
              done(true)
              this.endFlag=true
            }
          }, 1000);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    emptyArticles() {
      this.$store.dispatch('guestbook/emptyArticles')
    },
  }
}
</script>

<style scoped>
.form-top{
  display: flex;
}
.guestbook-header{
  min-height: 100px;
  max-width: 1420px;;
  margin: 0 auto;
  padding : 0 5%;
}
.guestbook-body{
  max-width: 1420px;;
  margin: 0 auto;
}
.end-text{
  top: 12px;
  font-size: 20px;
  position: relative;
  color:#fff;
  text-align: center;
  margin-bottom: 50px;
}
.end-text>div:nth-child(1){
  position: absolute;
  width: 200px;
  background-color: #2a433b;
  z-index: 3;
  top:50%;
  left:43%;
  
  /* background-color: #2a433b; */
}
.end-text>div:nth-child(2){
  position: absolute;
  transform: translate(8px,-10px);
  z-index: 2;
  width: 200px;
  height: 30px;
  background-color: #fe3901;
  
  top:50%;
  left:43%;
}
</style>
<template>
  <div>
    <!-- <Icons/> -->
    <div class="guestbook-header row justify-between items-center">
      <h3>GUESTBOOK</h3>
      <BookWrite/>
    </div>
    <q-layout>
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
    </q-layout>
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
  margin-bottom: 100px;
  margin-top: 50px;
}
.end-text>div:nth-child(2){
  position: absolute;
  width: 200px;
  height: 50px;
  background-color: #2a433b;
  line-height: 50px;
  z-index: 3;
  top:50%;
  left:43%;
  /* vertical-align: middle; */
  /* background-color: #2a433b; */
}
.end-text>div:nth-child(3){
  position: absolute;
  transform: translate(8px,-10px);
  z-index: 2;
  width: 200px;
  height: 45px;
  background-color: #fe3901;
  
  top:50%;
  left:43%;
}

.end-text>div:nth-child(1),
.end-text>div:nth-child(4){
  border: 1px solid #DECBA7;
  margin: 0 10%;
  width:25%;
  align-content: center;
  top:50%;
  /* position: absolute; */
}



h2 {
    font: 33px sans-serif;
    margin-top: 30px;
    text-align: center;
    text-transform: uppercase;
}

h2.background {
    position: relative;
    z-index: 1;
}


.background:before {
    border-top: 2px solid #DECBA7;
    content:"";
    margin: 0 auto; /* this centers the line to the full width specified */
    position: absolute; /* positioning must be absolute here, and relative positioning must be applied to the parent */
    top: 50%; left: 0; right: 0; bottom: 0;
    width: 95%;
    z-index: -1;
}

.background > span {
 
        /* to hide the lines from behind the text, you have to set the background color the same as the container */ 
  background: white; 
  color: #2a433b;
  padding: 0 15px;
  margin: 0 15px; 
  z-index: 3;

}


h2.double:before { 
    /* this is just to undo the :before styling from above */
    border-top: none; 
}

h2.double:after {
    border-bottom: 1px solid blue;
    -webkit-box-shadow: 0 1px 0 0 red;
    -moz-box-shadow: 0 1px 0 0 red;
    box-shadow: 0 1px 0 0 red;
    content: "";
    margin: 0 auto; /* this centers the line to the full width specified */
    position: absolute;
    top: 45%; left: 0; right: 0;
    width: 95%;
    z-index: -1;
}


</style>
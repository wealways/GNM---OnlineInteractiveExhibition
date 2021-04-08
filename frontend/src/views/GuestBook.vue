<template>
  <div class='container'>
    <IconMap/>
    <div class="guestbook-header row justify-between items-center">
      <h3 style="color:#2A433B;">GUESTBOOK</h3>
      <BookWrite/>
    </div>
    <q-layout>
      <q-page-container class="guestbook-body">
        <q-page>
          <q-infinite-scroll @load="onLoad" :offset="350">
            <masonry :cols="{ default: 5, 576: 1 }" :gutter="15" style="padding:12px 15px;">
              <Book v-for="(article, idx) in articles" :key="idx" :article="article" />
            </masonry>
            <template v-slot:loading>
              <div class="row justify-center q-my-md">
                <q-spinner-dots color="deep-orange" size="30px" />
              </div>
            </template>
          </q-infinite-scroll>
          <div v-if="endFlag" class="end-text row items-center justify-between">
            <div class='endline'>
              <hr class='hrline'>
            </div>
            <div @click="goUp" style="cursor:pointer; display:flex;" class="hoverbtn">
              <div>목록의 끝입니다</div>
              <q-icon name="mdi-arrow-up-circle-outline"></q-icon>
            </div>
            <div class='blank'></div>
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
    IconMap: () => import('@/components/IconMap/IconMap'),
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
      endFlag:false,
      fullWidth: false,
    }
  },
  mounted(){
    // 세션에 매핑되는 이미지 가져오기 (미완성)
    this.$store.dispatch('guestbook/getImages',this.$route.name)
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
.container {
  background-color: #FCF9F2;
}

.mapwrapper {
  background-color: #FCF9F2;
}


.map {
  position: absolute;
  left: 3%;
  top: 5%;
  background-color: transparent;
}

.map:hover {
  color: red;
}

.mapback {
  height: 80%;
}
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
  font-size: 20px;
  font-family:'Noto Sans KR';
  font-weight: 900;
  position: relative;
  color:#DECBA7;
  text-align: center;
}
.endline{
  width: 80%;
  margin-left: 6%;
}
.hrline {
  border: 2px solid #DECBA7;
}
.blank {
  height: 300px;
}
.hoverbtn:hover {
  font-size: 21px;
  transition: 0.7s;
}
h3{
  font-family: 'Montserrat';
}
</style>
<template>
  <div>
    <!-- <Icons/> -->
    <div class="guestbook-header row justify-between items-center">
      <h3>방명록</h3>
      <BookWrite/>
    </div>
    <q-page-container class="guestbook-body">
      <q-page>
        <masonry :cols="{ default: 5, 576: 1 }" :gutter="15" style="padding:12px 15px;">
          <Book v-for="(article, idx) in articles" :key="idx" :article="article" />
        </masonry>
      </q-page>
      <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
        <div slot="no-more" style="color: rgb(102, 102, 102); font-size: 14px; padding: 10px 0px;">
          목록의 끝입니다 :)
        </div>
      </infinite-loading>
    </q-page-container>
  </div>
</template>

<script>
import * as articleApi from '@/api/v1/guestbook'
import InfiniteLoading from 'vue-infinite-loading';

export default {
  name: 'GuestBook',
  components: {
    Book: () => import('@/components/GuestBook/Book'),
    BookWrite: () => import('@/components/GuestBook/BookWrite'),
    // Icons: () => import('@/components/IconMap/Icons'),
    InfiniteLoading,
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
      handlerdata: '',
    }
  },
  created() {
    this.emptyArticles()
  },
  methods: {
    emptyArticles() {
      this.$store.dispatch('guestbook/emptyArticles')
    },
    // masonry + infinity
    infiniteHandler($state) {
      this.handlerdata = $state;
      const EACH_LEN = 20;
      const params = {
        "page":String(this.page),
        "articles_per_page":String(EACH_LEN)
      }
      articleApi
        .GetArticles(params)
        .then((res) => {
          setTimeout(() => {
            if (res.status===200) {
              $state.loaded();
              this.page += 1;
              this.$store.dispatch('guestbook/getArticles',res.data)
              // this.articles = this.articles.concat(res.data);
              console.log(res.data.length)
              if (res.data.length / EACH_LEN < 1) {
                $state.complete();
              }
            } else {
              $state.complete();
            }
          }, 1000);
        })
        .catch((err) => {
          console.log(err);
        });
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
}
.guestbook-body{
  max-width: 1420px;;
  margin: 0 auto;
}
</style>
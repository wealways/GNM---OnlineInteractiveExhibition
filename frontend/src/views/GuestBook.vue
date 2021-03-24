<template>
  <div>
    <div class="row justify-between items-center">
      <h3>방명록</h3>
      <BookWrite/>
    </div>
    <q-page-container>
      <q-page>
        <masonry :cols="{ default: 5, 576: 1 }" :gutter="15" style="padding:12px 15px;">
          <Book v-for="(article, idx) in articles" :key="idx" :article="article" />
        </masonry>
        <infinite-loading @infinite="infiniteHandler" spinner="waveDots">
          <div slot="no-more" style="color: rgb(102, 102, 102); font-size: 14px; padding: 10px 0px;">
            목록의 끝입니다 :)
          </div>
        </infinite-loading>
      </q-page>
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
      const EACH_LEN = 9;
      const params = {
        "page":String(this.page),
        "articles_per_page":String(EACH_LEN)
      }
      articleApi
        .GetArticles(params)
        .then((res) => {
          setTimeout(() => {
            if (res.data) {
              this.$store.dispatch('guestbook/getArticles',res.data)
              // this.articles = this.articles.concat(res.data);
              this.page += 1;
              $state.loaded();
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
</style>
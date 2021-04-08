<template>
  <div id="main">
    <!-- 평면도 -->
    <IconMap />
    <!-- 각각의 결과물 -->
    <OutputList />
    <!-- 방명록 작성 이동 -->
    <q-btn
      padding="lg"
      color="primary"
      icon="auto_stories"
      id="guest-book-btn"
      :to='"/guestbook"'
    >
      <q-tooltip 
        content-style="font-size: 16px"
        anchor="top middle" 
        self="bottom middle" 
        :offset="[10, 10]">
          <strong>방명록 작성</strong>
      </q-tooltip>
    </q-btn>
    <!-- 메인 벽지 -->
    <div class="wall"></div>
  </div>
</template>

<script>
import IconMap from "@/components/IconMap/IconMap.vue";
import OutputList from "@/components/SpecialGallery/OutputList.vue";
import $ from 'jquery'

export default {
  name: 'SpecialGallery',
  components: {
    IconMap,
    OutputList,
  },
  data() {
    return {
      test: false,
    }
  },
  mounted() {
    const $main = $('#main')
    // add caption container
    this.$caption = $( '<div class="gr-caption"><span class="gr-caption-close">x</span></div>' ).appendTo( $main );
    this.$caption.find( 'span.gr-caption-close' ).on( 'click', $.proxy( this.hideDescription, this ) );

    // click on item's caption
    var self = this;
    this.$el.on( 'click', 'figure > figcaption', function() {
      var $caption = $( this ),
        $item = $caption.parent(), 
        idx = $item.index() - 1;
      
      if( self.caption === self.currentItem && idx === self.currentItem ) {
        return false;
      }
      else if( idx !== self.currentItem ) {
        self.jump( idx, function() {
          self.showDescription( $caption, idx );
        } );
      }
      else {
        self.showDescription( $caption, idx );
      }
      
    } );
  },
}
</script>

<style scoped>
#main {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.column {
  align-self: center;
  display: flex;
  flex-direction: row;
}
/* guestbook 가는 버튼 */
#guest-book-btn {
  position: absolute;
  z-index: 2;
  bottom: 5%;
  right: 3%;
}
/* 메인 배경 */
.wall {
  z-index: -1;
  position: absolute;
  height:100%;
  width: 100%;
  background-image: url(https://cdn.pixabay.com/photo/2016/11/28/21/36/white-1866105_960_720.jpg);
  background-repeat: no-repeat;
  background-position: center;
  background-size: cover;
  
}
</style>
<template>
  <div id="main">
    <!-- 평면도 -->
    <IconMap />
    <!-- 각각의 결과물 -->
    <div class="list">
      <Output v-for="(image,idx) in selectableImages" :key="idx" :changedImage="image" :artist="artistName[idx]"/>
      <!-- <Output />
      <Output /> -->
    </div>
    <!-- 방명록 작성 이동 -->
    <div>
      <GoToGB style="position:absolute; bottom: 0px; right: 80px;"/>
    </div>
    <!-- 메인 벽지 -->
    <div class="wall"></div>
  </div>
</template>

<script>
import IconMap from "@/components/IconMap/IconMap.vue";
import GoToGB from "@/components/IconMap/GoToGB.vue";
import Output from "@/components/SpecialGallery/Output.vue";

export default {
  name: 'SpecialGallery',
  components: {
    IconMap,
    Output,
    GoToGB,
  },
  data() {
    return {
      test: false,
      artistName:['Monet','Klimt','천경자']
    }
  },
  computed:{
    selectableImages(){
      return this.$store.state.guestbook.selectable_images
    }
  }, 
  created(){
    this.$store.dispatch('guestbook/getImages',this.$route.name)
  },
  mounted() {
  },
  methods: {
  }
}
</script>

<style scoped>
#main {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  position:relative;
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
/* 결과물 리스트 */
.list {
  align-self: center;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
}

</style>
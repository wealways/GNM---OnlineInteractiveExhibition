<template>
  <div id="main">
    <!-- 평면도 -->
    <IconMap />
    <!-- 각각의 결과물 -->
    <div class="list">
      <Output />
      <Output />
      <Output />
    </div>
    <!-- <div class="q-pa-md">
      <q-btn color="purple" @click="showNotif" label="Show Notification" />
    </div> -->
    <!-- 설명 자세히 보기 -->
    <div class="description">
      <q-icon name="disabled_by_default" id="description-close"/>
      <p><strong>천경자</strong> 작가의 화풍으로 변환된 사진입니다</p>
      <hr>
      <div class="decription-btn">
      <q-btn push label="저장하기" class="btn"/>
      <q-btn push label="원본보기" class="btn"/>
      </div>
    </div>
    <!-- 방명록 작성 이동 -->
    <div>

      <GoToGB style="position:absolute; bottom: 0px; right: 80px;"/>
    </div>
    <!-- <q-btn
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
    </q-btn> -->
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
    }
  },
  mounted() {
    },
  methods: {
    showNotif () {
      this.$q.notify({
        message: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Hic quisquam non ad sit assumenda consequuntur esse inventore officia. Corrupti reiciendis impedit vel, fugit odit quisquam quae porro exercitationem eveniet quasi.',
        html: true,
        color: 'grey-12',
        multiLine: true,
        timeout: 0,
        badgeStyle: "opacity: 0",
        actions: [
          { label: 'X', color: 'black', handler: () => { /* ... */ } },
          { label: '저장하기', color: 'black', handler: () => { /* ... */ } }
        ]
      })
    }
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
  flex-wrap: nowrap;
}
/* 작품 설명 나오기*/
.description {
	position: absolute;
	width: 500px;
	height: 200px;
	padding: 20px;
	left: 50%;
	margin-left: -250px;
	bottom: 0;
	background: #ececec;
	box-shadow: 0 -1px 3px rgba(0,0,0.5,0.5);
	/* -webkit-transform: translateY(310px);
	-webkit-transition: -webkit-transform .5s ease;
	-moz-transform: translateY(310px);
	-moz-transition: -moz-transform .5s ease;
	-o-transform: translateY(310px);
	-o-transition: -o-transform .5s ease;
	transform: translateY(310px);
	transition: transform .5s ease; */
}
.description p {
  margin: 0;
  font-size: 18px;
}
.decription-btn {
  height: 90%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  /* align-items: flex-end; */
}
.btn {
  margin: 2% 15%;
  border-radius: 36px;
  background: linear-gradient(145deg, #fdfdfd, #d4d4d4);
  box-shadow:  13px 13px 26px #c9c9c9,
             -13px -13px 26px #ffffff;
  background-color: #ececec;
  color: #695c4c;

}
.btn:hover {
  background-color: #f000;
}
/* 작품 설명 닫기 */
#description-close {
  position: absolute;
  top: 5px;
  right: 5px;
  font-size: 25px;
  color: white;
  background-color: #72748d;
  cursor: pointer;
}
</style>
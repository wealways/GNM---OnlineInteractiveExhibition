import axios from 'axios';
import * as articleApi from '@/api/v1/guestbook'

export default {
  namespaced: true,
  state: {
    articles:[],
    modal_flag:false,
    user_article:{
      user_nickname:null,
      guestbook_image:null,
      guestbook_password:null,
      guestbook_comment:null,
      id:null
    },
    on_modify:false
  },

  // ==============================================================

  mutations: {
    // 글 불러오기
    GET_ARTICLES(state,articles){
      state.articles = state.articles.concat(articles)
    },
    EMPTY_ARTICLES(state){
      state.articles = []
    },

    // 글 작성하기
    CREATE_ARTICLE(state,article){
      state.articles.unshift(article)
    },

    // 글 삭제
    DELETE_ARTICLE(state,article_id){
      let idx = 0 
      state.articles.forEach(function(data,i){
        if(data.id===article_id){
          idx = i
        }
      })
      state.articles.splice(idx,1)

    },

    // 비밀번호 확인 후 방명록 작성 modal flag = true 변경
    // 방명록작성 버튼 클릭시 modal flag = true 변경
    // 방명록 작성 modal에서 modal flag = false 변경 (BookWrite.vue에서 onReset 함수 이용)
    // 방명록 작성 modal에서 취소 버튼 클릭스 modal flag = false 변경 (BookWrite.vue에서 onReset 함수 이용)
    CHANGE_FLAG(state,flag){
      state.modal_flag = flag
    },

    // 방명록 수정 상황에서 article_id 가지고 있어야 함
    MODIFY_ON(state,id) {
      state.on_modify = true
      let idx = 0 
      state.articles.some(function(data,i){
        if(data.id===id){
          idx = i
        }
      })
      state.user_article.id = state.articles[idx].id
      state.user_article.user_nickname = state.articles[idx].user_nickname
      state.user_article.guestbook_image = state.articles[idx].guestbook_image
      state.user_article.guestbook_password = state.articles[idx].guestbook_password
      state.user_article.guestbook_comment = state.articles[idx].guestbook_comment
    },

    //수정진행중인 상황 바꿔주기
    CHANGE_ON(state,flag){
      state.on_modify = flag
    },

    //글 수정하기
    MODIFY_ARTICLE(state,params){
      const article_id = params.article_id
      const modified = params.modified

      let idx = 0 
      state.articles.some(function(data,i){
        if(data.id===article_id){
          idx = i
        }
      })
      state.articles[idx].id = modified.id
      state.articles[idx].created_date = modified.created_date
      state.articles[idx].updated_date = modified.updated_date
      state.articles[idx].user_nickname = modified.user_nickname
      state.articles[idx].guestbook_comment = modified.guestbook_comment
      state.articles[idx].guestbook_image = modified.guestbook_image
      state.articles[idx].guestbook_password = modified.guestbook_password
    }
  },

  // ==============================================================

  actions: {
    //글 불러오기
    getArticles({commit},articles){
      commit('GET_ARTICLES',articles)
    },
    emptyArticles({commit}){
      commit('EMPTY_ARTICLES')
    },

    // 글쓰기
    async createArticle({commit},data){
      const cat = await axios.get('https://api.thecatapi.com/v1/images/search')
      data.guestbook_image = cat.data[0].url

      articleApi.CreateArticle(data)
      .then((res)=>{
        commit('CREATE_ARTICLE',res.data)
      })
      .catch((err)=>{
        console.log(err)
      })
    },
    
    //삭제
    deleteArticle({commit},params) {
      articleApi.DeleteArticle(params.id,params.password)
      .then((res)=>{
        if(res.data.result===false){
          alert('비밀번호를 확인하세요')
        }else{
          alert('삭제되었습니다.')
          commit('DELETE_ARTICLE',params.id)
        }
      })
      .catch((err)=>{
        console.log('삭제에러')
        console.log(err)
      })
    },

    // 수정 전 비밀번호 확인
    confirmPassword({commit},data){
      articleApi.ConfirmPassword(data.id,data.guestbook_password)
      .then((res)=>{
        if(res.data.result){
          commit('CHANGE_FLAG',true)
          commit('MODIFY_ON',data.id)
          commit('CHANGE_ON',true)
        }else{
          alert('비밀번호를 확인하세요')
        }
      })
      .catch((err)=>{
        console.log(err)
      })
    },

    // modal flag 변화시키기
    changeFlag({commit},flag){
      commit('CHANGE_FLAG',flag)
    },
    // 수정 진행중 변화시키기
    changeOn({commit},flag){
      commit('CHANGE_ON',flag)
    },

    // 글 수정하기
    modifyArticle({commit},params){
      articleApi.ModifyArticle(params.article_id,params.data)
      .then((res)=>{
        if(res.data.result===false){
          alert('수정실패')
        }else{
          commit('MODIFY_ARTICLE',{article_id:params.article_id,modified:res.data})
        }
      })
      .catch((err)=>{
        console.error(err)
      })

    }
  },

  // =============================================================

  getters:{
    modal_flag(state) {
      return state.modal_flag
    },
    on_modfiy(state){
      return state.on_modify
    },
    user_article(state) {
      return state.user_article
    }
  }
};

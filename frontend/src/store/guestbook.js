

export default {
  namespaced: true,
  state: {
    articles:[]
  },
  mutations: {
    STORE_ARTICLES(state,articles){
      state.articles = state.articles.concat(articles)
    },
    EMPTY_ARTICLES(state){
      state.articles = []
    }
  },
  actions: {
    storeArticles({commit},articles){
      commit('STORE_ARTICLES',articles)
    },
    emptyArticles({commit}){
      commit('EMPTY_ARTICLES')
    }
  },
  getters:{

  }
};

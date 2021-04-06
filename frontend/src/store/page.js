export default {
  namespaced: true,

  state: {
    page:1
  },

  mutations: {
    PAGE_CHANGE(state,page){
      state.page = page
    }
  },

  actions: {
    pageChange({commit},page){
      commit('PAGE_CHANGE',page)
    }
  },

  getters:{

  }
};

import * as Api from '@/api/v1/guestbook'

export default {
    namespaced: true,
  
    state: {
      sessionInfo: "",
    },
  
    mutations: {
      GET_SESSION(state, sessionkey){
        state.sessionInfo = sessionkey;
      }
    },
  
    actions: {
      getSession({commit}){
        // session storage에 session key가 없으면 getSession 실행
        let check = sessionStorage.getItem("session")
        if (check===null){
          Api.getSession()
          .then((response)=>{
            let sessionkey = response.data.sessionkey
            sessionStorage.setItem("session", sessionkey)
            commit('GET_SESSION',sessionkey)
          })
          .catch((err)=>{
            console.log(err)
          })
        }
      }
    },
  
    getters:{

    }
  };
  
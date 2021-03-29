import * as Api from '@/api/v1/guestbook'

export default {
    namespaced: true,
  
    state: {
      isSession: false,
    },
  
    mutations: {
      GET_SESSION(state){
        state.isSession = true;
      }
    },
  
    actions: {
      getSession({commit}){
        // session storage에 session key가 없으면 getSession 실행
        let check = sessionStorage.getItem("session")
        if (check===null){
          Api.getSession()
          .then((response)=>{
            console.log(response)
            let sessionkey = response.data.sessionkey
            sessionStorage.setItem("session", sessionkey)
            commit('GET_SESSION')
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
  
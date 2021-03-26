import axios from "axios";

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
        axios.post('http://localhost:8000/articles/session/')
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
    },
  
    getters:{

    }
  };
  
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000',
  // baseURL: 'http://j4c106.p.ssafy.io/api/',
  headers:{
    // post:{
    //   'Access-Control-Allow-Origin':'*'
    // }
  }
});

export default instance;
import axios from 'axios';

const instance = axios.create({
  // baseURL: 'http://localhost:8000',
  baseURL: 'http://localhost:8000',
  headers:{
    // post:{
    //   'Access-Control-Allow-Origin':'*'
    // }
  }
});

export default instance;
import axios from 'axios';

const instance = axios.create({
  baseURL: 'http://localhost:8000',
  headers:{
    post:{
      'Access-Control-Allow-Origin':'http://127.0.0.1:8000/'
    }
  }
});

export default instance;
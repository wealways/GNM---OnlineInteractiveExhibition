import axios from "axios";
import { API_BASE_URL } from "../config";

function createInstance() {
    const instance = axios.create({
        baseURL: API_BASE_URL,
        header: {
            'Content-Type': 'application/json'
        }
    });
    return instance;
}

function createInstanceFile() {
    const instance = axios.create({
        baseURL: API_BASE_URL,
        header: {
            'Content-Type': 'multipart/form-data'
        }
    });
    instance.interceptors.request.use(function (config){
        const token = sessionStorage.getItem('sessionkey');
        config.headers.Authorization = token ? `Bearer ${token}` : '';
        return config
    })
    return instance;
}

export { createInstance,createInstanceFile };


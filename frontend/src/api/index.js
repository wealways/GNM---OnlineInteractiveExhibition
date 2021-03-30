import axios from "axios";
import { API_BASE_URL } from "../config/index"

function createInstance() {
    let token = sessionStorage.getItem('session')
    const headers = {
        'Authorization': `${token}`
    }
    const instance = axios.create({
        baseURL: API_BASE_URL,
        headers: headers
    });
    return instance;
}

function createInstanceFile() {
    let token = sessionStorage.getItem('session')
    const headers = {
        'sessionkey': `${token}`
    }
    const instance = axios.create({
        baseURL: API_BASE_URL,
        headers: headers
    });
    return instance;
}

export { createInstance, createInstanceFile };


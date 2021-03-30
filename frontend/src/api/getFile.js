import http from '@/api/http'


function getFile(success, fail) {
    let token = sessionStorage.getItem('session')
    const headers = {
        'content-type':'application/json',
        'sessionkey': `${token}`
    }
    http
        .get(`galleries/passcard/`,{headers:headers})
        .then(success)
        .catch(fail);
}

export {getFile};


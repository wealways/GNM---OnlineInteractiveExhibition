import http from '@/api/http'


function getFile(artist, success, fail) {
    let token = sessionStorage.getItem('session')
    const headers = {
        'content-type':'application/json',
        'sessionkey': `${token}`
    }
    http
        .get(`galleries/image/input/${artist}/`,{headers:headers})
        .then(success)
        .catch(fail);
}

export {getFile};


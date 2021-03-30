import http from '@/api/http'


function getFile(artist, success, fail) {
    let token = sessionStorage.getItem('session')
    const headers = {
        'sessionkey': `${token}`
    }
    http
        .post(`galleries/image/input/${artist}/`,{headers:headers})
        .then(success)
        .catch(fail);
}

export {getFile};


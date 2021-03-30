import http from '@/api/http'

function fileUpload(artist, file, success, fail) {
    let token = sessionStorage.getItem('session')
    const headers = {
        'content-type': 'multipart/form-data',
        'sessionkey': `${token}`
    }
    console.log(headers)
    http
        .post(`galleries/image/input/${artist}/`,file,{headers:headers})
        .then(success)
        .catch(fail);
}

export {fileUpload};

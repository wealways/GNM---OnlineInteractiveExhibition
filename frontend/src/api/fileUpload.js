import http from '@/api/http'

export function fileUpload(artist, file) {
  let token = sessionStorage.getItem('session')
  const headers = {
    'content-type': 'multipart/form-data',
    'sessionkey': `${token}`
  }
  // console.log(headers)
  return http.post(`galleries/image/input/${artist}/`,file,{headers:headers})
}

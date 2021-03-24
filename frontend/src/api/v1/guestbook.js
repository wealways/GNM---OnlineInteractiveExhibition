import http from '@/api/http';

export function GetArticles(){
  return http.get('/articles/');
}

export function CreateArticle(params){
  console.log(params)
  return http.post('/articles/',params);
}
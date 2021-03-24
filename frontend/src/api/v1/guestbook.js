import http from '@/api/http';

export function GetArticles(params){
  return http.get('/articles/',{params:params});
}

export function CreateArticle(params){
  return http.post('/articles/',params);
}

export function DeleteArticle(article_id,password){
  const body = {
    "guestbook_password":password
  }
  return http.delete(`/articles/${article_id}/`,{data:body})
}

//비밀번호확인
export function ConfirmPassword(article_id,guestbook_password){
  return http.post(`/articles/password/${article_id}/`,{guestbook_password})
}

//글 수정
export function ModifyArticle(article_id,params){
  // params = article Object
  return http.put(`/articles/${article_id}/`,{data:params})
}
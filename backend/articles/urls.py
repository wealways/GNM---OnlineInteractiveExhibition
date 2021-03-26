from django.urls import path, include
from . import views 

app_name = 'articles'
urlpatterns = [
    path('', views.article_list_create),
    path('<int:article_pk>/', views.article_update_delete),
    path('password/<int:article_pk>/', views.password_check),
    path('session/', views.session),
]
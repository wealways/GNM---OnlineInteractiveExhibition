from django.urls import path, include
from . import views 

app_name = 'articles'
urlpatterns = [
    path('', views.article_list_create),
    # path('<int:card_id>', views.card_update_delete),

]
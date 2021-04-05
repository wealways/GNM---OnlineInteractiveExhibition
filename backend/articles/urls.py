# from django.urls import path, include
# from . import views 
# from rest_framework.routers import DefaultRouter
# from articles.views import ArticleViewSet
# from rest_framework import renderers

# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'', views.ArticleViewSet, basename='article')


# app_name = 'articles'
# urlpatterns = [
#     path('password/<int:article_pk>/', views.password_check),
#     path('session/', views.session),
#     path('', include(router.urls))
# ]
from django.urls import path, include
from . import views 
from rest_framework.routers import DefaultRouter
from articles.views import ArticleViewSet
from rest_framework import renderers

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'', views.ArticleViewSet, basename='article')


app_name = 'articles'
urlpatterns = [
    path('password/<int:article_pk>/', views.password_check),
    path('session/', views.session),
    path('expire/', views.expire),
    path("", ArticleViewSet.as_view({"get": "get", "post": "create"}), name="article"),
    path("<int:pk>/", ArticleViewSet.as_view({"put": "update", "delete": "delete"}), name="articleud"),
    # path('', include(router.urls))
]
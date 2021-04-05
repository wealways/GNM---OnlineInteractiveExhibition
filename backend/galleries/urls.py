from django.urls import path, include
from . import views 
from galleries.views import GalleryViewSet


app_name = 'galleries'
urlpatterns = [
    path("image/<str:imgtype>/<int:no>/", GalleryViewSet.as_view({"get": "get", "post": "create"}), name="gallery"),
    path('passcard/', views.passcard),
    path('test/', views.test)
]
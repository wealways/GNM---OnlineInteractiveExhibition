from django.urls import path, include
from . import views 
# from rest_framework.routers import DefaultRouter
from galleries.views import GalleryViewSet
# from rest_framework import renderers

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'gallery', views.GalleryViewSet, basename='gallery')


app_name = 'galleries'
urlpatterns = [
    path("image/<str:type>/<int:no>/", GalleryViewSet.as_view({"get": "get", "post": "create"}), name="gallery"),
    path('passcard/', views.passcard),
    # path('receiveimage/', views.receiveimage),
    # path('giveimage/<int:input_no>/', views.giveimage),
    # path('', include(router.urls)),
]
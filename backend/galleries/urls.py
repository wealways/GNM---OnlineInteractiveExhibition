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
    # path('receiveimage/', views.receiveimage),
    path("image/<str:type>/<int:no>/", GalleryViewSet.as_view({"get": "list", "post": "create"}), name="gallery"),
    path('giveimage/<int:input_no>/', views.giveimage),
    path('passcard/', views.passcard),
    # path('', include(router.urls)),
]
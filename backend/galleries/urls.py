from django.urls import path, include
from . import views 

app_name = 'galleries'
urlpatterns = [
    path('receiveimage/', views.receiveimage),
    path('giveimage/<int:input_no>/', views.giveimage),
    path('passcard/', views.passcard),
]
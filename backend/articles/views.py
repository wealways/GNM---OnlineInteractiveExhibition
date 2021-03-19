from django.shortcuts import render,get_object_or_404, get_list_or_404
from .serializers import GuestbookSerializer
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Guestbook
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def article_list_create(request):
    if request.method == "GET":
        articles = Guestbook.objects.all()
        serializer = GuestbookSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    else : # POST request 
        serializer = GuestbookSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)
    


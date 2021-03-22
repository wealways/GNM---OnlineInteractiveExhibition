from django.shortcuts import render,get_object_or_404, get_list_or_404
from .serializers import GuestbookSerializer
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Guestbook
from rest_framework.decorators import api_view
# from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@api_view(['GET', 'POST'])
# @swagger_auto_schema
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
    

@api_view(['PUT', 'DELETE'])
def article_update_delete(request,article_pk):
    article = get_object_or_404(Guestbook, pk=article_pk)
    if request.method == 'PUT':
        serializer = GuestbookSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return JsonResponse(serializer.data)
    else:
        article.delete()
        return JsonResponse({ 'id': article_pk })

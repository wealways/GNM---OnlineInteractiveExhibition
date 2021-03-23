from django.shortcuts import render,get_object_or_404, get_list_or_404
from .serializers import GuestbookSerializer, GuestbookBodySerializer
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Guestbook
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
# from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@api_view(['GET', 'POST'])
# @swagger_auto_schema(request_body=GuestbookBodySerializer)
def article_list_create(request):
    if request.method == "GET":
        articles = Guestbook.objects.all()
        serializer = GuestbookSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    else : # POST request 
        serializer = GuestbookSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            guestbook_password = make_password(request.POST.get('guestbook_password'))
            serializer.save(guestbook_password=guestbook_password)
            return JsonResponse(serializer.data)
    
# @swagger_auto_schema(request_body=GuestbookBodySerializer)
@api_view(['PUT', 'DELETE'])
def article_update_delete(request,article_pk):  
    # password = request.data.get('guestbook_password')
    # article_password = get_object_or_404(Guestbook, pk=article_pk).guestbook_password
    # res = check_password(password, article_password)
    article = get_object_or_404(Guestbook, pk=article_pk)
    if request.method == 'PUT':
        serializer = GuestbookSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            guestbook_password = make_password(request.POST.get('guestbook_password'))
            serializer.save(guestbook_password=guestbook_password)
            return JsonResponse(serializer.data)
    else:
        article.delete()
        return JsonResponse({ 'id': article_pk })

@api_view(['POST'])
def password_check(request, article_pk):
    password = request.data.get('guestbook_password')
    article_password = get_object_or_404(Guestbook, pk=article_pk).guestbook_password
    res = check_password(password, article_password)
    return JsonResponse({'result': res})
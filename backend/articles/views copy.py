from django.shortcuts import render,get_object_or_404, get_list_or_404
from .serializers import GuestbookSerializer, GuestbookBodySerializer
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Guestbook
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.utils import timezone


# from drf_yasg.utils import swagger_auto_schema

# Create your views here.
@api_view(['GET', 'POST'])
# @swagger_auto_schema(request_body=GuestbookBodySerializer)
def article_list_create(request):
    if request.method == "GET":
        # page = int(request.query_params.get('page')[0])
        page = int(request.query_params.get('page'))
        # articles_per_page = int(request.query_params.get('articles_per_page')[0])
        articles_per_page = int(request.query_params.get('articles_per_page'))
        
        start = (page-1) * articles_per_page
        end = page * articles_per_page
        articles = Guestbook.objects.all().order_by('-created_date')[start:end]
        serializer = GuestbookSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

    else : # POST request 
        serializer = GuestbookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            guestbook_password = make_password(request.data.get('guestbook_password'))
            serializer.save(guestbook_password=guestbook_password)
            return JsonResponse(serializer.data)
    
# @swagger_auto_schema(request_body=GuestbookBodySerializer)
@api_view(['PUT', 'DELETE'])
def article_update_delete(request,article_pk):  
    password = request.data.get('guestbook_password')
    article_password = get_object_or_404(Guestbook, pk=article_pk).guestbook_password
    res = check_password(password, article_password)
    if res:
        article = get_object_or_404(Guestbook, pk=article_pk)
        if request.method == 'PUT':
            serializer = GuestbookSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                guestbook_password = make_password(request.data.get('guestbook_password'))
                serializer.save(guestbook_password=guestbook_password)
                return JsonResponse(serializer.data)
        else:
            article.delete()
            return JsonResponse({ 'id': article_pk })
    else:
        return JsonResponse({'result':res})

@api_view(['POST'])
def password_check(request, article_pk):
    password = request.data.get('guestbook_password')
    article_password = get_object_or_404(Guestbook, pk=article_pk).guestbook_password
    res = check_password(password, article_password)
    return JsonResponse({'result': res})


@api_view(['POST'])
def session(request):
    # session-key exists
    if request.headers.get('sessionkey'):
        session_key = request.headers.get('sessionkey')
        m = Session.objects.get(pk=session_key)
        m.expire_date = timezone.now() + timezone.timedelta(days=50)
        m.save()
        return JsonResponse({'sessionkey':m.session_key})
    #session-key doesn't exist
    else:
        m = SessionStore()
        m.create()
        m.expire_date = timezone.now() + timezone.timedelta(days=50)
        m.save()
        return JsonResponse({'sessionkey':m.session_key})

from django.shortcuts import render,get_object_or_404, get_list_or_404
from .serializers import GuestbookSerializer, GuestbookBodySerializer, PasswordSerializer, GuestbookListSerializer
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from .models import Guestbook
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator
from drf_yasg import openapi
import datetime

# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):

    serializer_class = Guestbook

    queryset = Guestbook.objects.all()

    @swagger_auto_schema(query_serializer=GuestbookListSerializer)
    def get(self, request, **kwargs):

        page = int(request.query_params.get('page'))
        articles_per_page = int(request.query_params.get('articles_per_page'))
        
        start = (page-1) * articles_per_page
        end = page * articles_per_page
        articles = Guestbook.objects.all().order_by('-created_date')[start:end]
        serializer = GuestbookSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    

    @swagger_auto_schema(request_body=GuestbookBodySerializer)
    def create(self, request, **kwargs):
        serializer = GuestbookSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            guestbook_password = make_password(request.data.get('guestbook_password'))
            serializer.save(guestbook_password=guestbook_password)
            return JsonResponse(serializer.data)


    @swagger_auto_schema(request_body=GuestbookBodySerializer)    
    def update(self, request, pk, **kwargs):  
        password = request.data.get('guestbook_password')
        article_password = get_object_or_404(Guestbook, pk=pk).guestbook_password
        res = check_password(password, article_password)
        if res:
            article = get_object_or_404(Guestbook, pk=pk)
            serializer = GuestbookSerializer(article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                guestbook_password = make_password(request.data.get('guestbook_password'))
                serializer.save(guestbook_password=guestbook_password)
                return JsonResponse(serializer.data)
        else:
            return JsonResponse({'result':res})


    @swagger_auto_schema(request_body=GuestbookBodySerializer)   
    def delete(self, request, pk, **kwargs):
        password = request.data.get('guestbook_password')
        article_password = get_object_or_404(Guestbook, pk=pk).guestbook_password
        res = check_password(password, article_password)
        if res:
            article = get_object_or_404(Guestbook, pk=pk)
            article.delete()
            return JsonResponse({ 'id': pk })
        else:
            return JsonResponse({'result':res})


@swagger_auto_schema(method='post', request_body=PasswordSerializer)   
@api_view(['POST'])
def password_check(request, article_pk):
    password = request.data.get('guestbook_password')
    article_password = get_object_or_404(Guestbook, pk=article_pk).guestbook_password
    res = check_password(password, article_password)
    return JsonResponse({'result': res})



@swagger_auto_schema(
        method='post',
        manual_parameters=[openapi.Parameter('sessionkey', openapi.IN_HEADER,
        description="sessionkey",
        type=openapi.TYPE_STRING)]
    )
@api_view(['POST'])
def session(request):
    # session-key exists
    sessionkey = request.headers.get('sessionkey')
    m = Session.objects.filter(pk=sessionkey)
    if m:
        m = m[0]
        m.expire_date = timezone.now() + timezone.timedelta(days=30)
        m.save()
        return JsonResponse({'sessionkey':m.session_key})
    #session-key doesn't exist
    else:
        m = SessionStore()
        m.create()
        effectivetimes = 60 * 60 * 24 * 30 # 60초, 60분, 24시간, 30일
        m.set_expiry(effectivetimes)
        m.modified = True
        m.save()
        # print(m.expire_date)
        return JsonResponse({'sessionkey':m.session_key})




@swagger_auto_schema(
        method='put',
        manual_parameters=[openapi.Parameter('sessionkey', openapi.IN_HEADER,
        description="sessionkey",
        type=openapi.TYPE_STRING)]
    )
@api_view(['PUT'])
def expire(request):
    sessionkey = request.headers.get('sessionkey')
    m = Session.objects.filter(pk=sessionkey)
    if m:
        m = m[0]
        m.expire_date = timezone.now()
        m.save()
        return JsonResponse({'sessionkey':m.session_key, 'expire_date' : m.expire_date})
    else:
        return JsonResponse({'status' : 'session이 존재하지 않습니다.'})

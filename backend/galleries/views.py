from django.shortcuts import render,get_object_or_404, get_list_or_404
from .serializers import CardSerializer, ImageSerializer
from django.core import serializers
from django.http import JsonResponse, HttpResponse, FileResponse
from .models import Card
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.utils import timezone
import os
from drf_yasg import openapi
from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from pjt.settings.base import BASE_DIR
import requests
import json
# import os.path
# from django.utils.decorators import method_decorator
# from rest_framework.decorators import action
# https://drf-yasg.readthedocs.io/en/stable/custom_spec.html


# Create your views here.


sessionkey = openapi.Parameter('sessionkey', openapi.IN_HEADER, description="sessionkey", type=openapi.TYPE_STRING)



inputstatus = False







def session_check(sessionkey):
    session = Session.objects.filter(session_key=sessionkey)
    if session:
        date = timezone.now()
        if date > session[0].expire_date:
            sessionstatus = False
            # session[0].delete()
        else:
            sessionstatus = True
    else:
        sessionstatus = False

    return sessionstatus


class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = Card
    parser_classes = (MultiPartParser,)
    @swagger_auto_schema(
        manual_parameters=[sessionkey],
    )  
    def get(self, request, imgtype, no):
        sessionkey = request.headers.get('sessionkey')
        sessionstatus = session_check(sessionkey)
        if sessionstatus:
            card = Card.objects.filter(sessionkey=sessionkey)
            imagefield = str(imgtype) + '_image_' + str(no)
            cardquery = list(card.values(imagefield))
            imagefile = cardquery[0][imagefield]
            print(imagefile)
            imageaddress = os.path.join(*[BASE_DIR,'media',imagefile])
            img = open(imageaddress, 'rb')
            response = FileResponse(img)
            response['sessionkey'] = sessionkey
            return response
        else:
            return JsonResponse({'status': 'session이 존재하지 않거나 유효하지 않습니다.'})


    @swagger_auto_schema(
        request_body=ImageSerializer,
        manual_parameters=[sessionkey],
        ) 
    def create(self, request, imgtype, no, **kwargs):
        sessionkey = request.headers.get('sessionkey')
        sessionstatus = session_check(sessionkey)
        image = request.data.get('image')
        # print(image)
        if sessionstatus:
            card = Card.objects.filter(sessionkey=sessionkey)
            # card = get_object_or_404(Card, sessionkey=sessionkey)
            imagefield = str(imgtype) + '_image_' + str(no)
            data = {imagefield: image}
            if card:
                serializer = CardSerializer(card[0], data=data)
            else:
                serializer = CardSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(sessionkey=sessionkey)
                # AI 모델로 변환요청
                if imgtype =='input':
                    card = Card.objects.filter(sessionkey=sessionkey)
                    cardquery = list(card.values(imagefield))
                    imagefile = cardquery[0][imagefield]
                    imageaddress = os.path.join(*[BASE_DIR,'media',imagefile])
                    img = open(imageaddress, 'rb')
                    # 로컬 주소
                    base_url = 'http://127.0.0.1:'
                    # 해당 ai모델 연결
                    artist = ['monet/', 'klimt/', 'chun/']
                    # 해당 ai모델 포트 번호
                    port_num = ['8001/', '8002/', '8003/']
                    port_num = port_num[no - 1]
                    artist = artist[no - 1]
                    ai_url = base_url + port_num + artist
                    
                    print(f'요청 보내는 주소: {ai_url}')

                    response = requests.post(ai_url,files={'image': img},headers={'sessionkey': sessionkey})
                    response_status = json.loads(response.text)['status']
                    return JsonResponse({'status' : response_status}) 

                return JsonResponse(serializer.data)
        else:
            return JsonResponse({'status': 'session이 존재하지 않거나 유효하지 않습니다.'})


@swagger_auto_schema(
        method='get',
        manual_parameters=[sessionkey],
    ) 
@api_view(['get'])
def passcard(request):
    sessionkey = request.headers.get('sessionkey')
    sessionstatus = session_check(sessionkey)
    if sessionstatus:
        card = get_object_or_404(Card, sessionkey=sessionkey)
        serializer = CardSerializer(card)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse({'status': 'session이 존재하지 않거나 유효하지 않습니다.'})



@api_view(['POST'])
def test(request):
    print('im here')
    # sessionkey = request.headers.get('sessionkey')
    # sessionstatus = session_check(sessionkey)
    # image = request.file
    image = request.data.get('image')
    print(image)
    # if sessionstatus:
    #     print(image)
    return JsonResponse({'status' : 'success'})
        
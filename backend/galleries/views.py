from django.shortcuts import render,get_object_or_404, get_list_or_404
from .serializers import CardSerializer, CardBodySerializer, ImageSerializer
from django.core import serializers
from django.http import JsonResponse, HttpResponse, FileResponse
from .models import Card
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, FileUploadParser
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.utils import timezone
import os
from drf_yasg import openapi
from rest_framework import viewsets
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema, no_body   
from django.utils.decorators import method_decorator
from django.http.multipartparser import MultiPartParser


# input1 = openapi.Parameter('input_image_1', openapi.IN_FORM, description="input_image_1", type=openapi.TYPE_FILE)
# input2 = openapi.Parameter('input_image_2', openapi.IN_FORM, description="input_image_2", type=openapi.TYPE_FILE)
# input3 = openapi.Parameter('input_image_3', openapi.IN_FORM, description="input_image_3", type=openapi.TYPE_FILE)
# input4 = openapi.Parameter('input_image_4', openapi.IN_FORM, description="input_image_4", type=openapi.TYPE_FILE)
# output1 = openapi.Parameter('output_image_1', openapi.IN_FORM, description="output_image_1", type=openapi.TYPE_FILE)
# output2 = openapi.Parameter('output_image_2', openapi.IN_FORM, description="output_image_2", type=openapi.TYPE_FILE)
# output3 = openapi.Parameter('output_image_3', openapi.IN_FORM, description="output_image_3", type=openapi.TYPE_FILE)
# output4 = openapi.Parameter('output_image_4', openapi.IN_FORM, description="output_image_4", type=openapi.TYPE_FILE)
# input1 = openapi.Parameter('input_image_1', openapi.IN_BODY, description="input_image_1", type=openapi.TYPE_FILE)
# input2 = openapi.Parameter('input_image_2', openapi.IN_BODY, description="input_image_2", type=openapi.TYPE_FILE)
# input3 = openapi.Parameter('input_image_3', openapi.IN_BODY, description="input_image_3", type=openapi.TYPE_FILE)
# input4 = openapi.Parameter('input_image_4', openapi.IN_BODY, description="input_image_4", type=openapi.TYPE_FILE)
# output1 = openapi.Parameter('output_image_1', openapi.IN_BODY, description="output_image_1", type=openapi.TYPE_FILE)
# output2 = openapi.Parameter('output_image_2', openapi.IN_BODY, description="output_image_2", type=openapi.TYPE_FILE)
# output3 = openapi.Parameter('output_image_3', openapi.IN_BODY, description="output_image_3", type=openapi.TYPE_FILE)
# output4 = openapi.Parameter('output_image_4', openapi.IN_BODY, description="output_image_4", type=openapi.TYPE_FILE)
# input1 = openapi.Schema('input_image_1', openapi.TYPE_OBJECT, type=openapi.TYPE_STRING)
# input2 = openapi.Schema('input_image_2', openapi.TYPE_OBJECT, type=openapi.TYPE_STRING)
# input3 = openapi.Schema('input_image_3', openapi.TYPE_OBJECT, type=openapi.TYPE_STRING)
# input4 = openapi.Schema('input_image_4', openapi.TYPE_OBJECT, type=openapi.TYPE_STRING)
# output1 = openapi.Schema('output_image_1', openapi.TYPE_OBJECT, type=openapi.TYPE_STRING)
# output2 = openapi.Schema('output_image_2', openapi.TYPE_OBJECT, type=openapi.TYPE_STRING)
# output3 = openapi.Schema('output_image_3', openapi.TYPE_OBJECT, type=openapi.TYPE_STRING)
# output4 = openapi.Schema('output_image_4', openapi.TYPE_OBJECT, type=openapi.TYPE_STRING)
# input1 = openapi.Parameter('input_image_1', openapi.IN_QUERY, Required=False, description="input_image_1", type=openapi.TYPE_FILE)
# input2 = openapi.Parameter('input_image_2', openapi.IN_QUERY, Required=False, description="input_image_2", type=openapi.TYPE_FILE)
# input3 = openapi.Parameter('input_image_3', openapi.IN_QUERY, Required=False, description="input_image_3", type=openapi.TYPE_FILE)
# input4 = openapi.Parameter('input_image_4', openapi.IN_QUERY, Required=False, description="input_image_4", type=openapi.TYPE_FILE)
# output1 = openapi.Parameter('output_image_1', openapi.IN_QUERY, Required=False, description="output_image_1", type=openapi.TYPE_FILE)
# output2 = openapi.Parameter('output_image_2', openapi.IN_QUERY, Required=False, description="output_image_2", type=openapi.TYPE_FILE)
# output3 = openapi.Parameter('output_image_3', openapi.IN_QUERY, Required=False, description="output_image_3", type=openapi.TYPE_FILE)
# output4 = openapi.Parameter('output_image_4', openapi.IN_QUERY, Required=False, description="output_image_4", type=openapi.TYPE_FILE)
# openapi.Parameter('id', openapi.IN_PATH, type=openapi.TYPE_STRING, description='id', required=True, **{'x-example': '234'})




# openapi.Parameter(name="file",in_=openapi.IN_FORM,type=openapi.TYPE_FILE,required=True,  description="Document"                        )
# https://drf-yasg.readthedocs.io/en/stable/custom_spec.html


# Create your views here.


sessionkey = openapi.Parameter('sessionkey', openapi.IN_HEADER, description="sessionkey", type=openapi.TYPE_STRING)
image = openapi.Parameter('image', openapi.IN_BODY, description="image", type=openapi.TYPE_FILE)



class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = Card


    @swagger_auto_schema(
        manual_parameters=[sessionkey],
    )  
    def list(self, request, type, no):
        sessionkey = request.headers.get('sessionkey')
        if Card.objects.filter(sessionkey=sessionkey):
            card = Card.objects.filter(sessionkey=sessionkey)
            imagefield = str(type) + '_image_' + str(no)
            cardquery = list(card.values(imagefield))
            imagefile = cardquery[0][imagefield]
            base_address = 'C:/Users/multicampus/Desktop/s04p23c106/backend/pjt/media'
            img = open(os.path.join(base_address, imagefile), 'rb')
            response = FileResponse(img)
            response['sessionkey'] = sessionkey
            return response
        else:
            return JsonResponse({'status': 'session이 존재하지 않습니다.'})


    @swagger_auto_schema(
            parser_classes=(MultiPartParser,),
            # request_body=openapi.Schema('image', openapi.TYPE_FILE, type=openapi.TYPE_FILE),
            request_body=ImageSerializer,
            manual_parameters=[sessionkey],
        ) 
    def create(self, request, type, no):
        sessionkey = request.headers.get('sessionkey')
        image = request.data.get('image')
        if Card.objects.filter(sessionkey=sessionkey):
            card = get_object_or_404(Card, sessionkey=sessionkey)
            imagefield = str(type) + '_image_' + str(no)
            data = {imagefield: image}
            serializer = CardSerializer(card, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.sessionkey = sessionkey
                serializer.save()
                return JsonResponse(serializer.data)
        else:
            return JsonResponse({'status': 'session이 존재하지 않습니다.'})






@swagger_auto_schema(
        method='get',
        manual_parameters=[sessionkey],
    ) 
@api_view(['get'])
def passcard(request):
    
    sessionkey = request.headers.get('sessionkey')
    if Card.objects.filter(sessionkey=sessionkey):
        card = get_object_or_404(Card, sessionkey=sessionkey)
        serializer = CardSerializer(card)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse({'status': 'session이 존재하지 않습니다.'})























        

# @swagger_auto_schema(
#         methods=['post','put'],
#         parser_classes=(MultiPartParser,),
#         request_body=no_body,
#         manual_parameters=[sessionkey, input1, input2, input3, input4, output1, output2, output3, output4],
#     ) 
# @api_view(['POST', 'PUT'])
# def receiveimage(request):
#     sessionkey = request.headers.get('sessionkey')
#     if Card.objects.filter(sessionkey=sessionkey):
#         card = get_object_or_404(Card, sessionkey=sessionkey)
#         serializer = CardSerializer(card, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(sessionkey=sessionkey)
#             return JsonResponse(serializer.data)
#     else:
#         serializer = CardSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(sessionkey=sessionkey)
#             return JsonResponse(serializer.data)
#     return HttpResponse({'hi'})


@swagger_auto_schema(
        method='get',
        body_serializer=CardBodySerializer,
        manual_parameters=[sessionkey],
    )  
@api_view(['get'])
def giveimage(request, input_no):
    sessionkey = request.headers.get('sessionkey')
    if Card.objects.filter(sessionkey=sessionkey):
        card = Card.objects.filter(sessionkey=sessionkey)
        imagefield = 'input_image_' + str(input_no)
        cardquery = list(card.values(imagefield))
        # cardquery[0]['sessionkey'] = sessionkey
        imagefile = cardquery[0][imagefield]
        base_address = 'C:/Users/multicampus/Desktop/s04p23c106/backend/pjt/media'
        img = open(os.path.join(base_address, imagefile), 'rb')
        response = FileResponse(img)
        response['sessionkey'] = sessionkey
        return response
        # return FileResponse(img)
        # return JsonResponse(response[0])
    else:
        return JsonResponse({'status': 'session이 존재하지 않습니다.'})


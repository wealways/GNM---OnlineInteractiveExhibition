from django.shortcuts import render,get_object_or_404, get_list_or_404
from .serializers import CardSerializer
from django.core import serializers
from django.http import JsonResponse, HttpResponse
from .models import Card
from rest_framework.decorators import api_view
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.utils import timezone


# Create your views here.
@api_view(['POST', 'PUT'])
def receiveimage(request):
    sessionkey = request.headers.get('sessionkey')
    if Card.objects.filter(sessionkey=sessionkey):
        card = get_object_or_404(Card, sessionkey=sessionkey)
        serializer = CardSerializer(card, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(sessionkey=sessionkey)
            return JsonResponse(serializer.data)
    else:
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(sessionkey=sessionkey)
            return JsonResponse(serializer.data)


@api_view(['GET'])
def giveimage(request, input_no):
    sessionkey = request.headers.get('sessionkey')
    if Card.objects.filter(sessionkey=sessionkey):
        card = Card.objects.filter(sessionkey=sessionkey)
        imagefield = 'input_image_' + str(input_no)
        response = list(card.values(imagefield))
        response[0]['sessionkey'] = sessionkey
        return JsonResponse(response[0])
    else:
        return JsonResponse({'status': 'session이 존재하지 않습니다.'})


@api_view(['GET'])
def passcard(request):
    sessionkey = request.headers.get('sessionkey')
    if Card.objects.filter(sessionkey=sessionkey):
        card = get_object_or_404(Card, sessionkey=sessionkey)
        serializer = CardSerializer(card)
        return JsonResponse(serializer.data)
    else:
        return JsonResponse({'status': 'session이 존재하지 않습니다.'})
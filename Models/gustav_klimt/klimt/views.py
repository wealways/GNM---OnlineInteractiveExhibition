from django.shortcuts import render

# django media 위치 및 저장
from django.conf import settings
import os
# JSON response
from django.http import HttpResponse, JsonResponse

# csrf 허용
from django.views.decorators.csrf import csrf_exempt
import json

# image 저장 form(유효성 검사용)
from .forms import UploadFileForm

# parser 설정 - data 접근하기
from rest_framework.decorators import api_view

# 비동기 -> 동기 | 동기 -> 비동기
from asgiref.sync import sync_to_async, async_to_sync
import asyncio

# Create your views here.

# (content)파일 저장
def handle_uploaded_file(image, sessionkey):
    save_dir = os.path.join(settings.MEDIA_ROOT, 'content', sessionkey)
    print(f'저장할 위치: {save_dir}')
    # 파일 저장할 디렉토리 만들어주기
    if not(os.path.isdir(save_dir)):
        os.makedirs(os.path.join(save_dir))
    with open(os.path.join(save_dir, image.name), 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)

    # 파일 저장 위치를 return
    return os.path.join(save_dir, image.name)

# @sync_to_async
@csrf_exempt
@api_view(['POST'])
# @async_to_sync
def style_transfer(request):
    form = UploadFileForm(request.POST, request.FILES)
    # 이미지 파일 체크
    print(f'들어온 이미지: {request.FILES["image"]}')
    sessionkey = request.headers['sessionkey']
    # request의 형식 유효성 검사
    if form.is_valid():
        # 이미지 저장 주소 저장
        content_img = handle_uploaded_file(request.FILES['image'], sessionkey=sessionkey)
        print(f'content 이미지 저장 완료 where:{content_img}')
    else:
        return JsonResponse({'status': '요청 파일 형식 오류'})
    
    return JsonResponse({'status': 'success'})
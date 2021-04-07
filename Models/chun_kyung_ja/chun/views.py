from django.shortcuts import render

# django media 위치 및 저장
from django.conf import settings
import os
import subprocess
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
# from asgiref.sync import sync_to_async, async_to_sync
# import asyncio

# multithreading
import threading

# 경로 추출 라이브러리
from pathlib import Path

# ai to BE 요청 보내기
import requests
# Create your views here.

# (content)파일 저장
def handle_uploaded_file(image, sessionkey):
    save_dir = os.path.join(settings.MEDIA_ROOT, 'content', sessionkey)
    print(f'저장할 위치: {save_dir}')
    # 파일 저장할 디렉토리 만들어주기
    if not(os.path.isdir(save_dir)):
        os.makedirs(os.path.join(save_dir))
    # 파일 저장하기 
    with open(os.path.join(save_dir, image.name), 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)

    # 파일 저장 위치를 return
    return os.path.join(save_dir, image.name)


# ouput (to backend)
def push_output(output, sessionkey):
    # request headers 설정
    # headers = {'Content-Type': 'multipart/form-data; boundary=<calculated when request is sent>; charset=utf-8'}
    # headers['sessionkey'] = sessionkey
    headers = {'sessionkey': sessionkey}
    # 전달 위치(backend - POST)
    # params
    imgtype = 'output'
    no = 3
    # 변환 완료된 이미지 파일 - read binary
    # with open(output, 'rb') as destination:
    #     image = destination.read()

    image = open(output, 'rb')

    output = { 'image': image }
    print(f'산출물: {output}')
    # 로컬용 API 주소
    # BASE_URL = f'http://127.0.0.1:8000/galleries/image/{imgtype}/{no}/'
    # 배포용 API 주소
    BASE_URL = f'https://j4c106.p.ssafy.io/api/galleries/image/{imgtype}/{no}/'
    print(f'요청 보내는 주소: {BASE_URL}')
    # 요청 보내기
    response = requests.post(BASE_URL, headers = headers, files = output)
    image.close()
    print(f'응답: {response}')
    # 요청 받아서 보여주기
    return response


def transfer(content_img: str, sessionkey: str):
    ai_dir = os.path.join(settings.BASE_DIR, 'chun', 'style_transfer')
    print(f'모델 저장 위치: {ai_dir}')

    # style image 위치
    style_img = os.path.join(settings.BASE_DIR, 'static', 'images', 'geuranadayi_market.jpg')
    # model dir 위치
    models = os.path.join(settings.BASE_DIR, 'chun', 'style_transfer')
    # vgg19
    vgg = os.path.join(models, 'vgg_normalised.pth')
    # decoder - chun
    decoder = os.path.join(models, 'chun_kyung_ja_160000.tar')
    # 저장할 위치(output)
    output_save_dir = os.path.join(settings.MEDIA_ROOT, 'output', sessionkey)
    print(f'저장할 위치: {output_save_dir}')
    # 파일 저장할 디렉토리 만들어주기
    if not(os.path.isdir(output_save_dir)):
        os.makedirs(os.path.join(output_save_dir))
    output = output_save_dir

    # 명령어 실행
    command_line = [
        'python',
        'test.py',
        '--content',
        content_img,
        '--style',
        style_img,
        '--vgg',
        vgg,
        '--decoder',
        decoder,
        '--output',
        output,
    ]
    print('수행할 명령어: ')
    print(command_line)
    subprocess.check_call(command_line, cwd=ai_dir)
    print(f'이미지 변환 완료 저장 위치: {output}')
    # 작업이 끝나면 다시 현재 위치로 돌려줘야한다
    print(f'현재 위치는 : {os.getcwd()}')
    # 파일 찾기 - 반환된 파일을 찾아서 백엔드 서버로 전달
    content_img_path = Path(content_img)

    print(f'inputfile명: {content_img_path.stem}')
    
    # 산출물 파일명
    output_image_file_name = f'chun_{content_img_path.stem}_output.jpg'
    print(f'output file: {output_image_file_name}')
    # 절대 주소
    output_image_uri = os.path.join(output, output_image_file_name)
    print(f'산출물 저장 위치 절대주소: {output_image_uri}')
    push_output(output_image_uri, sessionkey=sessionkey)


@csrf_exempt
# @api_view(['POST'])
def style_transfer(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # request의 형식 유효성 검사 및 세션 키 넘어오는지 확인
        if 'sessionkey' in request.headers and form.is_valid():
            # 이미지 파일 체크
            print(f'들어온 이미지: {request.FILES["image"]}')
            sessionkey = request.headers['sessionkey']
            # 이미지 저장 주소 저장
            content_img = handle_uploaded_file(request.FILES['image'], sessionkey=sessionkey)
            print(f'content 이미지 저장 완료 where:{content_img}')
            # 화풍변환 작동 - sessionkey 넘겨주기
            t = threading.Thread(target = transfer, args=[content_img, sessionkey])
            t.setDaemon(False)
            t.start()
            print(f'이미지 저장 끝 CPU개수: {os.cpu_count()}')
            
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': '요청 파일 형식 오류 또는 세션 키 미포함'})
        
    else:
        return JsonResponse({'status': f'잘못된 요청 방식입니다 { request.method }'})
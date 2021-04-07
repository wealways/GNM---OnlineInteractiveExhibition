## ai 모델 배포하기

[TOC]

#### 들어가기 앞서

**SGI(Server Gateway Interface)란**

- 미들웨어가 Java 기반 등으로 만들어졌기 때문에 Python 기반의 프레임워크는 중간에서 Java기반 미들웨어가 말하는 것을 해석해 줄 다른 미들웨어가 필요하게 되어짐

**WSGI(Web Server Gateway Interface)**

> 파이썬 스크립트(웹 어플리케이션)가 웹 서버와 통신하기 위한 인터페이스, like 프로토콜

하는 일

- 환경 변수가 바뀌면 타겟 URL에 따라 리퀘스트의 경로를 지정
- 같은 프로세스에서 여러 어플리케이션과 프레임 워크가 실행
- XSLT 스타일 시트르 적용하는 것과 같이 전처리

종류

> mod_wsgi, uwsgi, gunicorn, twisted.web, tornado ....



**ASGI(Asynchronous Server Gateway Interface)**

> single, synchronous callable 등의 문제 해결을 위해 사용하는 인터페이스

종류

> uvicorn, FastAPI ...



### 배포가 아닌 dev 환경으로 맞춰서 백그라운드에서 작동을 하고 있는 상태로 두게 되면 BE에서 통신이 가능할 것이다라는 생각에서 출발



#### 아나콘다(가상환경) 실행

```bash
# 가상환경 생성
$ conda create -n [env name] python=[version]
$ conda create -n style_transfer python=3.7.7

# 가상환경 목록 확인
$ conda info --envs

# 가상환경 활성화
$ conda activate style_transfer
or
$ source activate style_transfer
```



1. 백엔드 배포용

   ```python
   # galleries/views.py
   ...
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
   ...
   ```

2.  프론트엔드 배포용

   ```js
   // baseURL: 'http://localhost:8000',
     baseURL: 'http://j4c106.p.ssafy.io/api/',
   ```

3. ai 모델 배포용(linux용 requirements.txt)

   ```python
   # window OS
   # asgiref==3.3.1
   # certifi==2020.12.5
   # Django==3.1.7
   # djangorestframework==3.12.3
   # imageio==2.9.0
   # mkl-fft==1.3.0
   # mkl-random==1.1.1
   # mkl-service==2.3.0
   # numpy==1.17.2
   # olefile==0.46
   # opencv-python==4.4.0.46
   # Pillow==7.1.0
   # protobuf==3.9.1
   # pytz==2021.1
   # six==1.12.0
   # sqlparse==0.4.1
   # tensorboardX==1.8
   # torch==1.8.1
   # torchaudio==0.8.1
   # torchvision==0.9.1
   # tqdm==4.35.0
   # wincertstore==0.2
   
   # Linux
   asgiref==3.3.1
   certifi==2020.12.5
   chardet==4.0.0
   Django==3.1.7
   djangorestframework==3.12.3
   idna==2.10
   imageio==2.9.0
   numpy==1.17.2
   olefile==0.46
   opencv-python==4.4.0.46
   Pillow==7.1.0
   protobuf==3.9.1
   pytz==2021.1
   requests==2.25.1
   six==1.12.0
   sqlparse==0.4.1
   tensorboardX==1.8
   torch==1.8.1
   torchaudio==0.8.1
   torchvision==0.9.1
   tqdm==4.35.0
   typing-extensions==3.7.4.3
   urllib3==1.26.4
   wincertstore==0.2
   ```

   

#### 1. frontend

```bash
# 패키지 설치
$ npm i

# dist로 static 파일 모으기
$ npm run build
```



#### 2. Nginx

```bash
# nginx 설치 확인
nginx -v
```

 설정하기

```shell
sudo vim /etc/nginx/sites-enabled/default


# /etc/nginx/sites-enabled/default안에서 웹서버 루트 기존 설정은 주석처리, front를 build한 위치로 변경
server{
	listen 80; # 80번 포트에서 실행하겠으빈다.
	listen [::]:80;
	
	server_name j4c106.p.ssafy.io # ec2 퍼블릭 dns? 
	
	root /home/ubuntu/s04p23c106/frontend/dist; #프론트엔드를 배포한 위치
	index index.html index.htm;
	
	location / { # SPA 처음 페이지!
		try_files $uri $rui/ index.html 
	}
	
}


# 설정 변경 후 syntax 검사 필수
sudo nginx -t
# 설정 변경 후 Nginx 재시작
sudo service nginx restart
```




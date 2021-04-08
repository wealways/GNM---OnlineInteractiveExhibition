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
		try_files $uri $rui/ /index.html 
	}
	
}


# 설정 변경 후 syntax 검사 필수
sudo nginx -t
# 설정 변경 후 Nginx 재시작
sudo service nginx restart
```



#### 3. backend

```bash
# 가상환경 설정 및 활성화
$ python -m venv venv

$ source venv/bin/activate

# 필요 패키지 설치
$ pip install -r requirements.txt

# django 모델, static 설정
$ python maange.py makemigrations

$ python manage.py migrate

$ python manage.py collectstatic
```



#### 4. nohup

- nohup(nohangup)

  > hangup의 반대(중단) - 컴퓨터 프로그램이 충돌하거나 제대로 실행되지 않을 때 발생하는 상태
  >
  > 유닉스, 리눅스에서 daemon 형태로 파일을 실행시키는 프로그램
  >
  > 터미널 세션이 끊겨도 실행을 멈추지 않고 동작

- daemon

  > 사용자가 직접적으로 제어하지 않고 백그라운드에서 돌면서 여러 작업을 하는 프로그램을 뜻함

- 실행파일  권한

  > nohup으로 실행시킬 파일은 권한이 755이상이어야 한다
  >
  > ```
  > 파일권한 예시
  > -rwxr-xr-x
  > 
  > 이는 나눠서
  > 
  > rwx: 사용자권한(owner)
  > r-x: 그룹 권한
  > r-x: 다른 사용자(other) 권한
  > 
  > r: read(읽기)
  > w: write(쓰기)
  > x: execute(실행)
  > ```

  - 권한 변경

    ```bash
    # 소유자(사용자, user)에게 실행권한 부여
    $ chmod u+x file.txt
    
    # 그룹에 읽기, 쓰기, 실행 권한 부여
    $ chmod g+rwx file.txt
    
    # 그룹과 다른 사용자(other)에게 읽기 권한 부여
    $ chmod go+r file.txt
    
    # 숫자로 변경
    # r(4) w(2) x(1) - 2진수 bit 계산이기 때문
    
    # 사용자에게 모든 권한 그룹 및 다른 사용자에겐 읽기 권한만
    $ chmod 744 file.txt
    ```

    

- **AI 모델 백그라운드 실행**

  ```bash
  # 가상환경 활성화
  $ conda activate style_transfer
  or
  $ source activate style_transfer
  
  # (처음 pull 받았다면) migrate 실행
  $ python manage.py migrate
  
  # Django runserver에서 .reload를 위해 2개의 프로세스를 띄움
  $ nohup python ./manage.py runserver --noreload 0.0.0.0:[port 번호] &
  
  # 모네 - 8001, 클림트 - 8002, 천경자 - 8003 각자 manage.py 위치에서 실행
  
  # process 끄기
  $ kill PID(Process ID)
  ```

  [django runserver 2개 프로세스](https://m.blog.naver.com/crtstartup/222096808987)

  * (Update) 반쪽짜리 자동화

    ```
    shell script 파일로 배포되게끔
    만들기: $ vim start_ai.sh
    권한부여: $ chmod 755 start_ai.sh
    위치: ~/nohup/start_ai.sh
    
    #!/bin/bash << 아래 명령어는 bash 명령어로 수행하기
    
    shell script로 작성할 경우 sub shell로 작동하기 때문에 change directory 명령어를 수행한 다음 해당 위치에서 떠나게 됨 이를 극복하기 위해 bash 명령어로 해당 위치로 이동하는 alias 설정한 다음 이를 불러오는 방식으로 설계
    ```

    ```bash
    # .bashrc
    
    # style_transfer activate
    alias style_transfer='source activate style_transfer'
    
    # django manage.py directory
    alias monet='cd /home/ubuntu/test/Models/claude_monet'
    alias klimt='cd /home/ubuntu/test/Models/gustav_klimt'
    alias chun='cd /home/ubuntu/test/Models/chun_kyung_ja'
    
    # 절대 경로로 설정
    ```

    - shell script 내용

    ```shell
    #!/bin/bash
    
    style_transfer
    
    # 디렉토리 경로 이동
    monet
    # migrate
    python manage.py migrate
    # deploy
    nohup python ./manage.py runserver --noreload 0.0.0.0:8001 &
    
    # 디렉토리 경로 이동
    klimt
    # migrate
    python manage.py migrate
    # deploy
    nohup python ./manage.py runserver --noreload 0.0.0.0:8002 &
    
    # 디렉토리 경로 이동
    chun
    # migrate
    python manage.py migrate
    # deploy
    nohup python ./manage.py runserver --noreload 0.0.0.0:8003 &
    ```

    - 해당 쉘 스크립트 실행하기

      ```bash
      # 해당 위치 이동 후
      $ source start_ai.sh
      
# 현재 nohup이 자동 적용 안되는 문제 발생 - 하나의 프로세스만 적용됨
      # 3개로 나눠놓기 - start_[작가이름].sh 3개
      ```
      
      

#### 변경사항 적용해서 deploy

1. Nginx

   ```bash
   # 작동 중인 Nginx 종료
   $ nginx -s stop
   
   # 현재 연결 중인 커넥션 완료 후 종료
   $ nginx -s quit
   ```

2. gunicorn

   ```bash
   # vim 편집
   $ sudo vi /etc/systemd/system/gunicorn.service
   
   # /etc/systemd/system/gunicorn.service
   
   [Unit]
   Description=ssafy4 gj final-pjt
   After=network.target
   
   [Service]
   User=ubuntu
   Group=www-data
   WorkingDirectory=/home/ubuntu/**루트폴더명**
   ExecStart=/home/ubuntu/프로젝트명/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/ubuntu/**루트폴더명**/**루트폴더명**.sock **프로젝트폴더명**.wsgi:application
   
   [Install]
   WantedBy=multi-user.target
   
   # 작동 중인 gunicorn 종료
   $ pkill gunicorn
   ```

3. 적용하기

   1. gunicorn

   ```bash
   # gunicorn start
   $ sudo systemctl start gunicorn
   
   # gunicorn enable
   $ sudo systemctl enable gunicorn
   
   # gunicorn status 확인
   $ sudo systemctl status gunicorn
   
   # 에러 발생시 gunicorn.service 수정 후
   $ sudo systemctl daemon-reload
   $ sudo systemctl restart gunicorn
   ```

   2. Nginx

   ```bash
   # syntax 검사
   $ sudo nginx -t
   
   # nginx 실행
   $ sudo systemctl start nginx
   
   # 에러 발생시 nginx 수정 후
   $ sudo systemctl daemon-reload
   $ sudo systemctl restart gunicorn
   $ sudo systemctl restart nginx
   ```

   






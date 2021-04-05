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


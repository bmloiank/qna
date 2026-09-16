## django 프로젝트 생성하기
1. 디렉토리 생성하기
2. 가상환경 생성하기
3. 가상환경 활성화
4. django 패키지 설치
5. 패키지 requirements.txt 로 빼기
6. django 프로젝트 설정할것 

## django 프로젝트 초기 셋팅
1. template 설정 : html
```python
import os
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 프로젝트의 templates 폴더를 템플릿 경로로 등록
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        ...
    },
]
```

2. static 설정 : 정적자료를 넣는 곳
```python
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR
```

3. 타임존 설정 : 기본 UTC에서 서울시간대로 변경

```python
TIME_ZONE = 'Asia/Seoul'
USE_TZ = True
```



## 앱생성하기
1. 앱생성하기
django-admin startapp 앱이름

2. 앱등록
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 생성한 app이름,
]

```

3. urls.py 연결
config/urls.py
```python
from django.urls import path,include
app_name = "account"
urlpatterns = [
    path('account/',include('account.urls') )
]
```



## 장고의 유저
1. 장고 앱 migrate
```python
# 사용자정의 모델 생성할때 틀만들기
python manage.py makemigrations

# db에 테이블 만들기(변경사항 적용하기)
python manage.py migrate
```

2. db.sqlite3에서 tables 구경하기


3. superuser : 장고 최고관리자
python manage.py createsuperuser
- username : 외국식 id admin
- emailaddress : admin@서비스이름.com
- 비밀번호 1234 (원래안보여요.)


4. 장고어드민 로그인해보기
http://127.0.0.1:8000/admin/
관리자계정 admin/1234
일반계정 jjuhaaa/coding0831


# 로그인

1. 로그인페이지 구현
```python
from django.contrib.auth import views as auth_views
from django.urls import path,include
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='account/login.html'), name="login"),
]
```


2. 로그인하면 기본적으로 /account/profile
=> url 수정가능

```python
# 로그인 성공후 이동하는 URL
LOGIN_REDIRECT_URL = '/'
```

3. 로그아웃 버튼만들기
- 로그인 했는지를 판별

```python
# 유저가 인증이 되었는가? => 로그인 했냐?
{% if user.is_authenticated %}
    로그아웃버튼
{% else %}
    로그인버튼
{% endif %}
```





# QnA 앱 생성하기
1. 앱생성하기
```
django-admin startapp qna
```

2. 앱생성후에는 -> settings.py 앱등록
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'qna',
]


```

3. config/urls.py에 앱 url 추가하고 urls.py 생성하기
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', include('qna.urls'))
]

```




# 질문 CRUD
## url
```
목록페이지 /
상세페이지 /detail
작성페이지 /write
-> 생성 url  /create => 페이지는 없어. => 목록페이지로가
수정페이지 /edit
-> 수성 url /update
삭제 url /delete

```



# git 버전관리시스탬
## 1. 로컬(내컴퓨터) git 저장소를 생성하기
```
$ git init
```

## 2. .gitignore 파일 생성하기
- git이 특정파일은 무시할수 있도록 설정하는 팡리
- 내 컴퓨터 전용 환경설정을 제외하고 프로젝트에 관련된 내용만 적용시켜야한다.
https://www.toptal.com/developers/gitignore


## 3. 전체 선택
```
$ git add .
```

## 4. git 상태 확인
```
$ git status
```


## 5. 선택 해제
```
$ git reset .
$ git reset 디렉토리/파일명
```

## 6. 선택한 내용 저장하기
```
git commit -m "first init"
git commit

# 으로 되어있는건 작성이 안돼(주석)
맨위에는 제목(한글,영어 가능) - feat: 회원 로그인기능
(줄바꿈)
본문
- auth_user를 사용해서 슈퍼유저 생성하고 '/account/login' 로그인 기능 완성

:wq (write 후에 quit)
:q! (바로 강제종료)
:q (종료)

```
## 7. git 히스토리보기
```
git log
```

## 8. github 연결
```
git remote add 별칭 url

```
## 9. github 연결
```
git push origin main
```

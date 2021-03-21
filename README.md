# CEOS 13기 백엔드 django tutorial

### 폴더
#### polls - template : html 등 화면을 그리는 폴더

### 파일
#### urls.py - 뷰와 모델( / 함수)를 맵핑하는 파일
#### views.py - 기능 별 뷰를 모아두는 파일
#### models.py - 데이터베이스의 layout들 모아두는 파일 
#### admin.py - 관리자 생성 및 관리자 기능을 모아둔 파일
#### settings.py - 장고의 환경 설정을 세팅하는 파일

### 함수
#### views > vote - 선택된 내용을 +1 해주는 투표 함수 


1. Part 1
> 프로젝트 만들기
> > django-admin startproject mysite
>
> 서버 구동하기
> > python manage.py runserver
> 


2. Part 2
> SQLlite 사용하기
> * 테이블을 먼저 생성
> > $ python manage.py migrate
> 
> 모델 만들기
> >  __str__() 함수를 이용하여 모델의 return 및 기능을 정의
>
>어드민 만들기
> >  python manage.py createsuperuser

3. Part 3
> 뷰 추가하기
> > def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
> URL config
> * 해당하는 view로 라우팅 (url - view를 맵핑)
> 
> 정의 한 후 url 로 맵핑하기
> >     path('<int:question_id>/', views.detail, name='detail'),

4. Part 4
> views 에 함수 추가
> 
>  제너릭 뷰 생성 - ListView / DetailView
> * ListView - 개체 목록을 표시하는 제너릭 뷰
> * DetailView - "특정 개체에 대한" 세부 정보 페이지를 보여주는 제너릭 뷰


# CEOS 13th 김재연 django-tutorial
### 1st week study assignment review

#### Django request/response flow
1. URL config 에서 client request에 해당하는 view 결정
2. View 에서 로직대로 동작  
    2.1. DB CRUD가 필요하다면 model을 통해 DB로 접근  
    2.2. Template render
3. view에서 response to client

#### 1. URL config
- root app mysite 의 urls.py 파일의 url.urlpatterns를 참조하여 적절한 하위 앱으로 라우팅.  
  ex) path('polls/', include('polls.urls'))   ** polls/ 이후의 주소는 polls.urls의 url config에서 처리
- 하위 앱 polls 안에 urls.py 파일 생성, url 패턴에 맞게 view 할당.  
  ex) path('<int:pk>/results/', views.ResultsView.as_view(), name='results')  ** as_view()를 통해 view 클래스 인스턴스화, httpmethod 구분.
  
#### 2.  View
- 함수형 또는 클래스형으로 작성 가능.
- 클래스형으로 작성 시 generic view를 이용해 간편하게 작성.  
request에서 전달된 매개변수에 따라 db에서 데이터를 가져오고 template을 로드하는 일반적인 패턴 추상화.
각 generic view가 상속받은 attribute를 오버라이드 해서 사용. 

#### 2.1  Model
- 맨 처음 model 활성화를 위해 setting.py 에서 installed_apps에 앱 설치 알림.
- model 내용 변경. (클래스 - DB의 table, 멤버객체 - table의 column)  
- python manage.py makemigrations
- python manage.py migrate
  
+)  Foreign Key 관계에서 정참조는 바로 참조가능, 역참조는 [classname]_set 이용해서 참조.

#### 2.2 Template
- python 코드로부터 디자인 분리
- view에서 template을 렌더링할 때 context를 전달해서 python 객체를 template에 전달


# 과제1 README
<hr/>

###과제 내용 정리

>**[Part.1]**
> 
> * 프로젝트 생성
> <pre><code>$ django-admin startproject mysite</code></pre>
> * 개발 서버 동작
> <pre><code>$ python manage.py runserver</code></pre>
> * 설문조사 api 만들기
> <pre><code>python manage.py startapp polls</code></pre>
> * 첫 view 작성 (views.py)
> * polls.url을 urlcof에 매핑

>**[Part.2]**
> 
> * 데이터베이스 설치 (setting.py에 맞춰 필요한 table을 미리 만듦)
>   <pre><code>$ python manage.py migrate</code></pre>
> * 모델 만들기 (models.py : class Question, Choice)
> * settings.py에 PollsConfig 추가하여 앱을 프로젝트에 추가
> 모델 변경 사항 django에 전달
>   <pre><code>$ python manage.py makemigrations polls</code></pre>
> * 관리자 생성
>   <pre><code>$ python manage.py createsuperuser</code></pre>
> * admin에 poll app 추가

>**[Part.3]**
> 
> * 뷰 추가하기 (views.py : detail, results, vote)
> * 만들어진 뷰를 polls.urls에 매핑
> * templates를 통한 index view 업데이트
>   * templates 폴더 생성
>   * index.html
>   * views.py 에 index 뷰 업데이트
      <pre><code>from django.template import loader</code></pre>
>      <pre><code>from django.shortcuts import render</code></pre>
> * 404에러 일으키기 
>   <pre><code>from django.http import Http404</code></pre>
>   <pre><code>from django.shortcuts import get_object_or_404</code></pre>
> * {% url %} 태그를 이용하여 리팩토링
> * api 의 URLconf 에 app_name을 추가하여 API의 이름 공간 설정

>**[Part.4]**
> 
> * HTML \<form> 태그를 이용해 detail.html 수정
> * polls.views.py에 vote 함수 추가
> * rusults template 생성 및 view 작성 (results.html / view.py)
> * generic view 사용
>   * polls.urls 수정: \<question_id> ===> \<pk>
>   * views 수정: ListView / DetailView

<hr/>

## 과제를 통해 배운 내용
* 장고의 기본적인 작동 원리
* include() 함수 사용 방법과 원리
> Django가 함수 include()를 만나게 되면, URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include 된 URLconf로 전달합니다.
* model과 field
* settings.py에서 시간과 언어를 설정할 것   
(이번 과제에서는 Asia/Seoul & ko-KR 로 설정)
* migration: 테이블 생성 / 모델 변경사항 적용
* model에 \_\_str__ 쓰는 이유: 프롬프트에서 편하게 보임 / 장고 관리 사이트에서 사용
* context: 템플릿에서 쓰이는 변수명과 Python 객체를 연결하는 사전형 값
* render(): loader와 HttpResponse를 함축한 단축기능
* get_object_or_404() : get()과 raise Http404 함축한 단축기능

<hr/>

## 더 공부할 것
* path
* request / response
* generic view
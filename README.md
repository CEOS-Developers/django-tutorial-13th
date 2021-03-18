# CEOS 13th Back-End Django Tutorial

 * * *
## Week01 

###스터디(2021.03.14)
* 협업 툴 Git에 대한 간단한 설명
* MVC 디자인 패턴 및 Django의 MTV 패턴
* Django 개발 환경 설정 (설, 가상환경 등...)
* Pull request 연습 및 과제 설

###미션(2021.03.18)
* Django Tutorial Part.1 ~ Part. 4
* Pull request 하기
* readme.md 작성 및 발표하기

https://docs.djangoproject.com/ko/3.0/intro/tutorial01/

###Part.1

- Django 설치 확인

- mysite 프로젝트 생성 : 디렉토리 및 .py파일 생성 

- 개발 서버 확인 : 서버를 동작시킨 후 자신의 웹 브라우저를 통해 접속 

- 설문조사 앱 만들기 : 디렉토리 및 .py파일 생성 (프로젝트에는 여러 앱이 포함될 수 있다)

- 뷰 작성하기 : Index 뷰 작성 후 이와 연결된 URL을 만들기 위해 URLconf 생성 및 연결, include() 함수 사용

- 뷰 확인 : http://localhost:8000/polls/ 로 접속해 생성한 뷰 확인 

###Part.2

- 데이터 베이스 설치 : 기본으로 제공되는 SQLite 사용, 기본 어플리케이션에서 사용되는 테이블 생성 

- 모델 만들기 : Question 모델에는 question_text, pub_date / Choice 모델에는 question, choice_text, votes

- 모델 활성화 : 앱을 프로젝트에 포함시키기 위해 INSTALLED_APPS에 추가 및 모델에 사용되는 테이블 생성

- API 가지고 놀기 :  파이썬 쉘을 실행시켜 Question, Choice를 생성, 객체의 효과적 표현을 위해 __str__()메소드 추가 및 커스텀 메소드 추가

- 관리자 사이트 생성 : superuser 계정 생성한 후 관리자 사이트에 접속해 개발 서버 탐색 

- 관리 기능 탐색 :  관리자 사이트에 Question을 등록한 후, 관리자 사이트를 통해 Question 수 및 히스토리 확인


###Part.3

- 뷰 추가 : detail, results, vote 뷰 추가 및 URLconf로 URL 연결

- 뷰 빌딩 : HttpResponse 또는 Http404 발생

- 템플릿 생성 : 템플릿을 생성해서 페이지 디자인과 Index 뷰 분리 
  (이때 Django의 혼동 방지를 위해 polls/templates/polls/index.html에 생성), 
  템플릿에 뷰 업데이트(context 사용, HttpResponce 대신 render() 사용)

- 404 에러 일으키기 : 질문의 ID가 없는 경우 예외 발생 (try-except 대신 get_object_or_404() 사용)

- 템플릿 사용 :  Detail 뷰를 위한 템플릿 생성 및 업데이트, 하드코딩된 URL 제거

- URL의 이름공간 정하기 : URLconf에 namespace를 추가해서 앱들의 URL 구분


###Part.4

- 템플릿 수정 : Detail 뷰 템플릿에 form 요소 추가

- Vote 뷰 수정 : 선택하지 않은 경우 예외 발생, 트
  HttpResponse 대신 HttpResponseRedirect(), reverse()를 사용해
  설문을 한 뒤 결과 페이지로 리다이렉트 하도록 설정
  
- 제너릭 뷰 사용 : URLconf 수정, Django에서 제공하는 일반 뷰 사용

###미션을 마치면서...
Django를 이용한 백엔드 개발이 처음이었기 때문에, 
튜토리얼을 따라갔긴 하지만 각 코드가 어떤 동작과 기능을 하는지 완벽히 이해하지 못했다.
전체적인 설문조사 앱 제작 흐름을 보았을 때, 
모델을 만들어 데이터베이스에 연결시키고, 
이를 웹에서 볼 수 있도록 뷰를 만든 후 URL을 연결한다..라고 이해했는데, 확실하지는 않다.
튜토리얼 Part. 4를 마친 후에는, 웹 사이트에서 질문 목록, 투표, 결과 보기까지 할 수 있었다.

처음이라 낯설지만, 자주 접하면 익숙해질 거라 믿는다!! 

-2021.03.18 임해진-
* * *



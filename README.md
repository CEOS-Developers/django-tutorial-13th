# django-tutorial-13th
### 이수연 
### 2021. 3. 14 ~ 2021. 3. 21
* ## part1
 1. ### Include
    ~~~python
    path('polls/', include('polls.urls'))
    ~~~
    ##### 앞에 주소까지만 끊고 그 뒤부터는 include 된 URLconf로 넘겨줍니다
    ##### django에서는 여러개의 app이 독립적으로 존재하기때문에 최상위 URLconf에서 include를 이용해 app별로
    ##### url들을 정리해 줄 수 있을것같습니다

* ## part2
1. ### Models작성 및 수정 
     ##### models.py에 모델 작성 -> makemigrations -> migrate
     ##### 몇몇 field 클래스들은 필수 인수 필요
     ##### 예) CharField(max_length=200)
         
        
  2. ### Models 관계
     ~~~python
     class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
     ~~~
     ##### 위의 코드는 하나의 question마다 여러개의 choice가 있는 일대다 관계
     ##### django 다대다, 일대일, 일대다 관계 지원
    
  3. ### App 추가
     ##### mysite/settings.py에 INSTALLED_APP 리스트에 django app들을 꼈다 뺐다 할 수 있다.
 
  4. ### Shell
     ##### 모델 작성시에 아래와 같이 적어주면 shell에서 question모델을 조회할때 question_text를 보여준다
     ~~~python
        ...
         def __str__(self):
        return self.question_text
     ~~~
     ##### objects.filter 할 때 __를 이용해서 더 많은 옵션 가능 ( __exact , __lte... )
     ~~~python
     Question.objects.filter(question_text__startswith='What')
     ~~~
* ## part3
 1. ### Shortcut
    * ### render
        ~~~python
      return HttpResponse(template.render(context, request))
      ~~~
      ~~~python
      return render(request, 'polls/index.html', context)
      ~~~
      
    * ### get_object_or_404
        ~~~python
            try:
                question = Question.objects.get(pk=question_id)
            except Question.DoesNotExist:
                raise Http404("Question does not exist")
        ~~~
      
      ~~~python
        question = get_object_or_404(Question, pk=question_id)
        ~~~
2. ### Url name
    ##### polls/urls.py
    ~~~python
    app_name = polls
   ...
    path('<int:question_id>/', views.detail, name='detail'),
   ...
     ~~~
    ##### polls/index.html
   ~~~js
   "/polls/{{ question.id }}/" -> {% url 'polls:detail' question.id %}
    ~~~
      
      
* ## Part4
1. ### Form
   ##### name은 post요청보낼때 변수이름
     ~~~js
        <form action="{% url 'polls:vote' question.id %}" method="post">
        {% csrf_token %}
        {% for choice in question.choice_set.all %}
            <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
            ...
        {% endfor %}
            ...
        </form>
    ~~~
    ##### polls/views.py
    ##### POST[name]
     ~~~python
   ...
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
   ...
    ~~~
2. ### Reverse()
    ##### reverse안에서 '/polls/3/results/' 로 바뀐
    ~~~python
   return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
   ~~~

3. ### Generic
     * ### url
       ~~~python
       path('<int:pk>/', views.DetailView.as_view(), name='detail'),
       ~~~
     * ### ListView
       ~~~python
       class IndexView(generic.ListView):
            template_name = 'polls/index.html'
            context_object_name = 'latest_question_list'

        def get_queryset(self):
        """Return the last five published questions."""
            return Question.objects.order_by('-pub_date')[:5]
        ~~~
        ##### default template name : < app name >/< model name >_list.html
        ##### -> 변경하고싶다면 template_name = 'polls/index.html' 추가     
        ##### default context variable : < model >_list
        ##### -> 변경하고싶다면 context_object_name = 'latest_question_list'가 추가      
        #### get_qeuryset(self)는 요청마다 실행 -> 동적으로 쿼리 생성하기 좋다 
    
     * ### DetailView
       ~~~python
       class DetailView(generic.DetailView):
            model = Question
            template_name = 'polls/detail.html'
        ~~~
        ##### Question 중에 pk가 일치하는 모델 찾기
        ##### -> model = 'Question'추가 
       ##### default template name : < app name >/< model name >_detail.html
        ##### -> 변경하고싶다면 template_name = 'polls/detail.html' 추가
    
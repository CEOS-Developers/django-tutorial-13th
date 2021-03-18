# CEOS django-tutorial-13th 최예원
### 1st week study sum-up

---
##Part 1
- Basic settings
1. ```shell
    django-admin startproject mysite
    python manage.py startapp polls
    ```

2. Add 'polls.apps.PolsConfig' in INSTALLED_APPS (mysite/settings.py)

- Connecting urls 
```python
# polls/urls.py (Create)
urlpatterns = [
    path('', views.index, name='index'), # index function in views.py
]

# mysite/urls.py
urlpatterns = [
    path('polls/', include('polls.urls')), # Connect urls of apps with "include()"
    path('admin/', admin.site.urls),
]
```
---
##Part 2
- Creating models
```python
from django.db import models

# many-to-one relation
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text # show object in more effective way
```
- Migrate(whenever you change models)
```shell
python manage.py makemigrations polls # stores changes to your models
python manage.py migrate # apply changes to db
```
- Admin
```python
python manage.py createsuperuser  # Create admin

# Add models that have admin interface in polls.admin.py
from django.contrib import admin
from .models import Question
admin.site.register(Question)
```
---
##Part 3
- Add detail, results, vote with ids
```python
# polls/urls - urlpatterns
    path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
```
- Rendering
```html
<!--polls/templates/polls/index.html-->
<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
<!--after solving hard-coding problems-->
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
<!--after adding namespace of polls in urls-->
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```
```python
# polls/views.py
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) # shorten codes: try&except
    return render(request, 'polls/detail.html', {'question': question}) # shorten codes: loader
```
---
##Part4
- Form, Post, Redirection
```html
<form action="{% url 'polls:vote' question.id %}" method="post">
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
</form>
```
```python
def vote(request, question_id):
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    else:
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
```
- Generic views
```python
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
```
---
## New things I learned
1. 제네릭 뷰를 처음 써봤는데 너무 편했습니다. 조금 더 익숙해지는 연습을 해서 적절하게 잘 이용하면 좋을 것 같다는 생각이 들었습니다. 
   추가적으로 제네릭 뷰 이용할 때 url에서 question_id를 굳이 pk로 바꿔주는 이유가 궁금했는데,
   찾아보니 제네릭 뷰에서 기본값을 pk로 인식하기 때문이라고 합니다:)
2.  vote{{ choice.votes|pluralize }} 이 부분도 신기했습니다. 
   이걸 몰랐다면 if else 문을 사용해서 코드를 늘리고 있을 제 모습을 생각하니 반성하게 됩니다. 
   3. 제네릭 뷰에 대해,, - 처음 사용해보는 입장에서 개인적으로는
정말 편하긴 했지만 'context_object_name'부분을 이해하기까지 시간이 조금 걸렸습니다. 
      템플릿에 전달할 객체(Question)를 어디서 선언하는지 눈에 잘 안들어왔기 때문인 것 같은데,
      **그래서 언제 클래스형 뷰를 써야할 지, 되도록 많이 쓰는게 좋은 것인지, 개발자 분들이 실제로 개발할 때는 
      어떤 형식을 더 많이 사용하시는지 궁금합니다.**


import datetime

from django.db import models
from django.utils import timezone


# Question model
class Question(models.Model):
    objects = None
    # question_text: 질문 제목 char field
    question_text = models.CharField(max_length=200)
    # pub_date: 발행 시간 datetime field
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # 해당 Question model이 발행되고 하루가 지났는 지 확인
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Choice model
class Choice(models.Model):
    DoesNotExist = None
    # question: Choice - Question 연결
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice_text: 선택지 char field
    choice_text = models.CharField(max_length=200)
    # votes : 투표수 int field
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

from django.db import models

# Create your models here.
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # required arg
    pub_date = models.DateTimeField('date published')  # designate human-readable name

    def __str__(self):  # for obj ref
        return self.question_text

    def was_published_recently(self):  # custom method
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # each choice is related to a single question
    choice_text = models.CharField(max_length=200)# for obj ref
    votes = models.IntegerField(default=0)  # optional arg

    def __str__(self):  # for obj ref
        return self.choice_text

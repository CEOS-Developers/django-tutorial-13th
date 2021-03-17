from django.db import models

# Create your models here.

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # required arg
    pub_date = models.DateTimeField('date published')  # designate human-readable name


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # each choice is related to a single question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # optional arg

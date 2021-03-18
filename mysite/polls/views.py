# Create your views here.
# A view is a “type” of Web page in your Django application
# that generally serves a specific function and has a specific template.

from .models import Question
from django.http import Http404
from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import get_object_or_404, render

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # get list of 5 recent Qs
    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')  # loads the template and passes the context
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)  # shortcut for HttpResponse


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def detail(request, question_id):
    # question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)   # shortcut for Http404 exception
    # except Question.DoesNotExist:
    # raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
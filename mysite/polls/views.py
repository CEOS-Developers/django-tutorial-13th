# Create your views here.
# A view is a “type” of Web page in your Django application
# that generally serves a specific function and has a specific template.

from .models import Question, Choice
# from django.http import Http404
from django.http import HttpResponseRedirect
# from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

'''Used Generic View for more simple and easy programming'''

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]  # get list of 5 recent Qs
    # output = ', '.join([q.question_text for q in latest_question_list])
    # template = loader.get_template('polls/index.html')  # loads the template and passes the context
    context = {'latest_question_list': latest_question_list} 
'''


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


'''
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
'''


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # get id
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  # redirect to result page


'''
def detail(request, question_id):
    # question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id)   # shortcut for Http404 exception
    # except Question.DoesNotExist:
    # raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
'''


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

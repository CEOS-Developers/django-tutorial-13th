from django.http import  HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list' # default name = question_list 따라서 이름을 바꿔주기위한 코드

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'  # default name = question_detail.html


class ResultsView(generic.DetailView):
    model = Question # url에서 pk를 넘겨주기 때문에 Question모델에서 pk가 일치하는 것을 찾아서 question으로 반환
    template_name = 'polls/results.html' # default name = question_detail.html

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1 # vote값 올려주기
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) #'/polls/3/results/'

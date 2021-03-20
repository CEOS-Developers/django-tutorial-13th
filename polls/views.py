from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'polls/index.html'  # 템플릿 이름
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # 가장 최근 발행된 질문 5개 반환
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):  # redirect to polls/detail
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):  # redirect to polls/results
    model = Question
    template_name = 'polls/results.html'


# 선택한 설문의 ID를 받아 투표결과를 더하거나 오류를 발생시키는 함수
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # Question object 받지 못할 경우 404
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])  # 선택된 설문의 ID를 pk로 받음
    except (KeyError, Choice.DoesNotExist):  # request.POST['choice']가 없으면 KeyError 발생
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1  # 투표 된 선택지의 득표량 1 증가
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

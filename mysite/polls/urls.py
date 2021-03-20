# To get from a URL to a view, Django uses what are known as ‘URLconfs’.
# A URLconf maps URL patterns to views.

from django.urls import path

from . import views
app_name = 'polls'  # namespace
urlpatterns = [
    # ex: /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),  # Generic View

    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # Generic View
    # pk for primary key, used instead of question_id

    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # Generic View

    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/vote/', views.vote, name='vote'),  # Generic View
]
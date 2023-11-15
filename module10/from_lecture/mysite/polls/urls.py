from django.urls import path
from . import views

app_name = 'polls' # <a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a>
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/resluts/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

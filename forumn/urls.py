from django.urls import path
from .views import QuestionsView, AnswerView

urlpatterns = [
    path('',QuestionsView,name='questionspage'),
    path('answer/<int:pk>/',AnswerView,name='answers')
]
from django.urls import path
from .views import QuestionsView

urlpatterns = [
    path('',QuestionsView,name='questionspage')
]
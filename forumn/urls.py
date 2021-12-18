from django.urls import path
from .views import QuestionsView, AnswerView, UpvoteView

urlpatterns = [
    path('',QuestionsView,name='questionspage'),
    path('answer/<int:pk>/',AnswerView,name='answers'),
    path('upvotes/<int:pk>/', UpvoteView, name='upvote')
]
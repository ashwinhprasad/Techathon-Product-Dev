from django import forms
from .models import QuestionsModel, AnswerModel

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionsModel
        fields = ('title','description')

class AnswerForm(forms.ModelForm):
    class Meta:
        model = AnswerModel
        fields = ('answer',)
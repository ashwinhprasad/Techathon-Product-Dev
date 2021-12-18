from django import forms
from .models import QuestionsModel

class QuestionForm(forms.ModelForm):
    class Meta:
        model = QuestionsModel
        fields = ('title','description')
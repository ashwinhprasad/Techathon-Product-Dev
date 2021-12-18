from django.shortcuts import render
from .forms import QuestionForm
from .models import QuestionsModel

# Create your views here.
def QuestionsView(request):
    form = QuestionForm()
    questionInstances = QuestionsModel.objects.all()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            qm = QuestionsModel(**form.cleaned_data,asked_by=request.user)
            qm.save()
    return render(request,'forumn/questions.html',{
        'questionForm':form,
        'questionsList':questionInstances
    })

from django.shortcuts import render, redirect
from .forms import QuestionForm, AnswerForm
from .models import AnswerModel, QuestionsModel, HashtagModel
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def QuestionsView(request):
    form = QuestionForm()
    tag = request.GET.get('tag') or None
    if tag is not None:
        questionInstances = QuestionsModel.objects.filter(hashtagmodel=tag).order_by('-upvotes')[:10]
    else:
        questionInstances = QuestionsModel.objects.order_by('-upvotes')[:10]
    tags = HashtagModel.objects.all()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            qm = QuestionsModel(**form.cleaned_data,asked_by=request.user)
            qm.save()
            tag = HashtagModel.objects.get(tagname=request.POST['tag'])
            tag.question.add(qm)
            tag.save()
    return render(request,'forumn/questions.html',{
        'questionForm':form,
        'questionsList':questionInstances,
        'hashtags':tags
    })


@login_required(login_url='login')
def AnswerView(request,pk):
    question = QuestionsModel.objects.get(id=pk)
    form = AnswerForm()
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            ans = AnswerModel(**form.cleaned_data,question=question,answer_by=request.user)
            ans.save()
    answers = AnswerModel.objects.filter(question=question)
    return render(request,'forumn/answer.html',{
        'question':question,
        'AnswerForm':form,
        'answers':answers
    })

@login_required(login_url='login')
def UpvoteView(request,pk):
    question = QuestionsModel.objects.get(id=pk)
    question.upvotes += 1
    question.save()
    return redirect(f'/forum/answer/{pk}')
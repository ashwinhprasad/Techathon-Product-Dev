from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import UserModel, SkillModel, AchievementModel, CertificationsModel
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from events.models import AnnouncementsModel

# Create your views here.
def RegisterView(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = UserModel(email=form.cleaned_data['email'],
                    username=form.cleaned_data['username'],
                    phone=form.cleaned_data['phone'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        else:
            print(form.errors)
    context = { "form": form }
    return render(request,"user/register.html",context)


def LoginView(request):
    if request.method == "POST":
        user = authenticate(request,email=request.POST['email'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Email Id and Password does not Match")
            return redirect('login')
    return render(request,'user/login.html',{})


def UserLogoutView(request):
    logout(request)
    return redirect('login')


def HomeView(request):
    # announcement = AnnouncementsModel.objects.order_by('date')[0]
    return render(request,'home.html',{})


@login_required(login_url='login')
def ProfileView(request):
    user_obj = request.user
    skills = SkillModel.objects.filter(person=user_obj)
    achievements = AchievementModel.objects.filter(person=user_obj)
    certifications = CertificationsModel.objects.filter(person=user_obj)    
    return render(request,'user/profile.html',{'user':user_obj})
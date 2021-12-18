from django.urls import path
from .views import LoginView, RegisterView, HomeView

urlpatterns = [
    path('',RegisterView,name='register'),
    path('login/',LoginView,name='login')
]

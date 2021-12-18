from django.urls import path
from .views import LoginView, RegisterView, HomeView, UserLogoutView

urlpatterns = [
    path('',RegisterView,name='register'),
    path('login/',LoginView,name='login'),
    path('logout/',UserLogoutView,name='logout')
]

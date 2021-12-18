from django.contrib import admin
from django.urls import path, include
from user.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('forum/',include('forumn.urls')),
    path('home/',HomeView,name='home')
]

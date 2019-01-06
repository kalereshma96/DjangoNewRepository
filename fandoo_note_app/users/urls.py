from django.urls import path
from . import views

urlpatterns = [
     path('register/', views.register, name='register'),
     path('profile/', views.profile, name='profile'),
     path('home/', views.home, name='home'),
     path('login/', views.login1, name='login'),
]





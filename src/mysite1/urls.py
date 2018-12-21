from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from .views import home, register



urlpatterns = [

    url(r'^$', home),
    url(r'^register/', register),
]

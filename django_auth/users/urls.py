
from django.conf.urls import url
from django.urls import path

from .views import CreateUserAPIView,UserRetrieveUpdateAPIView
from . import views

urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    path('ot/',views.authenticate_user),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view())

]
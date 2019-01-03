from django.contrib import admin
from django.urls import path,include
from users.views import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path(r'^login/$', views.UserLoginAPIView.as_view(), name='login'),
    path(r'^api/auth/token/', obtain_jwt_token),
]
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url, include
from django.contrib import admin


api_urls = [
    url(r'^notes/', include('fundoonotes.urls', namespace='fundoonotes')),
    url(r'^users/', include('users.urls', namespace='users')),
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]

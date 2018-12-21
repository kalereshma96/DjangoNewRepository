from django.conf.urls import url
from . import views
from django.urls import reverse

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    # music/712/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),

]

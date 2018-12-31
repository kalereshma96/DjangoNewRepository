from django.conf.urls import url

from tokenapi.views import token
from tokenapi.views import token_new
from tokenapi.urls import url


urlpatterns = [
    url(r'^new.json$', token_new, name='api_token_new'),
    url(r'^(?P<token>.{24})/(?P<user>\d+).json$', token, name='api_token'),
    url(r'^token/', include('tokenapi.urls')),

]
from django.conf.urls import url
from fundoonotes.views import FundooNotesListCreateAPIView, FundooNotesDetailAPIView

app_name = 'fundoonotes'

urlpatterns = [
    url(r'^$', FundooNotesListCreateAPIView.as_view(), name="list"),
    url(r'^(?P<pk>[0-9]+)/$', FundooNotesDetailAPIView.as_view(), name="detail"),
]

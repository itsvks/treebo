from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from hotel import views

urlpatterns = [
    url(r'^deals/list/$', views.DealsList.as_view()),
    url(r'^deals/stats/$', views.DealsStats.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

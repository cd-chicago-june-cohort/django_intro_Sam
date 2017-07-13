from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^new/$', new),
    url(r'^create/$', create),
    url(r'^(?P<num>\d+)/$', show),
    url(r'^(?P<num>\d+)/edit/$', edit),
    url(r'delete/$', destroy),
]
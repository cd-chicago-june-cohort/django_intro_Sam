from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^new/$', new)
]
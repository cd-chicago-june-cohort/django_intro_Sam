from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^register/', register),
    url(r'^login/', login),
    url(r'^users/', users),
    url(r'^new$', new),
]
from django.conf.urls import url, include
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^users$', index),
    url(r'new$', new_user),
    url(r'create$', make_user),
    url(r'(?P<user_id>\d+)/edit$', edit_user),
    url(r'(?P<user_id>\d+)$', show_user),
    url(r'(?P<user_id>\d+)/destroy$', destroy),
    url(r'(?P<user_id>\d+)/update$', update),
]
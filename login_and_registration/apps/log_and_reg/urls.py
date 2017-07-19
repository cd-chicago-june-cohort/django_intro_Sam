from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'register$', register_user),
    url(r'login$', login_user),
    url(r'success$', success),
]

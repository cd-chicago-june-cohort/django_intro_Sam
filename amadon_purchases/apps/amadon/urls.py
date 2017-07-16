from django.conf.urls import url, include
from views import index, purchase, success

urlpatterns = [
    url(r'^$', index),
 #   url(r'^buy/(?P<parameter>d+)$', purchase),
    url(r'purchase$', purchase),
    url(r'success$', success)
]

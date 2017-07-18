from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^new$', add_course),
    url(r'remove/(?P<course_id>\d+)$', remove_page),
    url(r'destroy/(?P<course_id>\d+)$', delete_course)
]


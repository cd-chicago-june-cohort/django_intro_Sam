from django.conf.urls import url, include
from views import *

urlpatterns = [
    url(r'^$', index),
    url(r'register$', register_user),
    url(r'login$', login_user),
    url(r'home$', load_home),
    url(r'add$', show_add_book),
    url(r'create$', add_book),
    url(r'books/(?P<book_id>\d+)$', show_book),
    url(r'review/(?P<book_id>\d+)$', add_review),
    url(r'user/(?P<user_id>\d+)$', show_user),
    url(r'logout$', logout),
    url(r'delete/(?P<review_id>\d+)$', destroy),
]


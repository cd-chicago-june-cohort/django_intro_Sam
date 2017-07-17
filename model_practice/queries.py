import django
from apps.user_login.models import *

def sort_first_name():
    users = User.objects.order_by('first_name')
    for user in users:
        print user.first_name, user.last_name
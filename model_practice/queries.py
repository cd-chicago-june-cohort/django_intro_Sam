import django
from apps.user_login.models import *
from apps.dojo_ninjas.models import *

def sort_first_name():
    users = User.objects.order_by('first_name')
    for user in users:
        print user.first_name, user.last_name

def show_first_dojo():
    print Ninja.objects.first().dojo.name

def show_first_ninjas():
    first_doj = Dojo.objects.first()
    ninjas = Ninja.objects.filter(dojo=first_doj)
    for ninja in ninjas:
        print ninja.first_name, ninja.last_name



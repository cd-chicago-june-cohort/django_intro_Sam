import django
from apps.user_login.models import *
from apps.dojo_ninjas.models import *
from apps.book_authors.models import *


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

def show_books():
    books = Book.objects.filter(all_authors__id=4)
    for book in books:
        print book.name 

def show_authors():
    authors = Author.objects.filter(all_books__id=2)
    for author in authors:
        print author.first_name, author.last_name

def third_author_books():
    books = Book.objects.filter(all_authors__id=3)
    for book in books:
        print book.name 

def second_author_books():
    books = Book.objects.filter(all_authors__id=2)
    for book in books:
        print book.name 
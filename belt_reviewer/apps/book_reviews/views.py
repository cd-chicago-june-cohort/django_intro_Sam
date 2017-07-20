# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
import re

def index(request):
    if 'current_user_name' not in request.session:
        request.session['current_user_id'] = 0
    if 'action' not in request.session:
        request.session['action'] = ''
    if 'review_format' not in request.session:
        request.session['review_format'] = ''
    return render(request, 'book_reviews/index.html')

def register_user(request):
    if request.method == 'POST':
        errors = User.objects.register_validator(request.POST)
        request.session['action'] = 'register'
        if len(errors):
            for error, error_message in errors.iteritems():
                messages.error(request, error_message, extra_tags = error)
            return redirect('/')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            secret_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name = first_name, last_name = last_name, username = username, email = email, password = secret_password)
            new_user.save()
            request.session['current_user_id'] = new_user.id
            request.session['action'] = 'register success'
            return redirect('/')
    else:
        return redirect('/')

def login_user(request):
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        request.session['action'] = 'login'
        if len(errors):
            for error, error_message in errors.iteritems():
                messages.error(request, error_message, extra_tags = error)
            return redirect('/')
        else:
            email = request.POST['email']
            this_user = User.objects.get(email = email)
            this_user.save()
            request.session['current_user_id'] = this_user.id
            return redirect('/home') 
    else:
        return redirect('/')

def load_home(request):
    user = User.objects.get(id = request.session['current_user_id'])
    all_books = Book.objects.all().order_by('title')
    all_reviews = Review.objects.all()
    if len(all_reviews) < 3:
        reviews = all_reviews
    else:
        reviews = []
        for i in range(1,4):
            reviews.append(all_reviews[len(all_reviews) - i])
    request.session['review_format'] = 'home page format'
    context = {
        'reviews' : reviews,
        'user' : user,
        'books' : all_books
    }
    return render(request, 'book_reviews/welcome_wall.html', context)

def show_add_book(request):
    authors = Author.objects.all().order_by('last_name')
    context = {
        'authors': authors
    }
    return render(request, 'book_reviews/add_book.html', context)

def add_book(request):
    if request.method == 'POST':
        author_errors = Author.objects.author_validator(request.POST)
        book_errors = Book.objects.book_validator(request.POST)
        if len(author_errors):
            for error, error_message in author_errors.iteritems():
                messages.error(request, error_message, extra_tags = error)
            return redirect('/add')
        elif len(book_errors):
            for error, error_message in book_errors.iteritems():
                messages.error(request, error_message, extra_tags = error)
            return redirect('/add')
        else:
            new_author_name = request.POST['add_author_first'] + request.POST['add_author_last']
            if len(new_author_name):
                first_name = request.POST['add_author_first']
                last_name = request.POST['add_author_last']
                author = Author.objects.create(first_name = first_name, last_name = last_name)
                author.save()
            else:
                author_id = request.POST['author_list']
                author = Author.objects.get(id = author_id)
            book_name = request.POST['book_title']
            new_book = Book.objects.create(title = book_name, author = author)
            new_book.save()
            review_content = request.POST['review']
            stars = request.POST['stars']
            creator = User.objects.get(id=request.session['current_user_id'])
            new_review = Review.objects.create(content = review_content, stars = stars, creator = creator, book = new_book)
            new_review.save()
            book_id = str(new_book.id)
            return redirect('/books/' + book_id)
    else:
        return redirect('/add')

def show_book(request, book_id):
    book = Book.objects.get(id = book_id)
    author = book.author.first_name + ' ' + book.author.last_name
    request.session['review_format'] = 'book page format'
    reviews = Review.objects.filter(book__id = book_id).order_by('-created_at')
    context = {
        'book' : book,
        'author' : author,
        'reviews' : reviews
    }
    return render(request, 'book_reviews/show_book.html', context)

def add_review(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        review_content = request.POST['review']
        stars = request.POST['stars']
        creator = User.objects.get(id=request.session['current_user_id'])
        new_review = Review.objects.create(content = review_content, stars = stars, creator = creator, book = book)
        new_review.save()
        return redirect('/books/' + str(book_id))
    else:
        return redirect('/books/' + str(book_id))

def show_user(request, user_id):
    user = User.objects.get(id = user_id)
    user_reviews = Review.objects.filter(creator__id = user_id) 
    review_count = len(user_reviews)
    book_list = []
    book_exists_in_list = False
    for i in range(review_count):
        for j in range(len(book_list)):
            if user_reviews[i].book.title == book_list[j].title:
                book_exists_in_list = True
        if not book_exists_in_list:
            book_list.append(user_reviews[i].book)
        book_exists_in_list = False
    context = {
        'user' : user,
        'user_reviews' : user_reviews,
        'review_count' : review_count,
        'book_list' : book_list
    }
    return render(request, 'book_reviews/show_user.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def destroy(request, review_id):
    bye_review = Review.objects.get(id = review_id)
    book_id = bye_review.book.id 
    bye_review.delete()
    if request.session['review_format'] == 'book page format':
        return redirect('/books/' + str(book_id))
    else:
        return redirect('/home')


    

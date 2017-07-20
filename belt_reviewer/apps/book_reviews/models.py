# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect, HttpResponse
import bcrypt
import re

#LOGIN AND REGISTRATION MODELS
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class UserManager(models.Manager):
    def register_validator(self, user_input):
        errors = {}
        input_email = user_input['email']
        input_username = user_input['username']
        check_email_list = User.objects.filter(email = input_email)
        check_username = User.objects.filter(username = input_username)
        if len(check_email_list) <> 0:
            errors['existing'] = 'This email is already registered. Log in.'
        if len(check_email_list) <> 0:
            errors['username'] = 'This username is already taken. Try another.'
        if len(user_input['first_name']) < 2:
            errors['first_name'] = 'First name must be at least 2 characters long'
        if not (user_input['first_name']).isalpha() or not (user_input['last_name']).isalpha():
            errors['name_chars'] = 'Name fields can only contain letters of the alphabet'
        if len(user_input['last_name']) < 2:
            errors['last_name'] = 'Last name must be at least 2 characters long'
        if len(user_input['username']) < 2:
            errors['username_length'] = 'Username must be at least 2 characters long'
        if user_input['password'] != user_input['confirm_pw']:
            errors['confirm_pw'] = 'Passwords do not match. Try again.'
        if len(user_input['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long'
        if not EMAIL_REGEX.match(user_input['email']):
            errors['email'] = 'Email syntax not valid.'
        return errors 
    def login_validator(self, user_input):
        errors = {}
        input_email = user_input['email']
        input_password = user_input['password']
        check_user = User.objects.filter(email = input_email)
        if len(check_user) == 0:
            errors['not_registered'] = 'Email not in system. Register first before attempting login.'
        if not bcrypt.checkpw(input_password.encode(), check_user[0].password.encode()):
            errors['wrong_password'] = 'Incorrect password. Please try again.'
        return errors 

class AuthorManager(models.Manager):
    def author_validator(self, author_input):
        errors = {}
        input_author_first = author_input['add_author_first']
        input_author_last = author_input['add_author_last']
        author_check = Author.objects.filter(first_name = input_author_first).filter(last_name = input_author_last)
        if len(author_check) <> 0:
            errors['author_exists'] = 'This author is already in the system. Choose from dropdown menu.'
        return errors 

class BookManager(models.Manager):
    def book_validator(self, book_input):
        errors = {}
        input_title = book_input['book_title']
        if len(book_input['add_author_first']) + len(book_input['add_author_last']):
            return errors 
        else:
            input_author_id = book_input['author_list']
            book_check = Book.objects.filter(title = input_title).filter(author__id = input_author_id)
        if len(book_check) <> 0:
            errors['book_exists'] = 'This book is already in the system. Choose book from homepage menu or enter a new title.'
        return errors 

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255, unique=True)
    email = models.CharField(max_length = 255, unique = True)
    password = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add = True)
    objects = UserManager()

class Author(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = AuthorManager()

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(Author, related_name = "all_books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()

class Review(models.Model):
    content = models.TextField()
    stars = models.IntegerField(default = 0)
    creator = models.ForeignKey(User, related_name= 'reviews')
    book = models.ForeignKey(Book, related_name= 'reviews')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)






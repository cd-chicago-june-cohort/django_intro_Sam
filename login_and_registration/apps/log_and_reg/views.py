# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt
import re

def index(request):
    if 'current_user_name' not in request.session:
        request.session['current_user_name'] = ''
    if 'action' not in request.session:
        request.session['action'] = ''
    return render(request, 'log_and_reg/index.html')

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
            email = request.POST['email']
            password = request.POST['password']
            secret_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            new_user = User.objects.create(first_name = first_name, last_name = last_name, email = email, password = secret_password)
            new_user.save()
            request.session['current_user_name'] = new_user.first_name
            return redirect('/success')
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
            request.session['current_user_name'] = this_user.first_name
            return redirect('/success') 
    else:
        return redirect('/')

def success(request):
    context={}
    if request.session['action'] == 'register':
        context = {
            'greeting' : 'Welcome, ',
            'status' : 'You have successfully registered!',
            'button' : 'Return Home and Log In'
        }
    if request.session['action'] == 'login':
        context = {
            'greeting' : 'Welcome back, ',
            'status' : 'You have successfully logged in!',
            'button' : 'Log Out'
        }
    return render(request, 'log_and_reg/success.html', context)


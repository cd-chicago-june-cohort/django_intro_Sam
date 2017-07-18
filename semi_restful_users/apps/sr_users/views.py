# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
import datetime
from django.contrib import messages

def index(request):
    users = User.objects.all()
    user_dict = {
        'users' : users
    }
    return render(request, 'sr_users/index.html', user_dict)

def new_user(request):
    return render(request, 'sr_users/new.html')

def make_user(request):
    errors = User.objects.input_validator(request.POST)
    if len(errors):
        for field, error in errors.iteritems():
            messages.error(request, error, extra_tags = field)
        return redirect('/users')
    else:
        full_name = request.POST['first_name'] + ' ' + request.POST['last_name']
        email_address = request.POST['email']
        new_user = User.objects.create(name = full_name, email = email_address)
        new_user.save()
        return redirect('/users')

def edit_user(request, user_id):
    context = {
        'user_id' : user_id
    }
    return render(request, 'sr_users/edit.html', context)

def show_user(request, user_id):
    context = {
        'user' : User.objects.get(id=user_id),
        'user_id' : user_id
    }
    return render(request, 'sr_users/show_user.html', context)

def destroy(request, user_id):
    bye_user = User.objects.get(id=user_id)
    bye_user.delete()
    return redirect('/users')

def update(request, user_id):
    this_user = User.objects.get(id=user_id)
    this_user.name = request.POST['first_name'] + ' ' + request.POST['last_name']
    this_user.email = request.POST['email']
    this_user.save()
    return redirect('/users/' + user_id)





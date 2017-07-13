# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def register(request):
    return HttpResponse('placeholder for users to input a new user record')

def login(request):
    return HttpResponse('placeholder for users to submit a login request')

def users(request):
    return HttpResponse('placeholder to later display a list of users')

def new(request):
    return redirect('/register')



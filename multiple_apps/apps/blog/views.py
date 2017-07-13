# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse('placeholder to later display full list of blogs')

def new(request):
    return HttpResponse('placeholder to later display a new form to create a new blog')

def create(request):
    return redirect('/blog/')

def show(request, num):
    url_num = str(num)
    return HttpResponse('placeholder to later display info about blog ' + url_num)

def edit(request, num):
    url_num = str(num)
    return HttpResponse('page to edit blog ' + url_num)

def destroy(request):
    return redirect('/blog/')
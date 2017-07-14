# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'survey/index.html')

def submit(request):
    if request.method == 'POST':   
        request.session['input_name'] = request.POST['name']
        request.session['input_loc'] = request.POST['location']
        request.session['input_lang'] = request.POST['fav_lang']
        request.session['input_comment'] = request.POST['comment']
        return redirect('/success')
    else:
        return redirect('/')

def success(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    return render(request, 'survey/success.html')
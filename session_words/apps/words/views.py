# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime, localtime


def index(request):
    if 'word_data' not in request.session:
        request.session['word_data'] = []
    print request.session['word_data']
    return render(request, 'words/index.html')

def submit(request):
    if request.method == 'POST':
        check_font_size = 'normal_font'
        if 'font_size' in request.POST:
            check_font_size = 'big_font'
        print check_font_size
        data = request.session['word_data']
        data.append({
            'word' : request.POST['word'],
            'text_color' : request.POST['color'],
            'font_size' : check_font_size,
            'time' : strftime("%B %-d, %Y %I:%M %p", localtime())
        })
        request.session['word_data'] = data
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    request.session['word_data'] = []
    return redirect('/')

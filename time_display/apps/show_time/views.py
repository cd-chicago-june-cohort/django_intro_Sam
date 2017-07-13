# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        'time': strftime('%-I:%M %p', gmtime()),
        'date': strftime('%B %-d, %Y', gmtime())
    }
    print context
    return render(request, 'show_time/index.html', context)

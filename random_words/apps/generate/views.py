# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string


def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    context = {
        'count': request.session['counter'],
        'word':  get_random_string(length=14)
    }
    request.session['counter'] += 1
    return render(request, 'generate/index.html', context)




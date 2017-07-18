# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import *
import datetime
from django.contrib import messages

def index(request):
    course_list = Course.objects.all()
    context = {
        'courses' : course_list
    }
    return render(request, 'courses/index.html', context)

def add_course(request):
    errors = Course.objects.course_validator(request.POST)
    if len(errors):
        for error, error_message in errors.iteritems():
            messages.error(request, error_message, extra_tags = error)
        return redirect('/')
    else:
        name = request.POST['name']
        description = request.POST['desc']
        new_course = Course.objects.create(name = name, desc = description)
        new_course.save()
    return redirect('/')

def remove_page(request, course_id):
    this_course = Course.objects.get(id = course_id)
    context = {
        'course' : this_course
    }
    return render(request, 'courses/delete_check.html', context)

def delete_course(request, course_id):
    this_course = Course.objects.get(id = course_id)
    this_course.delete()
    return redirect('/')


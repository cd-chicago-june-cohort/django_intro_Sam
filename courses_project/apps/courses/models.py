# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect, HttpResponse


class CourseManager(models.Manager):
    def course_validator(self, course_info):
        errors = {}
        if len(course_info['name']) < 10:
            errors['name'] = 'Name of course must be longer than 10 characters'
        if len(course_info['desc']) < 15:
            errors['desc'] = 'Course description must be longer than 15 characters'
        return errors


class Course(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    objects = CourseManager()

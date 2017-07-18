# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render, redirect, HttpResponse

class UserManager(models.Manager):
    def input_validator(self, post_info):
        errors = {}
        if len(post_info['first_name']) < 2 or len(post_info['first_name']) > 30:
            errors['first_name'] = 'Name fields must be at least 2 and no more than 30 characters'
        if len(post_info['last_name']) < 2 or len(post_info['last_name']) > 30:
            errors['last_name'] = 'Name fields must be at least 2 and no more than 30 characters'
        if len(post_info['email']) < 5 or len(post_info['first_name']) > 40:
            errors['first_name'] = 'Email field must be at least 5 and no more than 40 characters'
        return errors

class User(models.Model):
    name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()





    





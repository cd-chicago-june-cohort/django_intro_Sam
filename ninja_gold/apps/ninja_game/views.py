# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import random
from time import strftime, localtime


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0;
    if 'activity_list' not in request.session:
        request.session['activity_list'] = []
    return render(request, 'ninja_game/index.html')

def process(request):
    if request.method=='POST':
        place = request.POST['place']
        if place == 'farm':
            new_gold = random.randint(10,20)
            display_class = 'farm_display'
        if place == 'cave':
            new_gold = random.randint(5,10)
            display_class = 'cave_display'
        if place == 'house':
            new_gold = random.randint(2,5)
            display_class = 'house_display'
        if place == 'casino':
            new_gold = random.randint(-50,50)
            display_class = 'casino_win'
        time = strftime("%m/%d/%Y %I:%M %p", localtime())
        if new_gold < 0:
            display_class = 'casino_lose'
            lost_gold = new_gold * -1
            activity_string = 'Lost ' + str(lost_gold) + ' golds from the casino...Better luck next time (' + time + ')'
        else:
            activity_string = 'Earned ' + str(new_gold) + ' golds from the ' + place + ' (' + time + ')'
        activity_display = {
            'string' : activity_string,
            'display_class' : display_class
        }
        request.session['activity_list'].insert(0, activity_display)
        old_gold = request.session['gold']
        request.session['gold'] = int(old_gold) + int(new_gold)
        return redirect('/')
    else:
        return redirect('/')
        

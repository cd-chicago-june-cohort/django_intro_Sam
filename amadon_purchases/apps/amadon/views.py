# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

def index(request):
    request.session['product_list'] = [
        {'product_id': 0, 'product_name': 'Blue Romper', 'price': 19.99},
        {'product_id': 1, 'product_name': 'Black Boots', 'price': 49.99},
        {'product_id': 2, 'product_name': 'Red Sunglasses', 'price': 129.99},
        {'product_id': 3, 'product_name': 'Floral Dress', 'price': 89.99},
    ]
    if 'purchase' not in request.session:
        request.session['purchase'] = {}
    return render(request, 'amadon/index.html')

def purchase(request):
    if request.method == 'POST': 
        this_product_id = int(request.POST['id'])
        this_product = request.session['product_list'][this_product_id]
        how_many = request.POST['quantity']
        purchase_data = {
            'quantity': how_many,
            'price' : this_product['price'],
            'total': int(how_many) * float(this_product['price'])
        }
        request.session['purchase'] = purchase_data
        if 'purchase_history' not in request.session:
            request.session['purchase_history'] = {
                'total_products' : 0,
                'total_spending' : 0
            }
        products = request.session['purchase_history']['total_products']
        spending = request.session['purchase_history']['total_spending']
        total_data = {
            'total_products' : int(products) + int(request.session['purchase']['quantity']),
            'total_spending' : int(spending) + float(request.session['purchase']['total'])
        }
        request.session['purchase_history'] = total_data
        return redirect('/success')
    else:
        return redirect('/')

def success(request):
    return render(request, 'amadon/success.html')
    
    
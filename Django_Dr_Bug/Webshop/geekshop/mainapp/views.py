# -*- coding: utf_8 -*-
from django.shortcuts import render
from .models import Product

def main(request):
    return render(request, 'mainapp/main.html', {'username': 'doctor bug', 'array': ['e', 'r', 'r', 'o', 'r']})

def products(request, pk=None):
    context = {'products': Product.objects.all()}
    return render(request, 'mainapp/products.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')
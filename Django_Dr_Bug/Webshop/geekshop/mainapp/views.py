# -*- coding: utf_8 -*-
from django.shortcuts import render
from .models import Product, ProductCategory
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = BASE_DIR + '\\mainapp\\db.json'
data_json = {}

with open(path, 'r', encoding = "utf-8") as f:
    data_json = json.load(f)

data_json.update({'products': Product.objects.all(), 'products_category': ProductCategory.objects.all()})

# Create your views here.
def main(request):
    return render(request, 'mainapp/main.html', {'username': 'doctor bug', 'array': ['e', 'r', 'r', 'o', 'r']})

def products(request):
    return render(request, 'mainapp/products.html', data_json )

def contacts(request):
    return render(request, 'mainapp/contacts.html')
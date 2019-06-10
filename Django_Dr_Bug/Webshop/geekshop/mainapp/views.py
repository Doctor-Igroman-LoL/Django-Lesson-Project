# -*- coding: utf_8 -*-
from django.shortcuts import render
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = BASE_DIR + '\\mainapp\\db.json'

with open(path, 'r') as f:
    DATA_JSON = json.load(f)

# Create your views here.
def main(request):
    return render(request, 'mainapp/main.html', {'username': 'doctor bug', 'array': ['e', 'r', 'r', 'o', 'r']})

def products(request):
    return render(request, 'mainapp/products.html', DATA_JSON)

'''
{'links_menu': [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'products', 'name': 'Продукты'},
        {'href': 'contacts', 'name': 'Контакты'},
    ]}
'''

def contacts(request):
    return render(request, 'mainapp/contacts.html')
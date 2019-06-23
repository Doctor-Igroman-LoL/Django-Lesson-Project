from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory

def main(request):
    return render(request, 'mainapp/main.html', {'username': 'doctor bug', 'array': ['e', 'r', 'r', 'o', 'r']})

def products(request, pk=None):
    products = Product.objects.all()
    basket = []
    if request.user:
        basket = request.user.basket.all()

    if pk:
        category = get_object_or_404(ProductCategory, pk=pk)
        products = products.filter(category=pk)
    context = {'products': products, 'categories': ProductCategory.objects.all(), 'basket': basket}
    return render(request, 'mainapp/products.html', context)

def contacts(request):
    return render(request, 'mainapp/contacts.html')
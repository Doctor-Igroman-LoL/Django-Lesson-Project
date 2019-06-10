from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'mainapp/main.html', {'username': 'doctor bug', 'array': ['e', 'r', 'r', 'o', 'r']})

def products(request):
    return render(request, 'mainapp/products.html', {'links_menu': [
        {'href': 'main', 'name': 'Главная'},
        {'href': 'products', 'name': 'Продукты'},
        {'href': 'contacts', 'name': 'Контакты'},
    ]})

def contacts(request):
    return render(request, 'mainapp/contacts.html')
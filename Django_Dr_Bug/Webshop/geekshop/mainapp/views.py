from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'mainapp/main.html', {'username': 'Doctor Bug'})

def products(request):
    return render(request, 'mainapp/products.html')

def contacts(request):
    return render(request, 'mainapp/contacts.html')
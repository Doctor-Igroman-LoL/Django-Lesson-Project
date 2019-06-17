from django.shortcuts import render
from django.views.generic.edit import UpdateView

def register(request):
    pass

def login(request):
    return render(request, 'authapp/login.html')

def logout(request):
    pass

class EditView(UpdateView):
    pass

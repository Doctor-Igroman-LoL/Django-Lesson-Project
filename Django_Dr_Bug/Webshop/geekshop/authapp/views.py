from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.urls import reverse

def register(request):
    pass

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
        return HttpResponseRedirect(reverse('main'))

    return render(request, 'authapp/login.html')

def logout(request):
    pass

class EditView(UpdateView):
    pass

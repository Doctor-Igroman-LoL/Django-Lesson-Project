from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.urls import reverse
from .forms import ShopUserRegisterForm

def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        register_form = ShopUserRegisterForm()
    context = {'form': register_form}
    return render(request, 'authapp/register.html', context)

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
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

class EditView(UpdateView):
    #model = ShopUser
    template_name = 'auth/register.html'
    #fields = 'username', 'email', 'avatar'

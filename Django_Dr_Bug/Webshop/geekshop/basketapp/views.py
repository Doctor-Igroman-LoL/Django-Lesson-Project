from django.shortcuts import HttpResponseRedirect

def add(request, product_pk=None):
    print('Добавить ', product_pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove(request, product_pk=None):
    print('Удалить ', product_pk)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
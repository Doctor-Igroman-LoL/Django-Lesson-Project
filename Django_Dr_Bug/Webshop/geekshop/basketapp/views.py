from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from basketapp.models import BasketSlot
from mainapp.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def basket(request):
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket.all()
    return render(request, 'basketapp/basket.html', {'basket_items': basket})

@login_required
def add(request, product_pk=None):
    product = get_object_or_404(Product, pk=product_pk)
    old_basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()

    if old_basket_slot:
        old_basket_slot.quantity += 1
        old_basket_slot.save()
    else:
        new_basket_slot = BasketSlot(user=request.user, product=product)
        new_basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def remove(request, product_pk=None):
    product = get_object_or_404(Product, pk=product_pk)
    basket_slot = BasketSlot.objects.filter(user=request.user, product=product).first()

    if basket_slot:
        if basket_slot.quantity == 1:
            basket_slot.delete()
        else:
            basket_slot.quantity -= 1
            basket_slot.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def edit(request, pk):
    print('Es')
    print(request.is_ajax())
    if request.is_ajax():
        basket_slot = get_object_or_404(BasketSlot, pk=pk)
        quantity = int(request.GET.get('quantity'))
        if quantity > 0:
            basket_slot.quantity = quantity
            basket_slot.save()
        else:
            basket_slot.delete()
        return HttpResponse('Ok')
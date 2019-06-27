from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from mainapp.models import Product, ProductCategory
#from .forms import ProductAdminForm

class ProductListView(ListView):
    model = Product
    template_name = 'adminapp/products.html'
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        if self.kwargs.get('category_pk'):
            queryset = queryset.filter(category=self.kwargs.get('category_pk'))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'Все продукты. Админка'
        context['categories'] = ProductCategory.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        title = Product.objects.get(pk=self.kwargs.get('pk')).name
        context['title'] = '{}. Админка'.format(title)
        return context
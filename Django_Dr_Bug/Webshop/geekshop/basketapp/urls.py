from django.urls import path

from basketapp.views import add, remove, basket

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='read'),
    path('add/<int:product_pk>/', add, name='add'),
    path('remove/<int:product_pk>/', remove, name='remove'),
]
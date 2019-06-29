from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.UserCreateView.as_view(), name='user_create'),
    path('users/read/', adminapp.UserListView.as_view(), name='users'),
    path('users/read/superuser/<int:superuser_pk>/', adminapp.UserListView.as_view(), name='users_by_superusers'),
    path('users/read/<int:pk>/', adminapp.UserDetailView.as_view(), name='user_read'),
    path('users/update/<int:pk>/', adminapp.UserUpdateView.as_view(), name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    # url(r'^categories/create/$', adminapp.category_create,name='category_create'),
    path('categories/read/', adminapp.CategoryListView.as_view(), name='category'),
    # url(r'^categories/read/$', adminapp.categories, name='categories'),
    # url(r'^categories/update/(?P<pk>\d+)/$', adminapp.category_update, name='category_update'),
    # url(r'^categories/delete/(?P<pk>\d+)/$', adminapp.category_delete, name='category_delete'),
    path('products/create/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/read/', adminapp.ProductListView.as_view(), name='products'),
    path('products/read/category/<int:category_pk>/', adminapp.ProductListView.as_view(), name='products_by_category'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
]
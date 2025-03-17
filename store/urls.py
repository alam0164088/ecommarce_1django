from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # "contract" নয়, "contact" হবে
    path('cart/', views.cart, name='cart'),
    path('search/', views.search, name='search'),
]
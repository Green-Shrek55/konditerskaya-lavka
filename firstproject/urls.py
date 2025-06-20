from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('map/', views.map_view, name='map'),
    path('products/categories/', views.product_categories, name='product_categories'),
    path('products/all/', views.all_products, name='all_products'),
    path('cart/', views.cart, name='cart'),
    path('', include('shop.urls')),
]

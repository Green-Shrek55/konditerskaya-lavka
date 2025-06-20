from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static




urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),

    # Корзина
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    # Заказ
    path('order/create/', views.create_order, name='create_order'),

    # Аутентификация
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
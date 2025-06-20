from django.contrib.auth import views as auth_views
from django.urls import path
from shop import views as shop_views  # если шаблон регистрации там

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', shop_views.register, name='register'),
    path('', include('shop.urls')),
    
]

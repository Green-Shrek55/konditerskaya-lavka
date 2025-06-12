from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('firstproject.urls')),  # Все маршруты — в приложении
    path('admin/', admin.site.urls),
]

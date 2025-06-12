from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def map_view(request):
    return render(request, 'map.html')

def product_categories(request):
    return render(request, 'product_categories.html')

def all_products(request):
    return render(request, 'all_products.html')

def cart(request):
    return render(request, 'cart.html')

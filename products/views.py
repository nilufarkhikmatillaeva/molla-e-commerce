from django.shortcuts import render
from products.models import Product, Category

def cart(request):
    return render(request, 'products/cart.html')

def checkout(request):
    return render(request, 'products/checkout.html')

def product_detail(request, pk):
    return render(request, 'products/product-sidebar.html')

def product(request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    return render(request, 'products/product-list.html', {
        'products': products,
        'categories': categories
    })

def wishlist(request):
    return render(request, 'products/wishlist.html')

from django.shortcuts import render

from products.models import Category


def shop_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/categories.html', {
        'categories': categories
    })
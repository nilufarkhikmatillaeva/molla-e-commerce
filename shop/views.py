from django.shortcuts import render


def shop_list(request):
    return render(request, 'shop/category.html')

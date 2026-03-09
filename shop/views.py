from django.shortcuts import render


def shop_list(request):
    return render(request, 'category.html')

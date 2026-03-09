from django.shortcuts import render


def login_view(request):
    return render(request, 'users/login.html')

def account_view(request):
    return render(request, 'users/dashboard.html')

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import LoginForm, RegisterForm
from django.contrib.auth import get_user_model
User = get_user_model()


def login_view(request):
    login_form = LoginForm()
    register_form = RegisterForm()

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'login':
            login_form =LoginForm(request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request,user)
                    text = f"Welcome back. {user.username}! "
                    messages.success(request, text)
                    return redirect('shared:home')
                else:
                    messages.error(request, 'Invalid username or password.')

        if form_type == 'register':
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                username = register_form.cleaned_data.get('username')
                email = register_form.cleaned_data.get('email')
                password = register_form.cleaned_data.get('password1')
                user = User.objects.create_user(username=username, email=email, password=password)
                if user:
                    text = f"Welcome, {user.username}! You are now logged in as {user.email}. "
                    messages.success(request, text)
                    return redirect('users:login')
                else:
                    messages.error(request, "Something went wrong. Please try again later.")
    return render(request, 'users/login.html', {
        'login_form': login_form,
        'register_form': register_form,
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('shared:home')

def account_view(request):
    return render(request, 'users/dashboard.html')

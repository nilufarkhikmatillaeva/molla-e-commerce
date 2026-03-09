from django.urls import path

from users.views import login_view, account_view

app_name = 'users'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('account/', account_view, name='account'),
]
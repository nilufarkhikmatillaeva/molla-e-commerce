from django.urls import path

from shop import views

app_name = 'shop'

urlpatterns = [
    path('category', views.shop_list, name='shop'),
]
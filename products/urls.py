from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('products/', views.product, name='list'),
    path('product/<int:pk>/', views.product_detail, name='product-detail'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
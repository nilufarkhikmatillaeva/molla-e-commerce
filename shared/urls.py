from django.urls import path
from shared import views

app_name = 'shared'

urlpatterns = [
    path('', views.home, name='home'),
     path('404/', views.page_404, name='404'),
    path('about/', views.about_us, name="about"),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    ]
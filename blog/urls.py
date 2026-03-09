from django.urls import path

from blog import views

app_name = 'blogs'

urlpatterns = [
    path('blog', views.blog_page_view, name='list'),
    path('blog-detail', views.blog_detail_view, name='detail'),
]
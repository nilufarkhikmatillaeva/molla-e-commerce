from django.shortcuts import render

from blog.models import Blog, BlogStatus, Category, Tag, PopularPosts


def blog_page_view(request):
    context = {
        'blogs': Blog.objects.filter(status=BlogStatus.PUBLISHED),
        'categories': Category.objects.filter(parent=None),
        'tags': Tag.objects.all(),
        'popular_posts': PopularPosts.objects.all()
    }

    return render(
        request, 'blogs/blog-listing.html',
        context
    )
    return render(request, 'blogs/blog-listing.html')
def blog_detail_view(request, pk):
    return render(request, 'blogs/blog-detail.html')
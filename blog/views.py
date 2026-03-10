from django.shortcuts import render

def blog_page_view(request):
    return render(request, 'blogs/blog-listing.html')
def blog_detail_view(request, pk):
    return render(request, 'blogs/blog-detail.html')
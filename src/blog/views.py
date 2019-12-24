from django.shortcuts import render

# Create your views here.
from .models import BlogPost


# obj = BlogPost.objects.get(id=2)
# view for viewing the BlogPost details
def blog_post_details_page(request):
    context = BlogPost.objects.get(id=1)
    return render(request, 'blog_post_details.html', {'context': context})

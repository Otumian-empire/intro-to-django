from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost


# obj = BlogPost.objects.get(id=2)
# view for viewing the BlogPost details
# def blog_post_details_page(request):
#     context = BlogPost.objects.get(id=1)
#     return render(request, 'blog_post_details.html', {'context': context})

# # making the view dynamic or building dynamic urls
# def blog_post_details_page(request, post_id):
#     context = get_object_or_404(BlogPost, id=post_id)
#     return render(request, 'blog_post_details.html', {'context': context})

# making the view dynamic or building dynamic urls using slugs instead of ids
def blog_post_details_page(request, slug):
    # queryset = BlogPost.objects.filter(slug=slug)
    # if queryset.count() == 0:
    #     raise Http404

    # context = queryset.first()
    context = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog_post_details.html', {'context': context})

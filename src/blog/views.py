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
# def blog_post_details_page(request, slug):
#     # queryset = BlogPost.objects.filter(slug=slug)
#     # if queryset.count() == 0:
#     #     raise Http404

#     # context = queryset.first()
#     context = get_object_or_404(BlogPost, slug=slug)
#     return render(request, 'blog_post_details.html', {'context': context})


# read all blog post
def blog_post_list_view(request):
    # list out objects
    # could be a search

    # query set
    # qs = BlogPost.objects.filter(title__icontains='e')
    qs = BlogPost.objects.all()
    template_name = 'blog_post_list.html'
    context = {'title': 'All Post', 'object_list': qs}
    return render(request, template_name, context=context)


# create
def blog_post_create_view(request):
    # create an object using a form
    template_name = 'blog_post_create.html'
    context = {'title': 'Create Post', 'form': None}
    return render(request, template_name, context=context)


# read
def blog_post_detail_view(request, slug):
    # one object or detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {'title': 'Post Details', 'object': obj}
    return render(request, template_name, context=context)


# update
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {'title': 'Update post', 'object': obj, 'form': None}
    return render(request, template_name, context=context)


# delete
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete.html'
    context = {'title': 'Delete Post', 'object': obj, 'form': None}
    return render(request, template_name, context=context)

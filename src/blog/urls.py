from django.urls import path

# blogs urls
from blog.views import (
    blog_post_list_view,
    blog_post_create_view,
    blog_post_delete_view,
    blog_post_detail_view,
    blog_post_update_view)

# blog url routing paths
urlpatterns = [
    path('', blog_post_list_view),
    path('blog-new/', blog_post_create_view),
    path('<str:slug>/', blog_post_detail_view),
    path('<str:slug>/edit/', blog_post_update_view),
]

from django.views.generic import ListView

from .base import PostBaseView


class PostListView(PostBaseView, ListView):
    template_name = "posts/home.html"
    context_object_name = "posts"

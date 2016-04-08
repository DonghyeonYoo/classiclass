from django.views.generic import ListView

from posts.models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = "posts"

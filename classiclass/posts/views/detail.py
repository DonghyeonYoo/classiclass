from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .base import PostBaseView


class PostDetailView(PostBaseView, LoginRequiredMixin, DetailView):
    template_name = "posts/detail.html"
    slug_field = 'hash_id'

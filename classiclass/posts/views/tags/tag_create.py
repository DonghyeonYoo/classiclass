from django.views.generic import View
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from posts.models import Post
from tags.models import Tag


class PostTagCreateView(View):

    def post(self, request, *args, **kwargs):
        # post 뽑아옴
        post = Post.objects.get(
            hash_id=self.kwargs.get('slug')
        )
        # tag 없으면 생성 있으면 가져옴
        tag, is_tag_created = Tag.objects.get_or_create(
            name=request.POST.get('name')
        )
        post.tag_set.add(tag)

        return redirect(
            reverse(
                "post",
                kwargs={
                    "slug": post.hash_id,
                }
            )
        )

from rest_framework.generics import RetrieveAPIView

from posts.serializers.post import PostDetailSerializer

from posts.models import Post


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    lookup_field = "hash_id"
    serializer_class = PostDetailSerializer

from rest_framework import serializers

from posts.models import Post

from .tag import TagModelSerializer


class PostDetailSerializer(serializers.ModelSerializer):
    tags = TagModelSerializer(source="tag_set.all", many=True)

    class Meta:
        model = Post
        fields = (
            'thumbnail_image',
            'content',
            'tags',
        )

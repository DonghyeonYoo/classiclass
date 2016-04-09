from rest_framework import serializers

from tags.models import Tag


class TagModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = (
            "name",
        )

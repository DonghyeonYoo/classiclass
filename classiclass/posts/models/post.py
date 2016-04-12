from django.db import models
from django.conf import settings

from tags.models import Tag


class Post(models.Model):
    hash_id = models.CharField(
        max_length=8,
        blank=True,
        null=True,
        unique=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
    )
    title = models.CharField(
        max_length=30,
    )
    thumbnail_image = models.ImageField(
        blank=True,
        null=True,
    )
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    tag_set = models.ManyToManyField(
        Tag,
        blank=True,
    )

    def init_hash_id(self):
        from classiclass.utils.hash_id import get_encoded_hash_id

        self.hash_id = get_encoded_hash_id(self)
        self.save()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse(
            "post",
            kwargs={
                "slug": self.hash_id,
            }
        )

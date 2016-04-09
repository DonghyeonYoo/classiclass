from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phonenumber = models.CharField(
        max_length=20,
    )
    majors = models.TextField()
    ages = models.TextField()

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        from django.shortcuts import redirect
        return redirect(
            reverse(
                "login",
                kwargs={
                    "login": self.login,
                }
            )
        )

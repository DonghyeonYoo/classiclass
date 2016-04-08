from django.views.generic import View

from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("home"))

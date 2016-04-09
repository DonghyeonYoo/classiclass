from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


class HomeView(View):
    def get(self, request):
        template_name = "home2.html"

        return render(
            request,
            template_name,
            context={},
        )

    def post(self, request):
        pass

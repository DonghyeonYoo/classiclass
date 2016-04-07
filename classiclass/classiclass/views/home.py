from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse


class HomeView(View):
    def get(self, requset):
        template_name = "home.html"

        retrun render(
            request,
            template_name,
            context={},
        )
    def post(self, request):
        pass

from django.contrib.auth import login, authenticate, get_user_model
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages


class SignupView(View):
    def get(self, request):
        template_name = "users/signup.html"

        return render(
            request,
            template_name,
            context={},
        )

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        phonenumber = request.POST.get("phonenumber")
        major = request.POST.get("majors")
        age = request.POST.get("ages")

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            phonenumber=phonenumber,
            majors=major,
            ages=age,
        )

        user = authenticate(
            username=username,
            password=password,
        )

        user.major = major
        user.save()

        user.age = age
        user.save()

        if user:
            login(request, user)
            messages.add_message(
                request,
                messages.SUCCESS,
                "고마워 가입해줘성",
            )
        return redirect(reverse("home"))

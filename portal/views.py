from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from portal.models import Game
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin)

# Create your views here.

@csrf_exempt
def login_view(request):
    username = request.POST.get("uname")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("add_game"))
    else:
        return render(request, "portal/login.html", {"message": ""})



@csrf_exempt
def register_view(request):
    username = request.POST["uname"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        return render(
            request,
            "portal/login.html",
            {"message": "User already registered"},
        )
    else:
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pnumber = request.POST["pnumber"]

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=fname,
            last_name=lname,
        )
        user.first_name = fname
        user.last_name = lname
        id = user.id

        login(request, user)
        permission = 3
        user.user_permissions.add(permission)
        user.save()

        return render(
            request,
            "portal/login.html",
            {"message": "User registered successfully"},
        )


def logout_view(request):
    Session.objects.all().delete()
    return render(request, "portal/login.html", {"message": "Logged out."})


@login_required(login_url="/login")
def TimerView(request):
    return render(request, "portal/timer.html")


def CreateGameView(request):
    if request.method == "GET":
        return render(request, "portal/game_form.html")
    if request.method == "POST":
        title = request.POST.get("title")
        Game.objects.create(title=title, user_id=request.user.id)
        return render(request, 'portal/timer.html')
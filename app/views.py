from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.templates import *
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import UserProfile, UserSettings
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


# @login_required(login_url='login')
def flappy_birb(request) -> HttpResponse:
    return render(request, "flappybirb.html")

# @login_required(login_url='login')
def snake(request) -> HttpResponse:
    return render(request, 'snake.html')

@login_required(login_url='login')
def space_invaders(request) -> HttpResponse:
    return render(request, "spaceinvaders.html")

@login_required(login_url='login')
def run(request) -> HttpResponse:
    return render(request, "run.html")

# @login_required(login_url='login')
def pacman(request) -> HttpResponse:
    return render(request,"pacman.html")

def main(request) -> HttpResponse:
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'main.html')

@unauthenticated_user
def login_page(request) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.info(request, "Username OR Password is incorrect!")

    return render(request, 'login.html')

@unauthenticated_user
def signup(request) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = LoginForm()
        if request.POST:
            form = LoginForm(request.POST)
            if form.is_valid():
                user = form.save()
                group = Group.objects.get(name='player')
                username = form.cleaned_data['username']
                user.groups.add(group)
                messages.success(request, f"{username}, Account Created!!")
                return redirect('login')
        context = {"form":form}
        return render(request, 'signup.html', context)

    
def logoutUser(request):
    logout(request)
    return redirect('login')

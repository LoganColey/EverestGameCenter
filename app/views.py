from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.templates import *
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User, Achievement
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def flappy_birb(request) -> HttpResponse:
    return render(request, "flappybirb.html")

@login_required(login_url='login')
def snake(request) -> HttpResponse:
    return render(request, 'snake.html')

@login_required(login_url='login')
def space_invaders(request) -> HttpResponse:
    return render(request, "spaceinvaders.html")

@login_required(login_url='login')
def run(request) -> HttpResponse:
    return render(request, "run.html")

@login_required(login_url='login')
def pacman(request) -> HttpResponse:
    return render(request,"pacman.html")

@unauthenticated_user
def main(request) -> HttpResponse:
    context = {
        "games" : {
            "Galaga" : "https://www.wikihow.com/images/thumb/0/03/Play-Galaga-Like-a-Pro-Step-1-Version-2.jpg/v4-460px-Play-Galaga-Like-a-Pro-Step-1-Version-2.jpg.webp",
            "Pac Man" : "http://cdn.cnn.com/cnnnext/dam/assets/200518114838-05-pac-man-40.jpg",
            "Snake" : "https://i.ytimg.com/vi/DekS8Pgb1qc/hqdefault.jpg",
            "Flappy Bird" : "https://i.pcmag.com/imagery/articles/01kOuDEoQIHlbRAiuAt54sq-1.fit_scale.size_1028x578.v1569485675.jpg",
            "Tetris" : "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Typical_Tetris_Game.svg/640px-Typical_Tetris_Game.svg.png",
            "Run" : "https://img.poki.com/cdn-cgi/image/quality=78,width=600,height=600,fit=cover,g=0.5x0.5,f=auto/9afd3b92ab41ffca7f368a8fcbd6d39a75894efe0edbc14cf1f067cf625e6678.png"
        }
    }
    return render(request, 'main.html', context)

@unauthenticated_user
def login_page(request) -> HttpResponse:
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = form.get('username')
        password = form.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            messages.info(request, "Username OR Password is incorrect!")

    context = {"form":form}
    return render(request, 'login.html', context)

@unauthenticated_user
def signup(request) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = RegisterForm()
        if request.POST:
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password2']
                user = User(username=username, password=password)
                user.save()
                messages.success(request, "Account Created!!")
                return redirect('login')
        context = {"form":form}
        return render(request, 'signup.html', context)

    
def logoutUser(request):
    logout(request)
    return redirect('login')
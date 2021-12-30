from django.shortcuts import render
from django.http import HttpResponse
from app.templates import *
# Create your views here.
def flappy_birb(request) -> HttpResponse:
    return render(request, "flappybirb.html")

def snake(request) -> HttpResponse:
    return render(request, 'snake.html')

def space_invaders(request) -> HttpResponse:
    return render(request, "spaceinvaders.html")

def run(request) -> HttpResponse:
    return render(request, "run.html")

def pacman(request) -> HttpResponse:
    return render(request,"pacman.html")

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
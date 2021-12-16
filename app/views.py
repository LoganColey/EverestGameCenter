from django.shortcuts import render
from django.http import HttpResponse
from app.templates import *
# Create your views here.
def flappy_birb(request) -> HttpResponse:
    return render(request, "flappybirb.html")

def snake(request) -> HttpResponse:
    return render(request, 'snake.html')

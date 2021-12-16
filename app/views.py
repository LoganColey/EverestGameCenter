from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def flappy_birb(request) -> HttpResponse:
    return render(request, 'flabbybirb.html')

def snake(request) -> HttpResponse:
    return render(request, 'snake.html')

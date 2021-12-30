
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snake/', views.snake, name="snake"),
    path('flappybirb/', views.flappy_birb),
    path('spaceinvaders/', views.space_invaders),
    path('run/', views.run),
    path('pacman/', views.pacman),
    path('', views.main)
]

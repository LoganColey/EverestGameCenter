
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snake/', views.snake, name="snake"),
    path('flappybirb/', views.flappy_birb, name="flappybirb"),
    path('spaceinvaders/', views.space_invaders, name="galaga"),
    path('run/', views.run, name="run"),
    path('', views.main, name="main"),
    path('login/', views.login_page, name="login"),
    path('signup/', views.signup, name="signup"),
    path('pacman/', views.pacman, name="pacman"),
    path("logout/", views.logoutUser, name="logout")
]


from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('snake/', views.snake, name="snake"),
    path('flappy_birb/', views.flappy_birb)
]

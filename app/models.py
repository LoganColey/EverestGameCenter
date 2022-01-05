from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, PROTECT


class UserProfile(models.Model):
    user = models.CharField(max_length=20, null=True)


    def __str__(self):
        return self.name
        
class UserSettings(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=CASCADE)
    volume = models.PositiveIntegerField()
    audio = models.URLField(max_length=200)
    mode = models.BooleanField(null=False)
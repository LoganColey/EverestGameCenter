from django.db import models

class UserProfile(models.Model):
    user = models.CharField(max_length=20, null=True)
    pac_high_score = models.PositiveIntegerField(null=True)
    snake_high_score = models.PositiveIntegerField(null=True)
    run_high_score = models.PositiveIntegerField(null=True)
    flap_high_score = models.PositiveIntegerField(null=True)
    galaga_high_score = models.PositiveIntegerField(null=True)
    numbers_high_score = models.PositiveIntegerField(null=True)
    tetris_high_score = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name
        
class Achievement(models.Model):
    game = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=100, null=True)
    user = models.ManyToManyField(UserProfile)
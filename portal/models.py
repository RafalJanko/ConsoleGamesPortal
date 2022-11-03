from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)


class GameMeasurePoint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    milestone = models.CharField(max_length=50)
    time = models.CharField(max_length=50)


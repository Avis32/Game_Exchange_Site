from django.contrib.auth.models import User
from django.db import models
from GameExchangeSite.GameLibrary.models import Game

# Create your models here.


class Offer(models.Model):
    game = models.ForeignKey(Game, related_name='offer', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='offers_made', on_delete=models.CASCADE)

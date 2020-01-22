from django.db import models
from django.contrib.auth.models import User


class Price(models.Model):
    base_price = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return str(self.price)


class Platform(models.Model):
    platform_type = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.platform_type


class Game(models.Model):

    name = models.TextField(max_length=256)
    added_date = models.DateField(auto_now=True, blank=False)
    location = models.TextField(blank=True)
    review = models.TextField(max_length=512)
    price = models.OneToOneField(Price, on_delete=models.CASCADE, related_name='game')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE, related_name='games')

    def __str__(self):
        return self.name

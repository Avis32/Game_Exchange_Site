from django.contrib import admin
from django.contrib.auth.models import User

from . import models


admin.site.register(models.Price)
admin.site.register(models.Game)
admin.site.register(models.Platform)

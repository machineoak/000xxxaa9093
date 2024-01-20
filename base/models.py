from django.db import models
from django.utils import timezone

class user(models.Model):
    los_hannah_username = models.CharField(max_length=50)
    los_hannah_email = models.EmailField(default=0)
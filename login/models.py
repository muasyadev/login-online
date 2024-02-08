from django.db import models
from django.contrib.auth.models import User

class credentials(models.Model):
    username = models.CharField(max_length = 1000)
    password = models.CharField(max_length = 1000)
    email = models.CharField(max_length = 1000)
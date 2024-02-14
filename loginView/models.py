from django.db import models

# Create your models here.

class credentials (models.Model):
    username = models.CharField(max_length = 500)
    password = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
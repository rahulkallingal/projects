from django.db import models

# Create your models here.


class UserRegistration(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
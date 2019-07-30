from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Comments(models.Model):
    username=models.CharField(max_length=5,default="Anonymous")
    content=models.TextField()

    def __str__(self):
        return self.username


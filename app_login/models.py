from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15)
    fullname = models.CharField(max_length=60)
    email = models.EmailField(max_length=60, unique=True)
    gender = models.CharField(max_length=15)
    registered_at = models.DateTimeField(auto_now_add=True)
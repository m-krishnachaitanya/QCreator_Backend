from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(primary_key = True, max_length = 50)
    password = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
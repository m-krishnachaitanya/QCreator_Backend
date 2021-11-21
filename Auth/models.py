from django.db import models

# Create your models here.
class Login(models.Model):
    userid = models.AutoField(primary_key=True, default=None)
    username = models.CharField(max_length = 50, unique=True)
    password = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
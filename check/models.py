from django.db import models

# Create your models here.
class User(models.Model):
    uphone=models.CharField(max_length=11)
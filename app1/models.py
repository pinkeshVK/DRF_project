from django.db import models


# Create your models here.

class FirstModel(models.Model):
    title = models.TextField()
    name = models.TextField(default="Name")
    date = models.DateField(auto_now_add=True)

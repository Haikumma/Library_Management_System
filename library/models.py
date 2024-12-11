from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

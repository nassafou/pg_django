#from django.db import models

# Create your models here.

# from django.db import models

from django.db import models

class Artist(models.Model):
     name = models.CharField(max_length=200, unique=True)


class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)


class Album(models.Model):
    reference = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    available = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    picture = models.URLField()


class Booking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    contacted = models.BooleanField(default=False)

#from django.db import models

# Create your models here.

# from django.db import models

from django.db import models

class Artist(models.Model):
     name = models.CharField(max_length=200, unique=True)



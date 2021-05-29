from django.db import models

# Create your models here.
class Counties(models.Model):
    county = models.CharField(max_length=100) 
    location = models.CharField( max_length=100)
from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    name = models.CharField(max_length=5000)
    number = models.IntegerField()
    country = models.CharField(max_length=100)
    
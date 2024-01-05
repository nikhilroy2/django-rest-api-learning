from django.db import models

import uuid
# Create your models here.
class PersonalInfo(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    name = models.CharField(max_length=5000)
    number = models.IntegerField()
    country = models.CharField(max_length=100)
    
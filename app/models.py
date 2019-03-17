from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length =30)
    dpic = models.CharField(max_length =30)
    contact_info = models.CharField(max_length =30)

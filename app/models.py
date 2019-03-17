from django.db import models

# Create your models here.
class project(models.Model):
    Title = models.CharField(max_length =30)
    project_img = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    link = models.CharField(max_length =30)
class profile(models.Model):
    name = models.CharField(max_length =30)
    dpic = models.CharField(max_length =30)
    contact_info = models.CharField(max_length =30)

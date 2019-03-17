from django.db import models

# Create your models here.
class profile(models.Model):
    u_name = models.CharField(max_length =30)
    dpic = models.CharField(max_length =30)
    contact_info = models.CharField(max_length =30)

    def __str__(self):
        return self.u_name


class project(models.Model):
    title = models.CharField(max_length =30)
    project_img = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    link = models.CharField(max_length =30)
    # editor = models.ForeignKey(profile)



    def __str__(self):
        return self.title

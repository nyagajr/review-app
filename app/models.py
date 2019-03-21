from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.TextField(blank = True)
    u_name = models.CharField(max_length =30)
    dpic = models.ImageField(default = 'default.jpg',upload_to = 'articles/')
    contact_info = models.CharField(max_length =30)

    def __str__(self):
        return self.u_name

    def save_profile(self):
        self.save()

    # def delete_profile(self):
    #     self.delete()



class project(models.Model):
    title = models.CharField(max_length =30)
    project_img = models.ImageField(upload_to = 'articles/')
    description = models.CharField(max_length =300)
    link = models.URLField(max_length =30)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save_project(self):
        self.save()

    @classmethod
    def search_by_title(cls,search_term):
        app = cls.objects.filter(title__icontains=search_term)
        return app

    # def delete_project(self):
    #     self.delete()

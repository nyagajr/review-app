from django.db import models

# Create your models here.
class profile(models.Model):
    u_name = models.CharField(max_length =30)
    dpic = models.ImageField(upload_to = 'articles/')
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
    description = models.CharField(max_length =30)
    link = models.CharField(max_length =30)
    editor = models.ForeignKey(profile)

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

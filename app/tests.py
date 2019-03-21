from django.test import TestCase
from .models import *



# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.junior=Profile(bio='hello',u_name = 'junior', dpic = 'lol.jpg',contact_info = 'mee')

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.junior,Profile))


    # Testing Save Method
    def test_save_method(self):
        self.junior.save_profile()
        editors = Profile.objects.all()
        self.assertTrue(len(editors) > 0)

    # def test_delete_method(self):
    #     self.junior.delete_profile()
    #     editors = profile.objects.all()
    #     self.assertTrue(len(editors) = 1)

class ProjectTestClass(TestCase):
    def setUp(self):
        self.junior=Project(title = 'junior', project_img = 'lol.jpg',description = 'mee', link = 'you.com', editor = User)

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.junior,Project))

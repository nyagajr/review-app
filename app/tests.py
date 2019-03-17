from django.test import TestCase
from .models import profile, project

# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.junior=profile(u_name = 'junior', dpic = 'lol.jpg',contact_info = 'mee')

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.junior,profile))

class ProjectTestClass(TestCase):
    def setUp(self):
        self.junior=project(title = 'junior', project_img = 'lol.jpg',description = 'mee', link = 'you.com')

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.junior,project))

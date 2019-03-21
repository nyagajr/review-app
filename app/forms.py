from django import forms
from .models import *

class UploadForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('link',)


# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = project
#         exclude = ('link',)
#
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = profile
#         exclude = ('link',)

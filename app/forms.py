from django import forms
from .models import *

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['by','rating']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rate
        exclude = ['rater','task','average']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['name', 'projects']

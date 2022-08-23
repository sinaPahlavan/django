from django.forms import ModelForm
from django import forms
from .models import Submission
class SubmissionForm(forms.Form):
    class Meta:
        model = Submission
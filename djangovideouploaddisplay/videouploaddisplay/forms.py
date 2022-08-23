from django.forms import ModelForm
from django import forms
from .models import Submission
class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ('name', 'phone', 'email')

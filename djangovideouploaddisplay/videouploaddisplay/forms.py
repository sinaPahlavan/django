from django.forms import ModelForm

from .models import Submission, Contact

class SubmissionForm(ModelForm):

    class Meta:

        model = Submission

        fields = ('name', 'email', 'title', 'location', 'description', 'videoSub')

class ContactForm(ModelForm):

    class Meta:

        model = Contact

        fields = '__all__'

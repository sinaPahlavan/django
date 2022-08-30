from django.db import models
# Create your models here.

class Submission(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    title = models.CharField(max_length=50, default='')
    location = models.CharField(max_length=50,default='')
    description = models.TextField(max_length=100, default='')
    #age = models.CharField(max)
    videoSub = models.FileField(upload_to='')


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=100, default='')


from django.db import models
# Create your models here.

class Submission(models.Model):
    name = models.CharField(max_Length=50)
    email = models.EmailField(max_Length=50)
    videoSub = models.FileField(max_Length=50)


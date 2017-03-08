from __future__ import unicode_literals

from django.db import models

# Create your models here.


class admission(models.Model):
	offered_by=models.CharField(max_length=150)
	qualifications=models.CharField(max_length=150)
	catagory=models.CharField(max_length=150)
	details=models.TextField()
	url=models.URLField()
	temp = models.URLField()
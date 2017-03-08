from __future__ import unicode_literals

from django.db import models

# Create your models here.
class job_application(models.Model):
	qualification=models.CharField(max_length=150)
	last_date=models.CharField(max_length=150)
	offered_by=models.CharField(max_length=150)
	details=models.TextField()
	url=models.URLField()
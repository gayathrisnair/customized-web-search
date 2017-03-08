from __future__ import unicode_literals

from django.db import models

# Create your models here.
class tender(models.Model):
  typei=models.CharField(max_length=140)
  category=models.CharField(max_length=140)
  opening_date=models.CharField(max_length=140)
  closing_date=models.CharField(max_length=140)
  details=models.TextField()
  url=models.URLField()
    



from __future__ import unicode_literals

from django.db import models

# Create your models here.
class scholarship (models.Model):

  offered_by=models.CharField(max_length=120)
  gender=models.CharField(max_length=150)
  qualification=models.CharField(max_length=150)
  catagory=models.CharField(max_length=150)
  annual_income=models.CharField(max_length=150)
  last_date=models.CharField(max_length=150)
  details=models.TextField()
  url=models.URLField()


def __str__(self):
  return self.offered_by
def __unicode__(self):
  return self.offered_by
def __str__(self):
  return self.qualification
def __unicode__(self):
  return self.catagory
def __str__(self):
  return self.catagory
def __unicode__(self):
  return self.gender
def __str__(self):
  return self.gender
def __unicode__(self):
  return self.annual_income
def __str__(self):
  return self.annual_income
def __unicode__(self):
  return self.annual_income
def __str__(self):
  return self.last_date
def __unicode__(self):
  return self.last_date
def __unicode__(self):
  return self.qualification     
  
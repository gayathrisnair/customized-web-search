from django.shortcuts import render
#from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse,HttpResponseRedirect
from .models import scholarship


# Create your views here.
def create(request):

 
 
  '''res=requests.get("http://disabilityaffairs.gov.in/content/page/national-fellowship-scheme-for-pwds.php")
  soup=bs4.BeautifulSoup(res.text,"html.parser")
  In=soup.find_all("div",class_="about-us-heading")

  s=''
  for p in In:
    s+=(p.text).encode('ASCII','ignore')

  p=scholarship(details=s)
  p.save()'''		


  return render(request,"scholarship.html")
		

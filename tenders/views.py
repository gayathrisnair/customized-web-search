from django.shortcuts import render

# Create your views here.

from bs4 import BeautifulSoup
import requests
from django.http import HttpResponse,HttpResponseRedirect



# Create your views here.
def home_page(request):

  '''res=requests.get("http://www.nhfdc.nic.in/scholarship_NF.html")
  soup=BeautifulSoup(res.text,"html.parser")
  In=soup.find_all("td")
  s=[]
  for a in In:
    s=s.append(a.text)

  
  

  
  instance=scholarship.object.create(details=s)'''

  return render(request,"tender.html")
		
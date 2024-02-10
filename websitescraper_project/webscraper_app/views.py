from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from . models import Link
# Create your views here.

def home(request):
    urls=requests.get("https://www.google.com")
    bs=BeautifulSoup(urls.text,'html.parser')
    address=[]
    for lnk in bs.find_all('a'):
        li_address=lnk.get('href')
        li_name=lnk.string
        Link.objects.create(address=li_address,stringname=li_name)
    data_values=Link.objects.all()

    return render(request,'home.html',{'data_values':data_values})




from pickle import GET

from django.shortcuts import render
from django.http import HttpResponse
from . models import Place
from . models import team

def demo(request):
    obj=Place.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{'result':obj, 'res':obj1})



#def operations(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #sum=x+y
    #diff=x-y
    #pdt=x*y
    #qt=x/y
    #return render(request,"Result.html",{'Sum':sum,'Difference':diff,'Product':pdt,'Quotient':qt})
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'index.html',{'name':'abhi'});

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    val3=val1+val2
    return render(request,'result.html',{'result':val3});


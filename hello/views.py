from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
   # return HttpResponse("Hello, world!")
    return render(request, "hello/index.html")

def sai(request):
    return HttpResponse("Hello, Sai!")

def ebo(request):
    return HttpResponse("<h1> Hello, Ebo! </h1>")

def greet(request, name):
    #return HttpResponse(f"<h1>Hello, {name.capitalize()}!</h1>")
    return render(request, "hello/greet.html",{"name":name.capitalize()})

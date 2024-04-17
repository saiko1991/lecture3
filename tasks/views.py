from django.shortcuts import render

# Create your views here.
task = ["foo","bar","baz"]

def index(request):
    return render(request, "tasks/index.html", { "tasks":task})

def add(request):
    return render(request, "tasks/add.html")
from django.shortcuts import render
from datetime import datetime
# Create your views here.
now = datetime.now()


def index(request):
    return render(request,"newyear/index.html",{"newyear": now.day ==1 and now.month == 1})
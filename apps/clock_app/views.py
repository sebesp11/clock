from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'clock_app/index.html', context)



 


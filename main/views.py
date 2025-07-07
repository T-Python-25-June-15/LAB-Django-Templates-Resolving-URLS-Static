from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.


def home_view(request:HttpRequest):
    context = {
        
    }
    return render(request, 'main/index.html', context)

def term_view(request:HttpRequest):
    context = {
        
    }
    return render(request, 'main/terms.html', context)
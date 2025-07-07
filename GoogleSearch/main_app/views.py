from django.shortcuts import render
from django.http import HttpRequest, HttpResponse 

# Create your views here.

def home(request):
    return render(request, 'home.html')  

def terms(request):
    return render(request, 'terms.html')  

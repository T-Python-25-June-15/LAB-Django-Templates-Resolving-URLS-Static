from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def home_view(request:HttpRequest):
    return render(request, "main/index.html")

def tearms_view(request:HttpRequest):
    return render(request, "main/terms.html")


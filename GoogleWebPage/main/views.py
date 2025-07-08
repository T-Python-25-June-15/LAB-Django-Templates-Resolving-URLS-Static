from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def land_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/land.html')

def terms_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/terms.html')
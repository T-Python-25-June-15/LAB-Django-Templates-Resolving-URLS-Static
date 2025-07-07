from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

# Create your views here.
def google_page(request:HttpRequest):
  return render(request,"main/index.html")

def google_terms_page(request:HttpRequest):
  return render(request,"main/terms.html")



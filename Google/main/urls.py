from django.urls import path
from . import views

urlpatterns = [
    path('', views.google_page, name="google_page"),
    path('terms/', views.google_terms_page, name="google_terms_page"),
]

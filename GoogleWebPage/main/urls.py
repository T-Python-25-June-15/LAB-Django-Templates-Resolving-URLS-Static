from django.urls import path 
from . import views

app_name = 'main'
urlpatterns = [
    path("", views.land_view, name='land_view'),
    path("terms/", views.terms_view, name='terms_view'),
]
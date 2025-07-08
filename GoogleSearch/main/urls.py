from django.urls import path
from . import views as main
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home'),
    path('terms/', views.terms_page, name='terms'),
]
from django.urls import path
from app_base import views

urlpatterns = [
    #inicio muebleria
    path('', views.inicio),
]
from django.urls import path
from . import views

urlpatterns = [
    path('weatherall/', views.weatherall),
    path('weatherlimit/<int:limit>/', views.weatherlimit),
    
]
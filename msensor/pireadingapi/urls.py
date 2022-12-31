from django.urls import path
from . import views

urlpatterns = [
    path('pireadingall/', views.pireadingall),
    path('pireadinglimit/<int:limit>/',views.pireadinglimit),
    path('instareadpi/', views.instareadpi),
]
#from curses import has_extended_color_support
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from weatherapi.models import * 


def index(response):
    return HttpResponse("WeatherAPI")

def weatherall(response):
    data = WeatherApi.objects.all()
    data = serializers.serialize('json', data)
    return HttpResponse(data)

def weatherlimit(response, limit):
    wealimit = WeatherApi.objects.all().order_by('-weather_api_id')[:limit]
    countdata = serializers.serialize('json',wealimit)
    return HttpResponse(countdata)
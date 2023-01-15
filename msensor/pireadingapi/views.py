from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from pireadingapi.models import * 
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def index(response):
    return HttpResponse("pireadingAPI")

def pireadingall(response):
    data = PiReading.objects.all().order_by('-pi_reading_id')
    allpidata = serializers.serialize('json', data)
    return HttpResponse(allpidata)

def pireadinglimit(response, limit):
    pirlimit = PiReading.objects.all().order_by('-pi_reading_id')[:limit]
    countdata = serializers.serialize('json',pirlimit)
    return HttpResponse(countdata)

def instareadpi(response):
    #reads moisture sensor at current time
    i2c = busio.I2C(board.SCL, board.SDA)
    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)
    # you can specify an I2C adress instead of the default 0x48, but should not have to if only the moisture sensor is plugged in
    # ads = ADS.ADS1115(i2c, address=0x49)
    # Create single-ended input on channel 0
    chan = AnalogIn(ads, ADS.P0)
    # Create differential input between channel 0 and 1
    # chan = AnalogIn(ads, ADS.P0, ADS.P1)   
    return HttpResponse(chan.voltage)

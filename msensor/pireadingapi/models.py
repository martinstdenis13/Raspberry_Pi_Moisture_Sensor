from django.db import models

class PiReading(models.Model):
    pi_reading_id = models.AutoField(primary_key=True)
    pi_reading_date = models.DateField(blank=True, null=True)
    pi_reading_time = models.TimeField(blank=True, null=True)
    pi_reading_val = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pi_reading'


class WeatherApi(models.Model):
    weather_api_id = models.AutoField(primary_key=True)
    weather_api_date = models.DateField(blank=True, null=True)
    temp1 = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temp_min = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temp_max = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    loc_1 = models.CharField(max_length=30, blank=True, null=True)
    weather_main = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weather_api'

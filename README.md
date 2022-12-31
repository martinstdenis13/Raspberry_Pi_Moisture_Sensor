<h1>Moisture Sensor 1.0</h1>

<h2>This repository provides the following back end services to pair with a front end:</h2>
    
<ul>
    <li>Python script to read weather from WeatherAPI (https://openweathermap.org/api), ingest into mariadb database</li>
    <li>Python script to read moisture sensor from Raspberry Pi, ingest into mariadb database</li>
    <ul>
        <li>Moisture Sensor used: <a href="https://www.amazon.com/Gikfun-Capacitive-Corrosion-Resistant-Detection/dp/B07H3P1NRM/ref=asc_df_B07H3P1NRM/?tag=hyprod-20&linkCode=df0&hvadid=278878233965&hvpos=&hvnetw=g&hvrand=11611484778761586923&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=200511&hvtargid=pla-524998080120&psc=1">Amazon link</a></li>
        <li>ADS used: <a href="https://www.amazon.com/HiLetgo-Converter-Programmable-Amplifier-Development/dp/B01DLHKMO2/ref=sr_1_4?crid=2HY1QQF828W57&keywords=analog+digital+signal+converter+raspberry+pi&qid=1669767228&sprefix=analog+digital+signal+converter+raspberry+pi%2Caps%2C65&sr=8-4">Amazon link</a></li>
        </ul>        
    <li>SQL statements to create MariaDB database, user, tables to store weather and pi moisture sensor data</li>
    <li>Django to serve WeatherAPI, Raspberry Pi data as JSON objects, insta-read of moisture sensor as float value</li>
</ul>

<h2>Steps:</h2>
<ol>
<li>Install raspian on raspberry pi</li>
<li>Install mariadb on raspberry pi</li>
<li>Use m_database_setup.sql file to create tables, users</li>
<li>Install mariadb connector Python library</li>

```
pip3 install mariadb
```

<li>Install Django</li>
    - configure REST API for mariadb with Django
    - install cors-headers
<li>Install ADS Python library: (https://github.com/adafruit/Adafruit_CircuitPython_ADS1x15)</li>

```
pip3 install adafruit-circuitpython-ads1x15 
```
<li>Install gunicorn</li>
<li>Clone this repo:</li>

```
git clone https://github.com/martinstdenis13/moisture_sensor.git
```

<li>Modify msensor/msensor/settings.py with your Django SECRET_KEY and chosen db password</li>
    - Django SECRET_KEY docs: https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-SECRET_KEY
<li>Request API key from WeatherAPI</li>
<li>Modify weaimport.py and moisinput.py with your WeatherAPI key and chosen db password</li>
<li>Set cron to run Python script(s) to ingest weather and moisture sensor readings as often as desired (note WeatherAPI has a limit of calls per-day)</li>
<li>Serve your API with Gunicorn</li>
</ol>

<h1>Output Objects</h1>
<p> WeatherAPI data and moisture sensor reading data will be extracted from the mariadb created and served as JSON objects. Examples of the JSON objects returned by Django are as follows:</p>
<ul>
<li>WeatherAPI:</li>

```
{"model": "weatherapi.weatherapi", "pk": 70, "fields": {"weather_api_date": "2022-11-17", "temp1": "43.23", "temp_min": "39.70", "temp_max": "45.79", "loc_1": "London", "weather_main": "Clouds"}}
```

<li>Pi Reading API:</li>

```
{"model": "pireadingapi.pireading", "pk": 23, "fields": {"pi_reading_date": "2022-11-19", "pi_reading_time": "19:37:05", "pi_reading_val": 2.3468}}
```

</ul>



<h1>Future 1.X version features:</h1>
<ul>
    <li>Generate monthly/weekly report</li>
    <li>Add text notes to pi moisture reading (watered, very dry day, vacation from Date-Date)</li>
</ul>
<h1>Future 2.X version features:</h1>
<ul>
    <li>Integrate camera to take image of moisture sensor envrionment</li>
    <li>More advanced data analytics (predictive watering-needed alerts)</li>
</ul>

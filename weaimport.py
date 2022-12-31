import requests
import json
from datetime import datetime
import mariadb
import logging
import sys

#requests get JSON
#parse relevant JSON values
#db connect
#insert into db
#close connection, exit

now = datetime.today()
tstamp = now.strftime("%d/%m/%Y %H:%M:%S")

#api key and location for weather, either input at command line or modify below
api_key = input('Enter API Key: ')
#api_key = '' 
#enter your location here
location = 'London'

def fetch_weather_data(location,api_key):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},US&APPID={}'.format(location, api_key)
    r = requests.get(url)
    return(r.json())

def kelvin_convert(temperature):
    # convert temps from K to F, round to 2 decimals
    return round((temperature - 273) * (9 / 5) + 32, 2)

def get_temps(json_data):
    #extract temp, temp_min, temp_max from json
    temp = json_data.get('main').get('temp')
    temp_min = json_data.get('main').get('temp_min')
    temp_max = json_data.get('main').get('temp_max')
    #may have humidity as separate return
    humidity = json_data.get('main').get('humidity')
    return kelvin_convert(temp), kelvin_convert(temp_min), kelvin_convert(temp_max)

def get_weather(json_data):
    #extract "weather" types so list not returned
    weather_list = json_data.get('weather')
    return weather_list[0].get('main')

def get_location(json_data):
    #extract location
    return json_data.get('name')

def dbweather_connect():
    #print timestamp
    print(now)
    logging.basicConfig(filename="weather_db_insert.log", level=logging.INFO)
    #Enter your DB password below and uncomment the password line
    try:
        conn = mariadb.connect(
            user = 'm_user',
            #password = 'PASSWORD',
            password = input('Enter DB Password: '),
            host = 'localhost',
            port=3306,
            database = 'm_database'
        )
        #log connection success
        logging.info(tstamp+' : Connection Success')
    except mariadb.error as e:
        print(f"Error connecting: {e}")
        sys.exit(1)
        #log error
        logging.info(tstamp+' : Error: {e}')
    return conn

#function to insert weatherapi data
def dbweather_insert(temp1,temp_min,temp_max,loc_1,weather_main):
    #open connection
    db_connect = dbweather_connect()
    cur = db_connect.cursor()
    #Insert data
    try:
        cur.execute(
            "INSERT INTO weather_api (weather_api_date,temp1,temp_min,temp_max,loc_1,weather_main) VALUES (?,?,?,?,?,?)",
            (now,temp1,temp_min,temp_max,loc_1,weather_main)
        )
    except mariadb.Error as e:
        print(f"Error: {e}")
        #log error
        logging.info(tstamp+' : Error: {e}')

    #commit changes
    db_connect.commit()
    logging.info(tstamp+' : db COMMIT')
    #close connection
    db_connect.close()

if __name__ == '__main__':
    print("ingesting weather api into db, "+tstamp)
    #fetch data
    json_data = fetch_weather_data(location,api_key)
    #parse out temps
    temps_list = get_temps(json_data)
    print(temps_list)
    #parse out weather
    weather_main = get_weather(json_data)
    print(weather_main)
    api_location = get_location(json_data)
    #connect to db, insert weatherapi data, commit, close db connection
    dbweather_insert(temps_list[0],temps_list[1],temps_list[2],api_location,weather_main)

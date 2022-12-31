import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import mariadb
from datetime import date, datetime
import logging
import sys

now = date.today()
tstamp = datetime.now().strftime("%H:%M:%S")
dstamp = now.strftime("%Y-%m-%d")

def getvoltageval():
    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)
    # you can specify an I2C adress instead of the default 0x48
    # ads = ADS.ADS1115(i2c, address=0x49)

    # Create single-ended input on channel 0
    chan = AnalogIn(ads, ADS.P0)

    # Create differential input between channel 0 and 1
    # chan = AnalogIn(ads, ADS.P0, ADS.P1)
    print(chan.value, chan.voltage)
    return (chan.voltage)

def dbpi_connect():
    #print timestamp
    print(now)
    logging.basicConfig(filename="pi_db_insert.log", level=logging.INFO)
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

def dbpi_insert(pi_reading_date, pi_reading_time, pi_reading_val):
    #open connection
    db_connect = dbpi_connect()
    cur = db_connect.cursor()
    #Insert data
    try:
        cur.execute(
            "INSERT INTO pi_reading (pi_reading_date,pi_reading_time, pi_reading_val) VALUES (?,?,?)",
            (pi_reading_date, pi_reading_time, pi_reading_val)
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
    print("ingesting pi data into db, "+tstamp)
    #fetch data
    reading_val = getvoltageval()
    #ingest into db
    dbpi_insert(dstamp, tstamp, reading_val)

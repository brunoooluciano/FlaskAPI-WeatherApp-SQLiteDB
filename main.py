from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, session
from datetime import datetime
from weather import Weather
from currentweather import CurrentWeatherData 
from Locals import Location
import schedule
import time

apiKey = open("apikey.txt", "r").read() 
        
db = CurrentWeatherData()

dbLocals = Location()
cities = dbLocals.getLocals()
dbLocals.close()


def job():
    for city in cities:
        Current = Weather(city, apiKey) 
        Current.getData() 
        db.currentWeatherDataInsert(
            Current.city, 
            Current.description, 
            Current.temp, Current.tempMin, 
            Current.tempMax, 
            Current.humidity
        )
schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
db.close()


    
    
#atual = db.selectDataByCity('Curitiba')
#print(atual)

 


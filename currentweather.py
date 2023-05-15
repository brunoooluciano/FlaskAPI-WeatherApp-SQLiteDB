from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime, asc, desc
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, session, query
from datetime import datetime
import json

Base = declarative_base()


class CurrentWeather(Base):
    
    __tablename__ = 'CurrentWeather'
    id = Column(Integer, primary_key=True)
    date = Column(Integer)
    city = Column(String(200))
    description = Column(String(200))    
    temp = Column(Float)
    tempMin = Column(Float)
    tempMax = Column(Float)
    humidity = Column(Float)
    
class CurrentWeatherData:
    def __init__(self):
        engine = create_engine('sqlite:///weatherData.db', echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    def currentWeatherDataInsert(self, city, description, temp, tempMin, tempMax, humidity):
        day = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        current = CurrentWeather(
            date=day,
            city=city, 
            description=description,
            temp=temp, 
            tempMin=tempMin, 
            tempMax=tempMax, 
            humidity=humidity
        )
        self.session.add(current)       
        self.session.commit()
    def selectDataByCity(self, city):
        self.city = city
        result = self.session.query(CurrentWeather.id, 
                                    CurrentWeather.date, 
                                    CurrentWeather.city, 
                                    CurrentWeather.description, 
                                    CurrentWeather.temp, 
                                    CurrentWeather.tempMin, 
                                    CurrentWeather.tempMax, 
                                    CurrentWeather.humidity).filter_by(city=city).order_by(asc(CurrentWeather.id)).all()
        weather_data = []
        for weather in result:
            weather_data.append(
                {
                    'date': weather.date, 
                    'city': weather.city,
                    'description': weather.description,
                    'temp': weather.temp,
                    'tempMin': weather.tempMin,
                    'tempMax': weather.tempMax,
                    'humidity': weather.humidity
                }
            )
        return weather_data    
    
    def selectDataByDate(self, date):
        self.date = date
        result = self.session.query(CurrentWeather.id, 
                                    CurrentWeather.date, 
                                    CurrentWeather.city, 
                                    CurrentWeather.description, 
                                    CurrentWeather.temp, 
                                    CurrentWeather.tempMin, 
                                    CurrentWeather.tempMax, 
                                    CurrentWeather.humidity).filter(CurrentWeather.date.like(f'%{date}%')).order_by(asc(CurrentWeather.id)).all()
        weather_data = []
        for weather in result:
            weather_data.append(
                {
                    'date': weather.date, 
                    'city': weather.city,
                    'description': weather.description,
                    'temp': weather.temp,
                    'tempMin': weather.tempMin,
                    'tempMax': weather.tempMax,
                    'humidity': weather.humidity
                }
            )
        return weather_data 
    
     
    def close(self):
        self.session.close()
        
        
#engine = create_engine('sqlite:///weatherData.db', echo=True)

#Base.metadata.create_all(engine)

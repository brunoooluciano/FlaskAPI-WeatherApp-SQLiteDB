from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, session
from datetime import datetime
from weather import Weather

Base = declarative_base()

class Locals(Base):
    __tablename__ = 'Locals'
    id = Column(Integer, primary_key=True)
    city = Column(String(200))
    state = Column(String(200))    
    country = Column(String(200))

class CurrentWeather(Base):
    
    __tablename__ = 'CurrentWeather'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.now)
    city = Column(String(200))
    description = Column(String(200))    
    temp = Column(Float)
    tempMin = Column(Float)
    tempMax = Column(Float)
    humidity = Column(Float)
    
    
class Location:
    def __init__(self):
        engine = create_engine('sqlite:///weatherData.db', echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    def getLocals(self):
        cityList = []
        query = self.session.query(Locals.city).all()
        for city in query:
            cityName = city[0]
            cityList.append(cityName)
            db.close()
        return cityList
class CurrentWeatherData:
    def __init__(self):
        engine = create_engine('sqlite:///weatherData.db', echo=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()
    def currentWeatherDataInsert(self, city, description, temp, tempMin, tempMax, humidity):
        current = CurrentWeather(
            date=datetime.now(),
            city=city, 
            description=description,
            temp=temp, 
            tempMin=tempMin, 
            tempMax=tempMax, 
            humidity=humidity
        )
        self.session.add(current)       
        self.session.commit()
        
    def close(self):
        self.session.close()
        
        


apiKey = open("apikey.txt", "r").read() 
        
db = CurrentWeatherData()
dbLocals = Location()
cities = dbLocals.getLocals()

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
db.close()




from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, session
from datetime import datetime
from currentweather import CurrentWeatherData

Base = declarative_base()

class Locals(Base):
    __tablename__ = 'Locals'
    id = Column(Integer, primary_key=True)
    city = Column(String(200))
    state = Column(String(200))    
    country = Column(String(200))
    
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
        return cityList
    def close(self):
        self.session.close()

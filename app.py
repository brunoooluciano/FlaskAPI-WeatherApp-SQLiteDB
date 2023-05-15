from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, session, query
from datetime import datetime
from currentweather import CurrentWeatherData
import json


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weatherData.db'
db = SQLAlchemy(app)
cwd = CurrentWeatherData()

@app.route('/weatherData/filterby/city/<city>', methods=['GET'])
def get_weather_by_city(city):
    results =  cwd.selectDataByCity(city)   
    return jsonify(results)
@app.route('/weatherData/filterby/date/<date>', methods=['GET'])
def get_weather_by_date(date):
    results =  cwd.selectDataByDate(date)   
    return jsonify(results)
if __name__ == '__main__':
    app.run()
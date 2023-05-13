from flask import Flask, render_template, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import pyodbc 
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc:///:@BRUNOPC/WEATHERDATA?driver=SQL SERVER'pip 

db = SQLAlchemy(app)

locals = db.Locals("locals", db.metadata, autoload=True, autoload_with=db.engine)

"locals": db.session.query(locals).all()
results = jsonify({"locals": db.session.query(locals).all()})

print(results)

@app.route("/")
def hello(name=None):
    return render_template('index.html', name=name)
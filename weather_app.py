# Dependencies and boilerplate
from flask import Flask, jsonify

import pandas as pd
import matplotlib.pyplot as plt

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.automap import automap_base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import and_, or_
from sqlalchemy import func

# Create an engine connecting to the SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# Create a session
session = Session(bind = engine)

# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)
# Print all of the classes mapped to the Base
Base.classes.keys()

# Assign the measurement class to a variable called `Measurement`
Measurement = Base.classes.measurement

# Assign the stations class to a variable called `Stations`
Stations = Base.classes.stations

# Create an app, being sure to pass __name__
app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

# Precipitation
@app.route("/api/v1.0/precipitation")
def precip():
    
    #Query for the dates and temperature observations from the last year.
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2017-01-01')
    #Convert the query results to a Dictionary using date as the key and tobs as the value.
    data = {}

    # populate dict with rows from results
    for row in results:
        data[str(row.date)] = [row.prcp]
    
    #Return the json representation of your dictionary.
    return jsonify(data)

# Stations
@app.route("/api/v1.0/stations")
def stns():
    #Return a json list of stations from the dataset.
    results = session.query(Measurement.station).distinct()
    count = 0
    for row in results:
        count +=1
    return f'There are {count} unique stations'

# Tobs
@app.route("/api/v1.0/tobs")
def unique_stations():
    #Return a json list of stations from the dataset.
    #Query for the dates and temperature observations from the last year.
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= '2017-01-01')
    #Convert the query results to a Dictionary using date as the key and tobs as the value.
    data = {}

    # populate dict with rows from results
    for row in results:
        data[str(row.date)] = [row.tobs]
    
    #Return the json representation of your dictionary.
    return jsonify(data)

# start
@app.route("/api/v1.0/<start>")
def strt(start):
    # Return a json list of the minimum temperature, the average temperature, and 
    # the max temperature for a given start
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()

    return jsonify(result)

@app.route("/api/v1.0/<start>/<end>")
def strt_end(start, end):
    # When given the start and the end date, calculate the TMIN, TAVG, and TMAX for 
    # dates between the start and end date inclusive.
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
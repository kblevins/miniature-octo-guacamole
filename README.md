# What's the weather?
![umbrellas](umbrellas.jpeg)

API for analysis of Hawaiian climate data. Uses Python & SQLAlchemy to organize & analyze climate data.



##Python analyses

precip analysis - retrieve last 12 months of precip data & plot results

station analysis - identify the total number of stations & the most active stations, then retrieves 12 months of temperature data and plots results

temperature analysis - calculates min, avg, and max temperatures for a specified date range & plots it



##API - Flask routes

* `/api/v1.0/precipitation`

  * Query for the dates and temperature observations from the last year.

  * Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.

  * Return the json representation of your dictionary.

* `/api/v1.0/stations`

  * Return a json list of stations from the dataset.

* `/api/v1.0/tobs`

  * Return a json list of Temperature Observations (tobs) for the previous year

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Return a json list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

  * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.

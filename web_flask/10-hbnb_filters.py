#!/usr/bin/python3
"""
This script starts a Flask web application with routes for displaying State objects and their associated City objects.

Routes:
    /hbnb_filters: Display an HTML page with AirBnB filters and data loaded from the database
"""

from flask import Flask, render_template, teardown_appcontext
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)

@app.teardown_appcontext
def close_storage(exception):
    """ Remove the current SQLAlchemy Session after each request """
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def display_hbnb_filters():
    """ Display the AirBnB filters page with data loaded from the database """
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

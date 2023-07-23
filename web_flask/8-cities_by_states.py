#!/usr/bin/python3
"""
This script starts a Flask web application with routes for displaying State objects and their associated City objects.

Routes:
    /cities_by_states: Display a list of all State objects and their linked City objects.

Make sure you have the setup_mysql_dev.sql and all tables created in your AirBnB_clone_v2 repository.
"""

from flask import Flask, render_template, teardown_appcontext
from models import storage
from models.state import State

app = Flak(__name__)

@app.teardown_appcontext
def close_storage(exception):
    """ Remove the current SQLAlchemy Session after each request """
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """ Display a list of all State objects and their linked City objects """
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

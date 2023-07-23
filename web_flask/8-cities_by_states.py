#!/usr/bin/python3
"""
A Flask web app for displaying State objects and their City objects.

Routes:
    /cities_by_states: Displays all State objects and their linked City objects
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

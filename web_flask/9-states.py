#!/usr/bin/python3
"""
This script starts a Flask web application with routes for displaying State objects and their associated City objects.

Routes:
    /states: Display a list of all State objects present in FileStorage sorted by name
   /states/<id>: Display a specific State object and its linked City objects (if available). 
"""

from flask import Flask, render_template, teardown_appcontext
from models import storage
from models.state import State
from models.city import City

app = Flak(__name__)

@app.teardown_appcontext
def close_storage(exception):
    """ Remove the current SQLAlchemy Session after each request """
    storage.close()

@app.route('/states', strict_slashes=False)
def display_states():
    """ Display a list of all State objects present in FileStorage sorted by name """
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def display_state_cities(id):
    """ Display a specific State object and its linked City objects (if available) """
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda c: c.name)
        return render_template('9-states_cities.html', state=state, cities=cities)
    else:
        return render_template('9-not_found.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

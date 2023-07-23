#!/usr/bin/python3
"""
This script starts a Flask web application with routes for displaying State objects.

Routes:
    /states_list: Display a list of all State objects from the storage.
"""

from flask import Flask, render_template, teardown_appcontext
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close_storage(exception):
    """ Remove the current SQLAlchemy Session after each request"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """Displays a list of all State objects from the storage"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

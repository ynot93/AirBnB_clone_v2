#!/usr/bin/python3
"""
Displays a list of all states.

"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.teardown_appcontext
def clean_up(exception=None):
    """
    Performs clean up tasks e.g closing DB connection.

    """
    storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Lists all state objects with associated cities.

    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

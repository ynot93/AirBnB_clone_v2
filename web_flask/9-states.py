#!/usr/bin/python3
"""
Script to start a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Display a list of states

    """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """
    Display cities associated with a state

    """
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', state=state, mode='one')
    else:
        return render_template('9-states.html')


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the database connection after each request

    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


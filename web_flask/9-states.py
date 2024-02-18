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

@app.route('/states', strict_slashes=False)
def list_states():
    """
    Lists all state objects.

    """
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<state_id>', strict_slashes=False)
def list_cities(id):
    """
    Lists cities of a given state.

    """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-not_found.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

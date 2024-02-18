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

@app.route('/states_list', strict_slashes=False)
def get_states():
    """
    Lists all state objects present in the DB.

    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

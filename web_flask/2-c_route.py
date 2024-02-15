#!/usr/bin/python3
"""
Starts a Flask web app with host as 0.0.0.0 and
on port 5000.

"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Display Hello HBNB!

    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Display HBNB

    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """
    Display dynamic variable on route

    """
    text = text.replace('_', ' ')	
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

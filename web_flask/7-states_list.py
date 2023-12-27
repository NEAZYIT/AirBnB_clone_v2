#!/usr/bin/python3
""" Starts a Flask web application """

import os
import sys
import logging
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

# Set up the logger
logging.basicConfig(level=logging.DEBUG)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.

    States are sorted by name.
    """
    states = storage.all(State)

    # Log the retrieved states
    logging.debug(f"Retrieved states: {states}")

    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")

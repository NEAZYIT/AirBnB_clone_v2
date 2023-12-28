#!/usr/bin/python3
""" Starts a Flask web application """

import os
import sys
import logging
from flask import Flask, render_template
from models import storage
from models.state import State

# Adding the parent directory to the path
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states', methods=['GET'])
def cities_by_states():
    states = storage.all(State)
    print(type(states))
    sorted_states = sorted(states.values(), key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

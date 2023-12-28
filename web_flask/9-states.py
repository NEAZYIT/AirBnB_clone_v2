#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', methods=['GET'])
def display_states():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', methods=['GET'])
def display_state_cities(id):
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', state=state)
    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

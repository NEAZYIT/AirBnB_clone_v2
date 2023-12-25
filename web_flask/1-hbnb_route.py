#!/usr/bin/python3
"""
This script starts a Flask web application with two routes:
- '/' displays 'Hello HBNB!'
- '/hbnb' displays 'HBNB'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when accessing the root URL."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display 'HBNB' when accessing the '/hbnb' URL."""
    return 'HBNB'


if __name__ == '__main__':
    # Runs the Flask app on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)

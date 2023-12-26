#!/usr/bin/python3
"""
This script sets up a Flask web application with specific routes
including number validation and HTML templating.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    Displays 'C ' followed by the value of the text variable
    Replaces underscore (_) symbols with spaces
    """
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """
    Displays 'Python ' followed by the value of the text variable
    Replaces underscore (_) symbols with spaces
    """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def display_number(n):
    """
    Displays 'n is a number' only if n is an integer
    """
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>')
def display_number_template(n):
    """
    Renders an HTML template with the value of n inside an H1 tag
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

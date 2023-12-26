#!/usr/bin/python3
"""
This script starts a Flask web application with specific routes
and number validation.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def display_number(n):
    if isinstance(n, int):
        return f"{n} is a number"


@app.route('/number_template/<int:n>')
def display_number_template(n):
    if isinstance(n, int):
        return render_template('6-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def display_odd_or_even(n):
    if isinstance(n, int):
        odd_or_even = 'odd' if n % 2 != 0 else 'even'
        return render_template(
            '6-number_odd_or_even.html', n=n, odd_even=odd_or_even
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
""" Script that starts the Flask Web App """

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Return Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Return HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Replaces _ with spaces"""
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python', strict_slashes=False)
@app.route('python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    if text is not "is cool":
        text = text.replace('_', ' ')
    return f"Python {text}"


@app.rout('/number/<int:n', strict_slashes=False)
def is_int(n):
    """Route that prints if n is an integer"""
    if type(n) is int:
        return f"{n} is a number"
    else:
        raise TypeError


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)

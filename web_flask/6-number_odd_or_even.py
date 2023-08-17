#!/usr/bin/python3
''' Script that starts the Flask Web App'''

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def rerout():
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_fun(text):
    return ('c {}'.format(text.replace("_", " ")))


@app.route('/python', strict_slashes=False)
@app.route('python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def imanumber(n):
    """display “n is a number”, only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numbertemplate(n):
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashe=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           evenness=evenness)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)

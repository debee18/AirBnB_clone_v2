#!/usr/bin/python3
"""
Starts a Flask web application with seven routes, including rendering HTML templates.
"""

from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' when accessing the root route."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when accessing the /hbnb route."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display 'C ' followed by the value of the text variable."""
    text = escape(text).replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Display 'Python ' followed by the value of the text variable (default is 'is cool')."""
    text = escape(text).replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display 'n is a number' only if n is an integer."""
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Render an HTML template with 'Number: n' inside an H1 tag if n is an integer."""
    return render_template('6-number_odd_or_even.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Render an HTML template with 'Number: n is even|odd' inside an H1 tag if n is an integer."""
    odd_or_even = 'odd' if n % 2 != 0 else 'even'
    return render_template('6-number_odd_or_even.html', number=n, odd_or_even=odd_or_even)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


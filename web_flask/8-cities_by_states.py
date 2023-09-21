#!/usr/bin/python3
"""Flask web application to display states and their cities."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a list of states and their cities."""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    cities = storage.all(City)
    sorted_cities = sorted(cities.values(), key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=sorted_states, cities=sorted_cities)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


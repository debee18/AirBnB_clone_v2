#!/usr/bin/python3
"""Flask web application to display states and cities."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Display a list of states."""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """Display a list of cities for a specific state."""
    state = storage.get(State, id)
    if state is None:
        return render_template('9-states.html', not_found=True)
    
    cities = sorted(state.cities, key=lambda x: x.name)
    return render_template('9-states.html', state=state, cities=cities)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


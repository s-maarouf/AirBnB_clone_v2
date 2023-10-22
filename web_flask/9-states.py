#!/usr/bin/python3

"""This module listens using flask to 0.0.0.0:5000"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/python3

"""This module listens using flask to 0.0.0.0:5000"""

from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    storage.close()

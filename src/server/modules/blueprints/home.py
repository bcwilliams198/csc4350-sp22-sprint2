# pylint: disable = missing-function-docstring
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary; takes up space
"""


### IMPORTS
# third-party
from flask import Blueprint
from flask.helpers import send_from_directory

home_blueprint = Blueprint("home", __name__, static_folder="../../../client/build")


@home_blueprint.route("/home")
def home():
    return send_from_directory(home_blueprint.static_folder, "index.html")

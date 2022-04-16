# pylint: disable = missing-function-docstring
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary (maybe for polishing phase)
"""


### IMPORTS
## third-party
from flask import Blueprint, redirect, url_for
from flask_login import current_user


index_blueprint = Blueprint("index", __name__)


@index_blueprint.route("/")
def index():
    if current_user.is_authenticated:
        return redirect(url_for(""))

    return redirect(url_for("login.login"))

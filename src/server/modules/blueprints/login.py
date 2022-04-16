# pylint: disable = missing-function-docstring
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary (maybe for polishing phase)
"""


### IMPORTS
## third-party
from flask import Blueprint
from flask.helpers import send_from_directory

# from flask_login import login_user, logout_user


login_blueprint = Blueprint(
    "login", __name__, static_folder="../../../client/build", static_url_path=""
)


@login_blueprint.route("/login")
def login():
    return send_from_directory(login_blueprint.static_folder, "index.html")


@login_blueprint.route("/logout")
def logout():
    pass

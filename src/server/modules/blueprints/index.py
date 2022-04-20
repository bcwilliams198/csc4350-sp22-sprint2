# pylint: disable = missing-function-docstring
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary (maybe for polishing phase)
"""


### IMPORTS
## third-party
from flask import Blueprint, jsonify, redirect, url_for
from flask_login import current_user
from flask.helpers import send_from_directory


index_blueprint = Blueprint("index", __name__, static_folder="../../../client/build")


@index_blueprint.route("/")
def index():
    if current_user.is_authenticated:
        return send_from_directory(index_blueprint.static_folder, "index.html")
    # return send_from_directory(index_blueprint.static_folder, "index.html")
    return redirect(url_for("login.login"))


@index_blueprint.route("/get_user_info")
def get_user_info():
    user = {
        "name": current_user.name,
        "email": current_user.email,
        "picture": current_user.pic,
        # "name": "Alfonso",
        # "email": "alfonsobuzeta",
        # "picture": "alfonso.png",
    }
    return jsonify(user)

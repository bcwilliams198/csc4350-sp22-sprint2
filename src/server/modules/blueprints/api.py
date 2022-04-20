# pylint: disable = missing-function-docstring, relative-beyond-top-level, undefined-variable, wildcard-import
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary; takes up space
undefined-variable: vars (db, etc.) are defined, hidden by wildcard
wildcard-import: convenient (programmatic imports instead of static)
"""


### IMPORTS
# third-party
from flask import Blueprint, jsonify

## native
# data
from ..data.models import *  # maybe should use models instead?

# functions
from ..functions.external_apis.pokeapi import get_pokemon_data


api_blueprint = Blueprint("api", __name__, url_prefix="/api")


@api_blueprint.route("/")
def get_user(**args):
    email = args["email"]
    user = User.query.filter_by(email=email).first()
    return jsonify(user)


@api_blueprint.route("/search_pokemon")
def search_pokemon(pokemon):
    return get_pokemon_data(pokemon.lower())


# all database/API-calling routes belong here

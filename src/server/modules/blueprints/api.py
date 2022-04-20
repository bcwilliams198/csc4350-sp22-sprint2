# pylint: disable = missing-function-docstring, relative-beyond-top-level
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary; takes up space
"""


### IMPORTS
# third-party
from flask import Blueprint

# native
from ..functions.external_apis.pokeapi import get_pokemon_data


api_blueprint = Blueprint("api", __name__, url_prefix="/api")


@api_blueprint.route("/search_pokemon")
def search_pokemon(pokemon):
    return get_pokemon_data(pokemon.lower())


# all database/API-calling routes belong here

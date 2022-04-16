# pylint: disable =
"""
Disabled Pylint Warnings & Justifications:
"""

from flask import Blueprint

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

# all database/API-calling routes belong here

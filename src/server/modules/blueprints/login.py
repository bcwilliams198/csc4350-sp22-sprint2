# pylint: disable = missing-function-docstring, relative-beyond-top-level
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary; takes up space
relative-beyond-top-level: pylint doesn't seem to like relative imports
"""


### IMPORTS
# third-party
from flask import Blueprint, jsonify, request
from flask.helpers import send_from_directory

# from flask_login import login_user, logout_user

# native
from ..functions.external_apis.google import get_client, get_google_provider_cfg


client = get_client()

login_blueprint = Blueprint("login", __name__, static_folder="../../../client/build")


@login_blueprint.route("/login")
def login():
    return send_from_directory(login_blueprint.static_folder, "index.html")


@login_blueprint.route("/logout")
def logout():
    pass


@login_blueprint.route("/login_request")
def login_request():
    # lacks error handling
    google_provider_cfg, error = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    # use library to construct the request for login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=f"{request.base_url}/callback",
        scope=["openid", "email", "profile"],
    )
    print(f"{request.base_url}/callback")  # need to see if the redirect URL matches
    return jsonify(request_uri)


@login_blueprint.route("/login_request/callback")
def login_request_callback():
    # complete later
    pass

# pylint: disable = missing-function-docstring, relative-beyond-top-level
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary; takes up space
relative-beyond-top-level: pylint doesn't seem to like relative imports
"""


### IMPORTS
# third-party
from flask import Blueprint, jsonify, redirect, request, url_for
from flask.helpers import send_from_directory
from flask_login import login_user, logout_user

# native
from ..functions.external_apis.google import get_google_user, get_login_request_uri
from ..functions.init.db import db, User  # rely on api to do this


login_blueprint = Blueprint("login", __name__, static_folder="../../../client/build")


@login_blueprint.route("/login")
def login():
    return send_from_directory(login_blueprint.static_folder, "index.html")


@login_blueprint.route("/logout")
def logout():
    pass


@login_blueprint.route("/login_request")
def login_request():
    base_url = request.base_url
    if base_url.startswith("http://"):
        base_url = base_url.replace("http://", "https://")

    request_uri = get_login_request_uri(base_url=base_url)
    return jsonify(request_uri)


@login_blueprint.route("/login_request/callback")
def login_request_callback():
    url = request.url
    if url.startswith("http://"):
        url = url.replace("http://", "https://")

    base_url = request.base_url
    if base_url.startswith("http://"):
        base_url = base_url.replace("http://", "https://")

    code = request.args.get("code")
    google_user = get_google_user(url=url, base_url=base_url, code=code)
    if not google_user.get("email_verified"):
        return "User email not available or not verified by Google.", 400

    email = google_user["email"]
    given_name = google_user["given_name"]
    picture = google_user["picture"]
    user = User.query.filter_by(email=email).first()  # rely on API to manage DB
    if user is None:
        user = User(email=email, name=given_name, picture=picture)
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for("index.index"))

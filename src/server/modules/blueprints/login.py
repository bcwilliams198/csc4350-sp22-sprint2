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
    # google_provider_cfg, error = get_google_provider_cfg()
    # authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    # # use library to construct the request for login and provide
    # # scopes that let you retrieve user's profile from Google
    # redirect_uri = f"{request.base_url}/callback"
    # if redirect_uri.startswith("http://"):
    #     redirect_uri = redirect_uri.replace("http://", "https://")

    # request_uri = client.prepare_request_uri(
    #     authorization_endpoint,
    #     redirect_uri=redirect_uri,
    #     scope=["openid", "email", "profile"],
    # )
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

    # Get authorization code Google sent back to you
    code = request.args.get("code")
    google_user = get_google_user(url=url, base_url=base_url, code=code)
    # print(google_user.get("email_verified"))
    if not google_user.get("email_verified"):
        return "User email not available or not verified by Google.", 400

    # user = User.query.filter_by(email=users_email).first()
    # if user is None:
    #     user = User(email=users_email, name=users_name, pic=picture)
    #     print("Adding a new user")
    #     # if not add them to db
    #     db.session.add(user)
    #     db.session.commit()

    # # Begin user session by logging the user in
    # login_user(user)

    # # Send user back to homepage
    return redirect(url_for("index"))

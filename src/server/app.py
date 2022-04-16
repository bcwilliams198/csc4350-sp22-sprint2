# pylint: disable = missing-function-docstring
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary (maybe for polishing phase)
"""


### IMPORTS
# third-party imports
from flask import Flask
from flask.helpers import send_from_directory

# native imports
from modules.data.env import HOST, PORT


### FUNCTIONS
def create_app():
    flask_app = Flask(__name__, static_folder="../client/build", static_url_path="")

    @flask_app.route("/")
    def index():
        return send_from_directory(flask_app.static_folder, "index.html")

    # before returning, collect all blueprints from the blueprints folder

    return flask_app


### MAIN PROCEDURE
if __name__ == "__main__":
    app = create_app()
    # app.run(debug=True)  # development
    app.run(host=HOST, port=PORT)  # production

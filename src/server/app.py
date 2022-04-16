# pylint: disable = missing-function-docstring, redefined-outer-name, unused-wildcard-import, wildcard-import
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary (maybe for polishing phase)
redefined-outer-name: being able to re-use parameter names is convenient
unused-wildcard-import: the imports are being used, just not explicitly
wildcard-import: using the wildcard is convenient (no need to change main file)
"""


### IMPORTS
## third-party
from flask import Flask
from flask_login import LoginManager

## native
# blueprints
from modules.blueprints.index import index_blueprint
from modules.blueprints.login import login_blueprint

# data
# from modules.data.env import HOST, PORT
from modules.data.models import *


### FUNCTIONS
def create_app():
    app = Flask(
        __name__,
        # static_folder="../client/build",
        # static_url_path=""
    )

    # before returning, collect all blueprints from the blueprints folder
    app.register_blueprint(index_blueprint)
    app.register_blueprint(login_blueprint)

    return app


def init_login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def get_user(user_id):
        return User.query.get(int(user_id))


### MAIN PROCEDURE
if __name__ == "__main__":
    app = create_app()
    init_login_manager(app)
    app.run(debug=True)  # development
    # app.run(host=HOST, port=PORT)  # production

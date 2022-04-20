# pylint: disable = missing-function-docstring, redefined-outer-name, unused-wildcard-import, wildcard-import
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary; takes up space
redefined-outer-name: being able to re-use parameter names is convenient
unused-wildcard-import: the imports are being used, just not explicitly
wildcard-import: using the wildcard is convenient (no need to change main file)
"""


### IMPORTS
## third-party
from flask import Flask
from flask_cors import CORS

## native
# data
# from modules.data.env import HOST, PORT
from .modules.data.env import HOST, PORT
from .modules.data.models import *

# functions
from .modules.functions.init.blueprints import get_blueprints
from .modules.functions.init.login_manager import init_login_manager


### FUNCTIONS
def create_app():
    app = Flask(__name__, static_folder="../client/build", static_url_path="")
    CORS(app)
    blueprints = get_blueprints()
    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app


### MAIN PROCEDURE
if __name__ == "__main__":
    app = create_app()
    init_login_manager(app)
    # init database connection maybe? unsure how modules will share it
    app.run(debug=True, host=HOST, port=PORT, ssl_context="adhoc")  # development
    # app.run(host=HOST, port=PORT)  # production

# pylint: disable = missing-function-docstring, relative-beyond-top-level
"""
D
"""

### IMPORTS
# native
from ...data.models import db


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

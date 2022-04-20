# pylint: disable = missing-function-docstring, relative-beyond-top-level
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary; takes up space
relative-beyond-top-level: pylint doesn't seem to like relative imports
"""

### IMPORTS
# native
from ...data.models import db


def init_db(app):
    db.init_app(app)
    # have to figure out where to import db from
    # with app.app_context():
    #     db.create_all()

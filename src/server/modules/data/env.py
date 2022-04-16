# pylint: disable =
"""
Disabled Pylint Warnings & Justifications:
"""

### IMPORTS
# standard
from os import getenv

# third-party
from dotenv import find_dotenv, load_dotenv


### ENVIRONMENT VARIABLES
load_dotenv(find_dotenv())  # load environment variables into scope

# Google
GOOGLE_CLIENT_ID = getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)  # probably move to different file

# Heroku
HOST = getenv("IP", "0.0.0.0")
PORT = int(getenv("PORT", "8080"))

# PostgreSQL
DATABASE_URL = getenv("DATABASE_URL")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

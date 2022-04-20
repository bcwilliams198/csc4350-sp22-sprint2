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

# Flask
APP_SECRET_KEY = getenv("APP_SECRET_KEY")

# Google
GOOGLE_CLIENT_ID = getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = getenv("GOOGLE_CLIENT_SECRET")

# Heroku
HOST = getenv("IP", "0.0.0.0")
PORT = int(getenv("PORT", "8080"))

# PostgreSQL
DATABASE_URL = getenv("DATABASE_URL")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

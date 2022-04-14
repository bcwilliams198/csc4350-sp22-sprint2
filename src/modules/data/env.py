""" Imports the .env file from os """
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


# database
DATABASE_URL = getenv("DATABASE_URL")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")

# google
GOOGLE_CLIENT_ID = getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"

# heroku
HOST = getenv("IP", "0.0.0.0")
PORT = int(getenv("PORT", "8080"))

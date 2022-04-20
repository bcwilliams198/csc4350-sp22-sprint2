# pylint: disable = missing-function-docstring, relative-beyond-top-level
"""
Disabled Pylint Warnings & Justifications:
missing-function-docstring: useful, but not necessary; takes up space
relative-beyond-top-level: pylint doesn't seem to like relative imports
"""


### IMPORTS
# third-party
from oauthlib.oauth2 import WebApplicationClient
from requests import get

# native
from ...data.env import GOOGLE_CLIENT_ID


GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)  # probably move to different file


def get_client():
    return WebApplicationClient(GOOGLE_CLIENT_ID)


def get_google_provider_cfg():
    data, error = None, None
    response = get(GOOGLE_DISCOVERY_URL)
    # modularize error handling later
    if response.status_code == 200:
        data = response.json()
    else:
        error = response.text

    return data, error

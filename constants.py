from dotenv import load_dotenv
from os import environ
from typing import Text

load_dotenv()

TOKEN: Text = environ.get("TOKEN")

COLOUR_MAIN: int = 0xFFF
COLOUR_GOOD: int = 0xFFF
COLOUR_NEUTRAL: int = 0xFFF
COLOUR_BAD: int = 0xFFF

DBENDPOINT: Text = ""
DBUSER: Text = ""
DBPASS: Text = ""
DBNAME: Text = ""
DBPORT: int = 3306

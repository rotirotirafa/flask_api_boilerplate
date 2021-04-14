import os

from decouple import config

ABSOLUTE_PATH = os.path.abspath(__file__)

ROOT = os.path.dirname(ABSOLUTE_PATH)

BASE_DIR = os.path.dirname(ROOT)

DEBUG = config("DEBUG", default=False, cast=bool)

HOST = config("HOST", default="0.0.0.0")
PORT = config("PORT", default=8010, cast=int)

ENVIRONMENT = config("ENVIRONMENT", default="development")

BASE_PATH = config("BASE_PATH")

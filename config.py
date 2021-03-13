import os
import random
import string

from decouple import config


BASE_DIR = os.path.abspath('.')

DEBUG = True

SECRET_KEY = 'teste'

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rafael_rotiroti:123456@127.0.0.1:5432/crud'

SQLALCHEMY_TRACK_MODIFICATIONS = True

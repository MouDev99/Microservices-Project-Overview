import os
from dotenv import load_dotenv

load_dotenv()

class Configuration():
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
POSTGRES_URI = os.getenv("POSTGRES_URI")

class Config():
    TG_API_TOKEN = os.getenv("TG_API_TOKEN")
    SECRET_KEY = API_KEY
    SQLALCHEMY_DATABASE_URI = POSTGRES_URI
    UPLOAD_FOLDER = 'images'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

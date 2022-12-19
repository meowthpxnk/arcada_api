import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
POSTGRES_URI = os.getenv("POSTGRES_URI")

class Config():
    SECRET_KEY = API_KEY
    SQLALCHEMY_DATABASE_URI = POSTGRES_URI
    UPLOAD_FOLDER = 'images'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


if __name__ == '__main__':
    print(API_KEY)
    print(POSTGRES_URI)

from app import socket
from app import app
from app import db
import os

from app import tg_bot

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run()
        # app.run(port = 5050)

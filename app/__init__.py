import os

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.console.console_logs import ConsoleLogs

app = Flask(__name__)

app.config.from_object('app.config.Config')
socket = SocketIO(app, cors_allowed_origins="*")


app_ctx = app.app_context()
app_ctx.push()

host = "127.0.0.1"
port = 5000

db = SQLAlchemy(app)

Migrate(app, db)
from app import views, models, socket_views

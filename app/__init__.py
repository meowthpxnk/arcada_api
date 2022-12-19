import os

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from app.console.console_logs import ConsoleLogs


app = Flask(__name__)

CORS(app)
cors = CORS(app, resources = {
    r"/*":{
        "origins": "*"
    }
})

app.config.from_object('app.config.Config')
socket = SocketIO(app, cors_allowed_origins="*")

app_ctx = app.app_context()
app_ctx.push()

db = SQLAlchemy(app)

Migrate(app, db)
from app import views, models, socket_views

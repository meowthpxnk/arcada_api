import json
import time
import os

from flask import send_from_directory, url_for, send_file, request

from app import app
from app import db

basedir = os.path.abspath(os.path.dirname(""))

@app.route('/images/banners/<filename>', methods=['GET'])
def getBanner(filename):
    try:
        return send_file(os.path.join(basedir, app.config["UPLOAD_FOLDER"], "banners", filename))
    except:
        return {"error": "NOT_FOUND_FILE"}


@app.route('/images/dishes/<filename>', methods=['GET'])
def getDishImage(filename):
    try:
        return send_file(os.path.join(basedir, app.config["UPLOAD_FOLDER"], "dishes", filename))
    except:
        return {"error": "NOT_FOUND_FILE"}


@app.route('/images/restaurant/<filename>', methods=['GET'])
def getRestaurantImage(filename):
    try:
        return send_file(os.path.join(basedir, app.config["UPLOAD_FOLDER"], "restaurant", filename))
    except:
        return {"error": "NOT_FOUND_FILE"}


@app.route('/images/dish-icons/<filename>', methods=['GET'])
def getDishIconImage(filename):
    try:
        return send_file(os.path.join(basedir, app.config["UPLOAD_FOLDER"], "dishes-icons", filename))
    except:
        return {"error": "NOT_FOUND_FILE"}

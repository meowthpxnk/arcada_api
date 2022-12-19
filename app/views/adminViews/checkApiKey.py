from app import app
from app import db
from app.models.Restaurant import Restaurant

from app.methods import checkAPIkey as checkAPIkeyMethod

import json
import time
from flask import request



@app.route('/dashboard/checkApiKey', methods=['POST'])
def checkAPIkey():
    data = request.json
    verification = checkAPIkeyMethod(data["API_KEY"])

    return {"ok": True, "result": verification["ok"]}

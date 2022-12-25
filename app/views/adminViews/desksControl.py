import json
import time

from flask import request

from app import app

from app.methods import checkAPIkey
from app.methods.qr import createDeskDashboard as method_createDesk
from app.methods.qr import deleteDeskDashboard as method_deleteDesk

@app.route('/dashboard/createDesk/<restaurant_id>', methods=['POST'])
def createDesk(restaurant_id):

    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": False, "error": verification["error"]}

    try:
        data = request.json
        desk_number = data["desk_number"]
        result = method_createDesk(restaurant_id, desk_number)
    except Exception as e:
        return {"ok": False, "error": e}

    return {
        "ok": True,
        "result": result,
    }

@app.route('/dashboard/deleteDesk/', methods=['POST'])
def deleteDesk():

    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": False, "error": verification["error"]}

    try:
        data = request.json
        desk_key = data["desk_key"]
        result = method_deleteDesk(desk_key)
    except Exception as e:
        return {"ok": False, "error": e}

    return {
        "ok": True,
    }

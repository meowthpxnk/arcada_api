import json
import time

from flask import request

from app import app
from app.methods.qr import changeTurnOfQrMenu as method_changeTurnOfQrMenu
from app.methods.qr import changeTelegramChannel as method_changeTelegramChannel

from app.methods import checkAPIkey

@app.route('/dashboard/changeTurnOfQrMenu/<restaurant_id>', methods=['POST'])
def changeTurnOfQrMenu(restaurant_id):

    verification = checkAPIkey(request.args.get("API_KEY"))
    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    try:
        result = method_changeTurnOfQrMenu(restaurant_id)
    except Exception as e:
        return {"ok": False, "error": e}
    return {"ok": True, "result": result}

@app.route('/dashboard/changeTelegramChannel/<restaurant_id>', methods=['POST'])
def changeTelegramChannel(restaurant_id):

    verification = checkAPIkey(request.args.get("API_KEY"))
    if verification["ok"] == False:
        return {"ok": False, "error": verification["error"]}


    try:
        data = request.json
        telegram_channel_id = data["telegram_channel_id"]
        result = method_changeTelegramChannel(restaurant_id, telegram_channel_id)
    except Exception as e:
        return {"ok": False, "error": e}
    return {"ok": True, "result": result}

from app import app
from app import db
from app import socket

from app.models.Order import Order

from app.methods import checkAPIkey
from flask import request
from app.methods import orderSetPaid as orderSetPaidMethod

@app.route('/orderSetPaid/<id>', methods=['PUT'])
def orderSetPaid(id):
    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    orderSetPaidMethod(id)
    return {"ok": True}

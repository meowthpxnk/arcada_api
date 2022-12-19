from app import app
from app import db
from app import socket

from app.models.Order import Order

from app.methods import checkAPIkey
from flask import request

from app.methods import orderSetDelivered as OrderSetDeliveredMethod


@app.route('/orderSetDelivered/<id>', methods=['PUT'])
def orderSetDelivered(id):
    verification = checkAPIkey(request.args.get("API_KEY"))
    
    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    orderSetDeliveredMethod(id)
    return {"ok": True}

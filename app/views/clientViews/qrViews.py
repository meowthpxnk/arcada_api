from flask import request
import json

from app import app
from app.methods.qr import registerPrivateKey as method_registerPrivateKey
from app.methods.qr import checkPrivateKey as method_checkPrivateKey
from app.methods.qr import sendOrder as method_sendOrder
from app.methods.qr import callTheWaiter as method_callTheWaiter
from app.methods.qr import verificationPrivateKey as method_verificationPrivateKey



@app.route('/qrMenu/registerPrivateKey/', methods=['POST'])
def registerPrivateKey():
    try:
        data = request.json
        desk_key = data["desk_key"]
        result = method_registerPrivateKey(desk_key)
    except Exception as e:
        return {"ok": False, "error": f"{e}"}

    return {"ok": True, "result": result}


@app.route('/qrMenu/checkPrivateKey/', methods=['GET'])
def checkPrivateKey():
    try:
        private_key = request.args.get('private_key')
        restaurant_link = request.args.get('restaurant_link')
        result = method_checkPrivateKey(private_key, restaurant_link)
    except Exception as e:
        return {"ok": False, "error": f"{e}"}
    return {"ok": True, "result": result}


@app.route('/qrMenu/sendOrder/', methods=['POST'])
def sendOrder():

    try:
        data = request.json
        private_key = data["private_key"]
        order_info = data["order_info"]
        result = method_sendOrder(private_key, order_info)
    except Exception as e:
        return {"ok": False, "error": f"{e}"}


    print("ВСЕ УСПЕШНО!!!")
    return {"ok": True, "result": result}


@app.route('/qrMenu/callTheWaiter/', methods=['POST'])
def callTheWaiter():
    try:
        data = request.json
        private_key = data["private_key"]
        result = method_callTheWaiter(private_key)
    except Exception as e:
        return {"ok": False, "error": f"{e}"}
    return {"ok": True, "result": result}


@app.route('/qrMenu/verificationPrivateKey/', methods=['GET'])
def verificationPrivateKey():
    try:
        private_key = request.args.get('private_key')
        desk_key = request.args.get('desk_key')
        result = method_verificationPrivateKey(private_key, desk_key)
    except Exception as e:
        return {"ok": False, "error": f"{e}"}
    return {"ok": True, "result": result}

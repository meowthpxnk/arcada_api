from flask import request

from app import app
from app.methods import createOrder as createOrderMethod
from app.console.console_logs import ConsoleLogs, serverDecorator



@app.route('/createOrder', methods=['POST'])
def createOrder():
    data = request.json
    responce = createOrderMethod(data["dump"])
    responce["order_pay_url"] = 'https://www.tinkoff.ru/'
    print(responce)

    return {"ok": True, "dump": responce}

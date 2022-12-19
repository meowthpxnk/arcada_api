from flask import request

from app import app
from app.methods import getOrder as getOrderMethod

@app.route('/getOrder/<id>', methods=['GET'])
def getOrder(id):
    secret_key = request.args.get('secret_key')
    if (secret_key):
        order = getOrderMethod(id, secret_key)

        if(order != "error_secret_key"):
            return {"ok": True, "dump": order}

        return {
            "ok": True,
            "dump": {
                "error": "NOT_VALID_SECRET_KEY"
                }
            }

    return {"ok": True, "dump": {"error": "NOT_EXISTED_SECRET_KEY"}}

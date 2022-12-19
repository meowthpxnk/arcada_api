from flask import request

from app import app
from app.console.console_logs import ConsoleLogs, serverDecorator
from app.methods import orderSetPaid as orderSetPaidMethod

from app import db
from app.models.Order import Order


def payOrderAfterGettingMethod(order_id, secret_key):
    order = db.session.query(Order).filter(Order.id == order_id).first()
    order.isPaidAfterGetted = True
    db.session.commit()

    if (secret_key != order.secret_key):
        return 'error_secret_key'

    orderSetPaidMethod(order_id)


@app.route('/payOrderAfterGetting/<order_id>', methods=['PUT'])
def payOrderAfterGetting(order_id):
    secret_key = request.args.get('secret_key')

    if (secret_key):
        order = payOrderAfterGettingMethod(order_id, secret_key)

        if(order != "error_secret_key"):
            return {"ok": True, "dump": order}

        return {
            "ok": True,
            "dump": {
                "error": "NOT_VALID_SECRET_KEY"
                }
            }

    return {"ok": True, "dump": {"error": "NOT_EXISTED_SECRET_KEY"}}

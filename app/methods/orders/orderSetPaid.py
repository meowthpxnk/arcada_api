from app import db
from app import socket
from app.models.Order import Order
from app.methods import getUTCTime

def orderSetPaid(id):

    now_time = getUTCTime()
    now_time = (now_time['hour']*60)+now_time['minute']+(10*60)
    if now_time > 1439:
        now_time -= 1440

    order  = db.session.query(Order).filter(Order.id == id).first()

    order.paidTime = now_time
    db.session.commit()

    order.setPaid()

    socket.emit("change_order_status", {
        "order_id": id,
        "status": "WAIT_FOR_DELIVERY",
        "paid_time": now_time,
    }, namespace='/order')

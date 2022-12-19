from app import db
from app import socket
from app.models.Order import Order

def orderSetDelivered(id):
    order  = db.session.query(Order).filter(Order.id == id).first()

    order.setDelivered()

    socket.emit("change_order_status", {
        "order_id": id,
        "status": "DELIVERED"
    }, namespace='/order')

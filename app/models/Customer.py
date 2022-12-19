from app import db
from . import Order


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    phone = db.Column(db.String)
    address = db.relationship('Address', backref='Customer', uselist=False)
    orders = db.relationship('Order', backref='Customer')

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


    def createOrder(self):
        order = Order.Order(self.id)
        return order.id

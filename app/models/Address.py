from app import db
from . import Dish

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)

    def __init__(self, coordinates, customer_id):
        self.longitude = coordinates["longitude"]
        self.latitude = coordinates["latitude"]
        self.customer_id = customer_id

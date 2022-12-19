from app import db

class OrderDish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))
    counter = db.Column(db.Integer)


    def __init__(self, order_id, dish_id, counter):
        self.order_id = order_id
        self.dish_id = dish_id
        self.counter = counter

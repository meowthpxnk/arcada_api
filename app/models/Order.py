from app import db
from . import Dish
from app.methods import getUTCTime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    comment = db.Column(db.String)
    delivery_type = db.Column(db.String)
    delivery_fee = db.Column(db.Integer)
    dishes = db.relationship('OrderDish', backref='Order')
    status = db.Column(db.String)
    secret_key = db.Column(db.String)
    isPaidAfterGetted = db.Column(db.Boolean, default=False)
    paidTime = db.Column(db.Integer)
    delivery_time = db.Column(db.String)

    def __init__(self, customer_id, restaurant_id, comment, delivery_type, delivery_time, secret_key):
        self.customer_id = customer_id
        self.restaurant_id = restaurant_id
        self.comment = comment
        self.delivery_type = delivery_type
        self.secret_key = secret_key
        self.status = "WAIT_FOR_DELIVERY"
        now_time = getUTCTime()
        now_time = (now_time['hour']*60)+now_time['minute']+(10*60)
        if now_time > 1439:
            now_time -= 1440
        self.paidTime = now_time
        self.delivery_fee = 0
        self.delivery_time = delivery_time
        # db.session.add(self)
        # db.session.commit()

    def addDish(self, dish_id):
        dish = db.session.query(Dish.Dish).filter(Dish.Dish.id == dish_id).first()
        self.dishes.append(dish)

    def setPaid(self):
        self.status = "WAIT_FOR_DELIVERY"
        db.session.commit()

    def setDelivered(self):
        self.status = "DELIVERED"
        db.session.commit()

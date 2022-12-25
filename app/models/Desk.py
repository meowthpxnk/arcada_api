import string
import random

from datetime import datetime, timezone

from app import db
from app.models.Restaurant import Restaurant

from app.settings import Settings

order_delta = Settings.DESK_DELTA

class Desk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    key = db.Column(db.String, unique=True)
    call_the_waiter_time = db.Column(db.DateTime)

    private_keys = db.relationship('DeskPrivateKey', backref='Desk')

    def __init__(self, number, restaurant_id):

        if self.isExisted(number, restaurant_id):
            raise 'Already exists'

        restaurant = Restaurant.findById(restaurant_id)

        self.number = number
        self.restaurant_id = restaurant.id
        self.call_the_waiter_time = datetime.now(timezone.utc).replace(tzinfo=None)

        while True:
            try:
                self.key = self.generateKey()
                break
            except:
                continue

        db.session.add(self)
        db.session.commit()

    def getSecondsFromCall(self):
        now = datetime.now(timezone.utc).replace(tzinfo=None)
        return (now - self.call_the_waiter_time).seconds

    def getSecondsFromCallWithDelta(self):
        return order_delta - self.getSecondsFromCall()


    def callTheWaiter(self):
        self.call_the_waiter_time = datetime.now(timezone.utc).replace(tzinfo=None)
        db.session.commit()

    def tryCallTheWaiter(self):
        if self.canCallTheWaiter(self.getSecondsFromCall()):
            raise "Too fast call the waiter"
        return

    def create(restaurant):
        ...

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def getInfo(self):
        return {
            "number": self.number,
            "key": self.key,
        }

    @classmethod
    def findByKey(cls, key):
        desk = db.session.query(cls).filter(cls.key == key).first()
        if not desk:
            raise "Not exist"

        return desk

    @classmethod
    def isExisted(cls, number, restaurant_id):
        if db.session.query(cls).filter(cls.number == number, cls.restaurant_id == restaurant_id).first():
            return True
        return False

    @staticmethod
    def generateKey(size=6, chars=string.ascii_uppercase+string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def canCallTheWaiter(second_from_call, delta=order_delta):
        return not second_from_call > delta

    @staticmethod
    def getDelta():
        return order_delta

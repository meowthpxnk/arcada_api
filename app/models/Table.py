import string
import random

from datetime import datetime, timezone

from app import db
from app.models.Restaurant import Restaurant

delta = 119

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    key = db.Column(db.String, unique=True)
    call_the_waiter_time = db.Column(db.DateTime)

    categories = db.relationship('TablePrivateKey', backref='Table')

    def __init__(self, number, restaurant_id):

        if self.isExisted(number, restaurant_id):
            raise 'Already exists'

        restaurant = Restaurant.findById(restaurant_id)

        self.number = number
        self.restaurant_id = restaurant.id
        self.call_the_waiter_time = datetime.now(timezone.utc)

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
        return delta - self.getSecondsFromCall()


    def callTheWaiter(self):
        if self.canCallTheWaiter(self.getSecondsFromCall()):
            raise "Too fast call the waiter"
        self.call_the_waiter_time = datetime.now(timezone.utc)
        db.session.commit()

    def create(restaurant):
        ...

    def delete(self):
        db.session.delete(self)

    @classmethod
    def findByKey(cls, key):
        table = db.session.query(cls).filter(cls.key == key).first()
        if not table:
            raise "Not exist"

        return table

    @classmethod
    def isExisted(cls, number, restaurant_id):
        if db.session.query(cls).filter(cls.number == number, cls.restaurant_id == restaurant_id).first():
            return True
        return False

    @staticmethod
    def generateKey(size=6, chars=string.ascii_uppercase+string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def canCallTheWaiter(second_from_call, delta=delta):
        return not second_from_call > delta

    @staticmethod
    def getDelta():
        return delta

import string
import random

from datetime import datetime, timezone

from app import db
from app.models.Desk import Desk

class DeskPrivateKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desk_id = db.Column(db.Integer, db.ForeignKey('desk.id'))
    created_time = db.Column(db.DateTime)
    private_key = db.Column(db.String)

    def __init__(self, desk_key):
        desk = Desk.findByKey(desk_key)
        self.desk_id = desk.id
        self.created_time = datetime.now(timezone.utc)

        while True:
            try:
                self.private_key = self.generateKey()
                break
            except:
                continue

        db.session.add(self)
        db.session.commit()

    def isActive(self):
        return self.calculateTime(self.created_time)


    @classmethod
    def getByPrivateKey(cls, private_key):
        object = db.session.query(cls).filter(cls.private_key == private_key).first()
        if not object:
            raise "Not exist"
        return object

    @staticmethod
    def generateKey(size=16, chars=string.ascii_letters+string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def calculateTime(time, delta=600):
        now = datetime.now(timezone.utc).replace(tzinfo=None)
        print(now)
        return (now - time).seconds < delta

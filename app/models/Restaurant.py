from app import db
from app.methods import parseTitle

class Restaurant(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    link = db.Column(db.String, unique=True)

    logo = db.Column(db.String)
    start_work = db.Column(db.Integer)
    end_work = db.Column(db.Integer)
    color = db.Column(db.String)
    banner = db.Column(db.String)

    delivery_fee = db.Column(db.Integer)
    free_delivery_price = db.Column(db.Integer)

    telegram_channel = db.Column(db.String)

    categories = db.relationship('Category', backref='Restaurant')
    orders = db.relationship('Order', backref='Restaurant')
    desks = db.relationship('Desk', backref='Restaurant')

    is_online = db.Column(db.Boolean, default=False)
    is_online_qr_menu = db.Column(db.Boolean, default=False)

    def __init__(self, restaurant):

        self.title = restaurant["title"]
        self.link = restaurant["link"]

        if "logo" in restaurant:
            self.logo = restaurant["logo"]

        if "start_work" in restaurant:
            self.start_work = restaurant["start_work"]

        if "end_work" in restaurant:
            self.end_work = restaurant["end_work"]

        if "color" in restaurant:
            self.color = restaurant["color"]

        if "delivery_fee" in restaurant:
            self.delivery_fee = restaurant["delivery_fee"]

        if "price_for_free_delivery" in restaurant:
            self.free_delivery_price = restaurant["price_for_free_delivery"]

        db.session.add(self)
        db.session.commit()

    def getInfo(self):

        return {
            "title": self.title,
            "link": self.link,
            "color": self.color,
            "start_work": self.start_work,
            "end_work": self.end_work,
            "logo": self.logo,
            "is_online": self.is_online,
            "id": self.id,
            "banner": self.banner,
            "free_delivery_price": self.free_delivery_price,
            "delivery_fee": self.delivery_fee,
            "is_online_qr_menu": self.is_online_qr_menu,
            "telegram_channel": self.telegram_channel,
            "desks": [desk.getInfo() for desk in self.desks]
        }

    def create(restaurant):
        try:
            restaurant = Restaurant(restaurant)
        except:
            return{"restaurant": restaurant,"error": "ALREADY_EXISTED"}
        return restaurant

    def setLogo(self,logo):
        self.logo = logo
        db.session.commit()

    def setBanner(self,banner):
        self.banner = banner
        db.session.commit()

    def deleteBanner(self):
        self.banner = None
        db.session.commit()

    def changeTurnOfQrMenu(self):
        self.is_online_qr_menu = not self.is_online_qr_menu
        db.session.commit()

    def changeTelegramId(self, telegram_channel_id):
        self.telegram_channel = telegram_channel_id
        db.session.commit()

    # def enableQrMenu(self):
    #     self.is_online_qr_menu = True
    #     db.session.commit()
    #
    # def disableQrMenu(self):
    #     self.is_online_qr_menu = False
    #     db.session.commit()

    def edit(self, restaurant):

        if "title" in restaurant:
            self.title = restaurant["title"]

        if "logo" in restaurant:
            self.logo = restaurant["logo"]

        if "start_work" in restaurant:
            self.start_work = restaurant["start_work"]

        if "end_work" in restaurant:
            self.end_work = restaurant["end_work"]

        if "color" in restaurant:
            self.color = restaurant["color"]

        print(restaurant)

        if "free_delivery_price" in restaurant:
            self.free_delivery_price = restaurant["free_delivery_price"]

        if "delivery_fee" in restaurant:
            self.delivery_fee = restaurant["delivery_fee"]

        db.session.commit()

    def delete(self):
        for category in self.categories:
            category.delete()

        db.session.delete(self)
        db.session.commit()

    @classmethod
    def findById(cls, id):
        restaurant = db.session.query(cls).filter(cls.id == id).first()
        if not restaurant:
            raise "Not exist"
        return restaurant

    @classmethod
    def findByLink(cls, link):
        restaurant = db.session.query(cls).filter(cls.link == link).first()
        if not restaurant:
            raise "Not exist"
        return restaurant

from app import db
from app.methods import parseTitle

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    logo = db.Column(db.String)
    dishes = db.relationship('Dish', backref='Category')
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))


    def __init__(self, category):
        self.title = category["title"]
        self.restaurant_id = category["restaurant_id"]

        if "logo" in category:
            self.logo = category["logo"]

        db.session.add(self)
        db.session.commit()

    def create(category):
        isExisted = db.session.query(Category).filter(
            (Category.title == category["title"]) &
            (Category.restaurant_id == category["restaurant_id"])
        ).first()
        print(isExisted)

        if isExisted:
            return{"category": category,"error": "ALREADY_EXISTED"}

        category = Category(category)

        return category


    def getInfo(self):
        return{
            "id": self.id,
            "title": self.title,
            "restaurant_id": self.restaurant_id,
            "logo": self.logo,
        }

    def edit(self, category):
        if "title" in category:
            self.title = category["title"]

        if "logo" in category:
            self.logo = category["logo"]

        db.session.commit()

    def delete(self):
        for dish in self.dishes:
            dish.delete()
        self.restaurant_id = None
        db.session.commit()

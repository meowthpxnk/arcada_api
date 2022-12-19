from app import db
from .DishIngredient import dish_ingredient
from app.methods import parseTitle

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True)

    def __init__(self, title):

        check = db.session.query(Ingredient).filter(Ingredient.title == title).all()

        if len(check) == 0:
            self.title = title

            db.session.add(self)
            db.session.commit()

    def create(title):

        title = parseTitle(title)

        ingredient = Ingredient(title)

        if ingredient.id == None:
            ingredient = db.session.query(Ingredient).filter(Ingredient.title == title).first()

        return ingredient

    def getInfo(self):
        return self.title

from app import db
from .DishIngredient import dish_ingredient
from app.methods import parseTitle

class Dish(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String)
    price = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    photo = db.Column(db.String)
    description = db.Column(db.String)
    full_title = db.Column(db.String)
    portion = db.Column(db.String)


    is_full_menu = db.Column(db.Boolean, default = True)


    ingredients = db.relationship('Ingredient', secondary=dish_ingredient, backref='Dish')

    orders = db.relationship('OrderDish', backref='Dish')

    def __init__(self, dish):
        self.title = dish["title"]
        self.price = dish["price"]
        self.category_id = dish["category_id"]
        self.is_full_menu = dish["is_full_menu"]

        if "photo" in dish:
            self.photo = dish["photo"]

        if "description" in dish:
            self.description = dish["description"]

        if "portion" in dish:
            self.portion = dish["portion"]

        if "full_title" in dish:
            self.full_title = dish["full_title"]

        db.session.add(self)
        db.session.commit()

    def uploadPhoto(self, photoURL):
        self.photo = photoURL
        db.session.commit()

    def setPortion(self, portion):
        self.portion = portion
        db.session.commit()

    def setFullTitle(self, full_title):
        self.full_title = full_title
        db.session.commit()

    def setDescription(self, description):
        self.description = description
        db.session.commit()

    def setCategory(self, category_id):
        self.category_id = category_id
        db.session.commit()

    def setPrice(self, price):
        self.price = price
        db.session.commit()

    def getIngredients(self):
        ingredients = []

        for ingredient in self.ingredients:
            ingredients.append(ingredient.title)

        return ingredients

    def create(dish):
        isExisted = db.session.query(Dish).filter(
            (Dish.title == dish["title"]) &
            (Dish.category_id == dish["category_id"])
        ).first()
        print(isExisted)

        if isExisted:
            return {"dish": dish,"error": "ALREADY_EXISTED"}

        dish = Dish(dish)

        return dish

    def getInfo(self):

        dish = {
            "title": self.title,
            "id": self.id,
            "category_id": self.category_id,
            "photo": self.photo,
            "description": self.description,
            "full_title": self.full_title,
            "portion": self.portion,
            "ingredients": self.getIngredients(),
            "price": self.price,
            "is_full_menu": self.is_full_menu,
        }

        return dish

    def edit(self, dish):

        if "title" in dish:
            self.title = dish["title"]

        if "price" in dish:
            self.price = dish["price"]

        if "photo" in dish:
            self.photo = dish["photo"]

        if "description" in dish:
            self.description = dish["description"]

        if "portion" in dish:
            self.portion = dish["portion"]

        if "full_title" in dish:
            self.full_title = dish["full_title"]

        if "is_full_menu" in dish:
            self.is_full_menu = dish["is_full_menu"]

        db.session.commit()

    def delete(self):
        self.category_id = None
        db.session.commit()

    @classmethod
    def findById(cls, id):
        dish = db.session.query(cls).filter(cls.id == id).first()
        if not dish:
            raise "Not exist"
        return dish

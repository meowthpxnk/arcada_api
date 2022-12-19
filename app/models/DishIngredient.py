from app import db

dish_ingredient = db.Table('dish_ingredient',
    db.Column('dish_id', db.Integer, db.ForeignKey('dish.id')),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id')),
)

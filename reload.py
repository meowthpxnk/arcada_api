from app.models.Dish import Dish
from app import db

dishes = db.session.query(Dish).all()

for dish in dishes:
    dish.is_full_menu = False

db.session.commit()

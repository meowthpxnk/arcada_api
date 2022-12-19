from app import db
from app.models.Restaurant import Restaurant


def isExistedRestaurant(restaurant_id):
    restaurant = db.session.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

    if restaurant:
        return True
    else:
        return False
    return False

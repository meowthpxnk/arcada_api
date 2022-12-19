from app.models.Restaurant import Restaurant
from app import db

def changeTurnOfRestaurant(id):
    restaurant = db.session.query(Restaurant).filter(Restaurant.id == id).first()

    errors = {}

    if restaurant.is_online:
        restaurant.is_online = False
        db.session.commit()
        return {"result": "SUCCESS", "restaurant": restaurant.getInfo()}


    if not restaurant.color:
        errors["color"] = "NOT_EXISTED"

    if not restaurant.logo:
        errors["logo"] = "NOT_EXISTED"

    if not restaurant.start_work:
        errors["start_work"] = "NOT_EXISTED"

    if not restaurant.end_work:
        errors["end_work"] = "NOT_EXISTED"

    categories = restaurant.categories

    if not len(categories):
        errors["categories"] = "NOT_EXISTED"

    error_dishes_flag = False

    for category in categories:
        if len(category.dishes):
            error_dishes_flag = True
            break

    if not error_dishes_flag:
        errors["dishes"] = "NOT_EXISTED"


    if errors == {}:
        restaurant.is_online = True
        db.session.commit()
        return {"result": "SUCCESS", "restaurant": restaurant.getInfo()}



    return {"result": "ERROR", "errors": errors}

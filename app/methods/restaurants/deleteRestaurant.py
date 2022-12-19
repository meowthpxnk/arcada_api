from app.models.Restaurant import Restaurant
from PIL import Image
from app.settings import Settings

from app import db
from app.methods import isHexColorValid, allowedFile, fileSave, isPathValid

def deleteRestaurant(restaurant):
    errors = {}

    if "id" not in restaurant:
        errors["id"] = "NOT_EXISTED"


    restaurant_info = restaurant

    if errors == {}:


        restaurantGet = db.session.query(Restaurant).filter(Restaurant.id == restaurant["id"]).first()

        if restaurantGet != None:
            restaurantGet.delete()
        else:
            errors["main"] = "NOT_EXISTED"
            restaurant_info = restaurant


    return {"restaurant": restaurant_info, "errors": errors}

from app.models.Restaurant import Restaurant
from app import db

def deleteBannerToRestaurant(restaurant):
    errors = {}

    if "id" not in restaurant:
        errors["id"] = "NOT_EXISTED"


    restaurant_info = restaurant

    if errors == {}:


        restaurantGet = db.session.query(Restaurant).filter(Restaurant.id == restaurant["id"]).first()

        if restaurantGet != None:
            restaurantGet.deleteBanner()
            restaurant_info = restaurantGet.getInfo()
        else:
            errors["main"] = "NOT_EXISTED"
            restaurant_info = restaurant


    return {"restaurant": restaurant_info, "errors": errors}

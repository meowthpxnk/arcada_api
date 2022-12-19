from app.models.Restaurant import Restaurant
from PIL import Image
from app.settings import Settings

from app import db
from app.methods import isHexColorValid, allowedFile, fileSave, isPathValid

def createRestaurant(restaurant, logo):
    errors = {}

    if "title" not in restaurant:
        errors["title"] = "NOT_EXISTED"


    if "delivery_fee" not in restaurant:
        errors["delivery_fee"] = "NOT_EXISTED"

    if "price_for_free_delivery" not in restaurant:
        errors["price_for_free_delivery"] = "NOT_EXISTED"

    if "link" not in restaurant:
        errors["link"] = "NOT_EXISTED"
    else:
        if isPathValid(restaurant["link"]) != True:
            errors["link"] = "NOT_VALID_PATH"


    if "color" in restaurant:
        if isHexColorValid(restaurant["color"]) == False:
            errors["color"] = "NOT_VALID_FORMAT"

    if "start_work" in restaurant:
        if restaurant["start_work"] < 0 or restaurant["start_work"] >= 1440:
            errors["start_work"] = "NOT_VALID_TIME_CODE"

    if "end_work" in restaurant:
        if restaurant["end_work"] < 0 or restaurant["end_work"] >= 1440:
            errors["end_work"] = "NOT_VALID_TIME_CODE"

    logo_flag = False
    if logo:
        if allowedFile(logo.filename, {'png'}):
            logo_flag = True
        else:
            errors["logo"]  = "NOT_VALID_EXTENTION"
            logo_flag = False

    if logo_flag:
        logo = Image.open(logo)
        if logo.size[0] != logo.size[1] or logo.size[0] > 512:
            logo_flag = False
            errors["logo"]  = "NOT_VALID_SIZE"


    restaurant_info = restaurant

    if errors == {}:


        restaurant = Restaurant.create(restaurant)


        try:
            restaurant_info = restaurant.getInfo()

            if logo_flag:
                path = fileSave(logo, 'restaurant', f'{restaurant.id}.png')
                restaurant.setLogo(path)

            restaurant_info = restaurant.getInfo()

        except:
            errors["main"] = restaurant["error"]
            restaurant_info = restaurant["restaurant"]

    return {"restaurant": restaurant_info, "errors": errors}

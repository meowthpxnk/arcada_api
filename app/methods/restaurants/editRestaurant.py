from app.models.Restaurant import Restaurant
from PIL import Image
from app.settings import Settings

from app import db
from app.methods import isHexColorValid, allowedFile, fileSave, isPathValid

def editRestaurant(restaurant, logo):
    errors = {}

    if "id" not in restaurant:
        errors["id"] = "NOT_EXISTED"

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
        if allowedFile(logo.filename, Settings.VALID_EXTENTIONS_FOR_REST_LOGO):
            logo_flag = True
        else:
            errors["logo"]  = "NOT_VALID_EXTENTION"
            logo_flag = False


    if logo_flag:
        logo = Image.open(logo)
        if logo.size[0] != logo.size[1] or logo.size[0] > Settings.VALID_SIZE_FOR_REST_LOGO:
            logo_flag = False
            errors["logo"]  = "NOT_VALID_SIZE"


    restaurant_info = restaurant

    print(logo)

    if errors == {}:


        restaurantGet = db.session.query(Restaurant).filter(Restaurant.id == restaurant["id"]).first()

        if restaurantGet != None:
            if logo_flag:
                path = fileSave(logo, 'restaurant', f'{restaurantGet.id}.png')
                print(f'{path}')
                restaurantGet.setLogo(path)

            restaurantGet.edit(restaurant)
            restaurant_info = restaurantGet.getInfo()
        else:
            errors["main"] = "NOT_EXISTED"
            restaurant_info = restaurant


    return {"restaurant": restaurant_info, "errors": errors}

from PIL import Image

from app.models.Restaurant import Restaurant
from app.settings import Settings

from app import db
from app.methods import isHexColorValid, allowedFile, fileSave, isPathValid

def setBannerToRestaurant(restaurant, banner):
    errors = {}

    if "id" not in restaurant:
        errors["id"] = "NOT_EXISTED"


    banner_flag = False
    if banner:
        if allowedFile(banner.filename, Settings.VALID_EXTENTIONS_FOR_REST_BANNER):
            banner_flag = True
        else:
            errors["banner"]  = "NOT_VALID_EXTENTION"
            banner_flag = False


    if banner_flag:
        banner = Image.open(banner)
        if banner.size[0] != Settings.VALID_SIZE_FOR_REST_BANNER[0] or banner.size[1] != Settings.VALID_SIZE_FOR_REST_BANNER[1]:
            banner_flag = False
            errors["banner"]  = "NOT_VALID_SIZE"


    restaurant_info = restaurant

    print(banner)

    if errors == {}:


        restaurantGet = db.session.query(Restaurant).filter(Restaurant.id == restaurant["id"]).first()

        if restaurantGet != None:
            if banner_flag:
                path = fileSave(banner, 'banners', f'{restaurantGet.id}.png')
                print(f'{path}')
                restaurantGet.setBanner(path)

            restaurantGet.edit(restaurant)
            restaurant_info = restaurantGet.getInfo()
        else:
            errors["main"] = "NOT_EXISTED"
            restaurant_info = restaurant


    return {"restaurant": restaurant_info, "errors": errors}

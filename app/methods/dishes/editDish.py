from PIL import Image

from app.models.Dish import Dish
from app import db
from app.settings import Settings

from app.methods.categories import isExistedCategory
from app.methods.restaurants import isExistedRestaurant
from app.methods.ingredients import changeIngrList

from app.methods import allowedFile, fileSave


def editDish(dish, photo):
    errors = {}

    if "id" not in dish:
        errors["id"] = "NOT_EXISTED"

    if "category_id" not in dish:
        errors["category_id"] = "NOT_EXISTED"
    else:
        if isExistedCategory(dish["category_id"]) == False:
            errors["category_id"] = "NOT_EXISTED_CATEGORY_ID"

    if "ingredients" in dish and not isinstance(dish["ingredients"], list):
        errors["ingredients"] = "NOT_VALID_FORMAT"

    photo_flag = False
    if photo:
        if allowedFile(
            photo.filename,
            Settings.VALID_EXTENTIONS_FOR_DISH_PHOTO
        ):
            photo_flag = True
        else:
            errors["photo"]  = "NOT_VALID_EXTENTION"
            photo_flag = False


    if photo_flag:
        photo = Image.open(photo)
        valid_size = Settings.VALID_SIZE_FOR_DISH_PHOTO
        if photo.size[0] > valid_size[0] or photo.size[1] > valid_size[1]:
            photo_flag = False
            errors["photo"]  = "NOT_VALID_SIZE"




    dish_info = dish

    if errors == {}:

        dish_ingredients = None

        if "ingredients" in dish:
            dish_ingredients = dish["ingredients"]


        dishGet = db.session.query(Dish).filter(
            (Dish.id == dish["id"]) &
            (Dish.category_id == dish["category_id"])
        ).first()


        if dishGet != None:
            print(dishGet.ingredients)
            dishGet.edit(dish)
            if photo_flag:
                save_extention = Settings.SAVE_EXTENTION_FOR_DISH_PHOTO
                path = fileSave(photo, 'dishes', f'{dishGet.id}.{save_extention}')

                dishGet.uploadPhoto(path)


            if dish_ingredients:
                changeIngrList(dishGet.id, dish_ingredients)
            dish_info = dishGet.getInfo()
        else:
            errors["main"] = "NOT_EXISTED"
            dish_info = dish


    return {"dish": dish_info, "errors": errors}

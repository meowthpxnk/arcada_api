from PIL import Image
from app import db
from app.settings import Settings

from app.models.Dish import Dish
from app.models.Ingredient import Ingredient

from app.methods.categories import isExistedCategory
from app.methods.restaurants import isExistedRestaurant

from app.methods import allowedFile, fileSave

def createDish(dish, photo):
    errors = {}

    if "category_id" not in dish:
        errors["category_id"] = "NOT_EXISTED"
    else:
        if isExistedCategory(dish["category_id"]) == False:
            errors["category_id"] = "NOT_EXISTED_CATEGORY_ID"


    if "title" not in dish:
        errors["title"] = "NOT_EXISTED"

    if "price" not in dish:
        errors["price"] = "NOT_EXISTED"
    else:
        if isinstance(dish["price"], int) == False:
            errors["price"] = "NOT_VALID_FORMAT"

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

        dish = Dish.create(dish)

        try:
            dish_info = dish.getInfo()


            if photo_flag:
                save_extention = Settings.SAVE_EXTENTION_FOR_DISH_PHOTO
                path = fileSave(photo, 'dishes', f'{dish.id}.{save_extention}')

                dish.uploadPhoto(path)


            if dish_ingredients:
                for ingredient in dish_ingredients:
                    ingredient_dump = Ingredient.create(ingredient)

                    dish.ingredients.append(ingredient_dump)
                    db.session.commit()



            dish_info = dish.getInfo()

        except:
            errors["main"] = dish["error"]
            dish_info = dish["dish"]

        # print(dish_info)


    return {"dish": dish_info, "errors": errors}

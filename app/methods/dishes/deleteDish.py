from PIL import Image

from app.models.Dish import Dish
from app import db
from app.settings import Settings

from app.methods.categories import isExistedCategory
from app.methods.restaurants import isExistedRestaurant
from app.methods.ingredients import changeIngrList

from app.methods import allowedFile, fileSave


def deleteDish(dish):
    errors = {}

    if "id" not in dish:
        errors["id"] = "NOT_EXISTED"

    if "category_id" not in dish:
        errors["category_id"] = "NOT_EXISTED"
    else:
        if isExistedCategory(dish["category_id"]) == False:
            errors["category_id"] = "NOT_EXISTED_CATEGORY_ID"


    dish_info = dish


    if errors == {}:

        dishGet = db.session.query(Dish).filter(
            (Dish.id == dish["id"]) &
            (Dish.category_id == dish["category_id"])
        ).first()


        if dishGet != None:
            dishGet.delete()
        else:
            errors["main"] = "NOT_EXISTED"
            dish_info = dish


    return {"dish": dish_info, "errors": errors}

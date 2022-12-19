from app.models.Category import Category
from app import db
from app.methods.restaurants import isExistedRestaurant

def createCategory(category):
    errors = {}
    category_info = category

    if "title" not in category:
        errors["title"] = "NOT_EXISTED"

    if "restaurant_id" not in category:
        errors["restaurant_id"] = "NOT_EXISTED"
    else:
        if isExistedRestaurant(category["restaurant_id"]) == False:
            errors["restaurant_id"] = "NOT_EXISTED_RESTAURANT_ID"

    if errors == {}:
        category = Category.create(category)

        try:
            category_info = category.getInfo()

        except:
            errors["main"] = category["error"]
            category_info = category["category"]

    return {"category": category_info, "errors": errors}

from app.models.Category import Category
from app import db
from app.methods.restaurants import isExistedRestaurant

def deleteCategory(category):
    errors = {}
    category_info = category

    if "id" not in category:
        errors["id"] = "NOT_EXISTED"

    if "restaurant_id" not in category:
        errors["restaurant_id"] = "NOT_EXISTED"
    else:
        if isExistedRestaurant(category["restaurant_id"]) == False:
            errors["restaurant_id"] = "NOT_EXISTED_RESTAURANT_ID"

    if errors == {}:
        categoryGet = db.session.query(Category).filter(
            (Category.id == category["id"]) &
            (Category.restaurant_id == category["restaurant_id"])
        ).first()

        if categoryGet != None:
            categoryGet.delete()
        else:
            errors["main"] = "NOT_EXISTED"
            category_info = category


    return {"category": category_info, "errors": errors}

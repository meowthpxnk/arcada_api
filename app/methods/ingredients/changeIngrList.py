from app import db
from app.models.Dish import Dish
from app.models.Ingredient import Ingredient
from app.methods import parseArrayOfTitles

def changeIngrList(dish_id, new_ingredient_list):

    # FIND DISH VIA ID
    dish = db.session.query(Dish).filter(Dish.id == dish_id).first()
    if dish == None:
        return {"error": "DISH_NOT_EXISTED"}

    new_ingredient_list = parseArrayOfTitles(new_ingredient_list)
    old_ingredient_list = dish.ingredients


    # DELETE OLD INACTIVE INGREDIENTS
    deleted_ingredients = []

    for ingredient in old_ingredient_list:
        title = ingredient.getInfo()
        print(ingredient)
        if (title in new_ingredient_list) != True:
            deleted_ingredients.append(ingredient)

    for ingredient in deleted_ingredients:
        dish.ingredients.remove(ingredient)
        db.session.commit()

    # APPEND NEW ACTIVE INGREDIENTS
    changed_ingredient_list = dish.getIngredients()

    for ingredient in new_ingredient_list:
        ingredient_dump = Ingredient.create(ingredient)

        if not ingredient in changed_ingredient_list:
            dish.ingredients.append(ingredient_dump)

        db.session.commit()



    return dish.getIngredients()

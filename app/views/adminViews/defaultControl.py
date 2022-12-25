import json
import time

from flask import request

from app import app
from app import db
from app.models.Restaurant import Restaurant

from app.methods import createDish as createDishMethod
from app.methods import editDish as editDishMethod
from app.methods import createCategory as createCategoryMethod
from app.methods import editCategory as editCategoryMethod
from app.methods import checkAPIkey
from app.methods import getMenu as getMenuMethod

@app.route('/dashboard/getRestaurants', methods=['GET'])
def getDashboardRestaurants():
    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    restaurants  = db.session.query(Restaurant).all()

    return {
        "ok": True,
        "restaurants": [restaurant.getInfo() for restaurant in restaurants]
    }

@app.route('/dashboard/getMenu/<restaurant_id>', methods=['GET'])
def getDashboardMenu(restaurant_id):
    verification = checkAPIkey(request.args.get("API_KEY"))
    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    restaurant  = db.session.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

    menu = {
        "dishes": [],
        "categories": [],
    }

    desks = [desk.getInfo() for desk in restaurant.desks]
    telegram_channel = restaurant.telegram_channel
    enabled_qr_menu = restaurant.is_online_qr_menu

    for category in restaurant.categories:
        menu["categories"].append(category.getInfo())
        for dish in category.dishes:
            menu["dishes"].append(dish.getInfo())

    return {
        "ok": True,
        "menu": menu,
        "desks": desks,
        "telegram_channel": telegram_channel,
        "enabled_qr_menu": enabled_qr_menu
    }

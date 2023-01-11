import json
import time

from flask import request

from app import app

from app.methods import createRestaurant as createRestaurantMethod
from app.methods import editRestaurant as editRestaurantMethod
from app.methods import changeTurnOfRestaurant as changeTurnOfRestaurantMethod
from app.methods import deleteRestaurant as deleteRestaurantMethod
from app.methods import setBannerToRestaurant as setBannerToRestaurantMethod
from app.methods import deleteBannerToRestaurant as deleteBannerToRestaurantMethod

from app.methods import changeTelegramAdmin as method_changeTelegramAdmin

from app.methods import checkAPIkey



@app.route('/dashboard/deleteRestaurant/<id>', methods=['POST'])
def deleteRestaurant(id):
    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    dump = deleteRestaurantMethod({"id": id})

    return {"ok": True, "dump": dump}

@app.route('/dashboard/changeTurnOfRestaurant/<id>', methods=['POST'])
def changeTurnOfRestaurant(id):

    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    dump = changeTurnOfRestaurantMethod(id)

    return {"ok": True, "dump": dump}


@app.route('/dashboard/createRestaurant', methods=['POST'])
def createRestaurant():

    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}


    try:
        logo = request.files["logo"]
    except:
        logo = None

    restaurant = json.loads(request.form["restaurant"])

    restaurant = createRestaurantMethod(restaurant, logo)


    return {"ok": True, "restaurant": restaurant}

@app.route('/dashboard/editRestaurant', methods=['POST'])
def editRestaurant():

    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    try:
        logo = request.files["logo"]
        print(f'{logo}')
    except:
        logo = None
        print(f'{logo}')

    restaurant = json.loads(request.form["restaurant"])

    restaurant = editRestaurantMethod(restaurant, logo)



    return {"ok": True, "restaurant": restaurant}



@app.route('/dashboard/setBannerToRestaurant', methods=['POST'])
def setBannerToRestaurant():

    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    try:
        banner = request.files["banner"]
    except:
        banner = None

    restaurant = json.loads(request.form["restaurant"])

    restaurant = setBannerToRestaurantMethod(restaurant, banner)



    return {"ok": True, "restaurant": restaurant}


@app.route('/dashboard/deleteBannerToRestaurant', methods=['POST'])
def deleteBannerToRestaurant():

    verification = checkAPIkey(request.args.get("API_KEY"))

    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    restaurant = json.loads(request.form["restaurant"])

    restaurant = deleteBannerToRestaurantMethod(restaurant)


    return {"ok": True, "restaurant": restaurant}



@app.route('/dashboard/changeTelegramAdmin/<restaurant_id>', methods=['POST'])
def changeTelegramAdmin(restaurant_id):

    verification = checkAPIkey(request.args.get("API_KEY"))
    if verification["ok"] == False:
        return {"ok": False, "error": verification["error"]}

    print("------GET_INFO-------")
    print(request)
    print(request.json)
    print("------GET_INFO-------")


    try:
        data = request.json
        telegram_admin_id = data["telegram_admin_id"]
        result = method_changeTelegramAdmin(restaurant_id, telegram_admin_id)
    except Exception as e:
        return {"ok": False, "error": f"{e}"}
    return {"ok": True, "result": result}

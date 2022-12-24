import json
import time

from flask import request

from app import app

from app.methods import checkAPIkey

from app.methods import getMenu as getMenuMethod




### |-------| DISH CONTROL |-------| ###

from app.methods import createDish as createDishMethod

@app.route('/dashboard/createDish', methods=['POST'])
def createDish():

    verification = checkAPIkey(request.args.get("API_KEY"))
    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    try:
        photo = request.files["photo"]
    except:
        photo = None

    dish = json.loads(request.form["dish"])
    dish = createDishMethod(dish, photo)
    return {"ok": True, "dish": dish}



from app.methods import editDish as editDishMethod

@app.route('/dashboard/editDish', methods=['POST'])
def editDish():

    verification = checkAPIkey(request.args.get("API_KEY"))
    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    try:
        photo = request.files["photo"]
    except:
        photo = None

    dish = json.loads(request.form["dish"])
    dish = editDishMethod(dish, photo)
    return {"ok": True, "dish": dish}



from app.methods import deleteDish as deleteDishMethod

@app.route('/dashboard/deleteDish', methods=['POST'])
def deleteDish():
    verification = checkAPIkey(request.args.get("API_KEY"))
    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    data = request.json

    dish = data["dish"]
    dish = deleteDishMethod(dish)

    return {"ok": True, "dish": dish}



### |-------| CATEGORIES CONTROL |-------| ###

from app.methods import createCategory as createCategoryMethod

@app.route('/dashboard/createCategory', methods=['POST'])
def createCategory():

    verification = checkAPIkey(request.args.get("API_KEY"))
    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    category = json.loads(request.form["category"])
    category = createCategoryMethod(category)
    return {"ok": True, "category": category}



from app.methods import editCategory as editCategoryMethod

@app.route('/dashboard/editCategory', methods=['POST'])
def editCategory():

    verification = checkAPIkey(request.args.get("API_KEY"))
    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    category = json.loads(request.form["category"])
    category = editCategoryMethod(category)
    return {"ok": True, "category": category}



from app.methods import deleteCategory as deleteCategoryMethod

@app.route('/dashboard/deleteCategory', methods=['POST'])
def deleteCategory():

    verification = checkAPIkey(request.args.get("API_KEY"))
    if verification["ok"] == False:
        return {"ok": True, "error": verification["error"]}

    data = request.json

    category = data["category"]
    category = deleteCategoryMethod(category)
    return {"ok": True, "category": category}

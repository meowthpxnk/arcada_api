from flask import request

from app import app
from app.methods import getRestaurants as getRestaurantsMethod


@app.route('/getRestaurants', methods=['GET'])
def getRestaurants():
    dump_object = getRestaurantsMethod()
    return {"ok": True, "dump": dump_object}

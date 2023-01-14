from flask import request

from app import app
from app.methods import getMenu as getMenuMethod
from app.methods import getQrMenu as getQrMenuMethod
from app.console.console_logs import ConsoleLogs, serverDecorator

@app.route('/getMenu/<restaurant_link>', methods=['GET'])
def getMenu(restaurant_link):

    ConsoleLogs.PRINT(f"Get menu via link: {restaurant_link}")

    dump_object = getMenuMethod(restaurant_link)
    return {"ok": True, "dump": dump_object}

@app.route('/getQrMenu/<restaurant_link>', methods=['GET'])
def getQrMenu(restaurant_link):

    ConsoleLogs.PRINT(f"Get menu via link: {restaurant_link}")

    dump_object = getQrMenuMethod(restaurant_link)
    # print(dump_object)
    return {"ok": True, "dump": dump_object}

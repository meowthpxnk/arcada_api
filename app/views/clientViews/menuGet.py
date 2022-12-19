from flask import request

from app import app
from app.methods import getMenu as getMenuMethod
from app.console.console_logs import ConsoleLogs, serverDecorator

@app.route('/getMenu/<restaurant_link>', methods=['GET'])
@serverDecorator("GET_MENU")
def getMenu(restaurant_link):

    ConsoleLogs.PRINT(f"Get menu via link: {restaurant_link}")

    dump_object = getMenuMethod(restaurant_link)
    return {"ok": True, "dump": dump_object}

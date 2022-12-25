from app import db
from app.models.Desk import Desk
from app.methods import parseOrderCart
from app.models.DeskPrivateKey import DeskPrivateKey
from app import tg_bot

from app.parse_messages.qr_messages import parseOrderMessage, parseCallWaiterMessage


def sendOrder(private_key, order_info):

    private_key = DeskPrivateKey.getByPrivateKey(private_key)
    desk = private_key.Desk
    restaurant = desk.Restaurant

    restaurant_chat_id = restaurant.telegram_channel

    try:
        private_key.tryCreateOrder()
    except:
        return {"status": "TOO_MANY_REQUESTS", "waiting_time": private_key.waiting_time()}

    if restaurant_chat_id == "" or restaurant_chat_id == None:
        raise Exception("SEND_ERROR")

    cart = parseOrderCart(order_info['cart'])
    name = order_info['name']
    comment = order_info['comment']
    desk_number = desk.number

    message = parseOrderMessage(desk_number, name, cart, comment)
    # print(message)
    # responce = {}

    try:
        responce = tg_bot.sendMessage(chat_id = restaurant_chat_id, text = message)
        if not responce["ok"]:
            raise Exception("SEND_ERROR")
    except:
        raise Exception("SEND_ERROR")

    private_key.createOrder()

    return {"status": "SEND"}

def callTheWaiter(private_key):
    private_key = DeskPrivateKey.getByPrivateKey(private_key)
    desk = private_key.Desk
    restaurant = desk.Restaurant

    restaurant_chat_id = restaurant.telegram_channel

    if restaurant_chat_id == "" or restaurant_chat_id == None:
        raise Exception("SEND_ERROR")

    try:
        desk.tryCallTheWaiter()
    except:
        waiting_time = desk.getSecondsFromCallWithDelta()
        return {"status": "WAIT_ERROR", "waiting_time": waiting_time}

    message = parseCallWaiterMessage(desk.number)

    try:
        responce = tg_bot.sendMessage(chat_id = restaurant_chat_id, text = message)
        if not responce["ok"]:
            raise Exception("SEND_ERROR")
    except:
        return {"status": "SEND_ERROR"}

    desk.callTheWaiter()

    return {"status": "SUCCESS", "delta": desk.getDelta()}

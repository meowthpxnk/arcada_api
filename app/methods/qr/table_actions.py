from app.models.Table import Table
from app.methods import parseOrderCart
from app.models.TablePrivateKey import TablePrivateKey
from app import tg_bot

from app.parse_messages.qr_messages import parseOrderMessage, parseCallWaiterMessage


def sendOrder(private_key, order_info):

    private_key = TablePrivateKey.getByPrivateKey(private_key)
    table = private_key.Table
    restaurant = table.Restaurant

    restaurant_chat_id = restaurant.telegram_channel

    if restaurant_chat_id == "" or restaurant_chat_id == None:
        raise Exception("SEND_ERROR")

    cart = parseOrderCart(order_info['cart'])
    name = order_info['name']
    comment = order_info['comment']
    table_number = table.number

    message = parseOrderMessage(table_number, name, cart, comment)
    # print(message)
    # responce = {}

    try:
        responce = tg_bot.sendMessage(chat_id = restaurant_chat_id, text = message)
        if not responce["ok"]:
            raise Exception("SEND_ERROR")
    except:
        raise Exception("SEND_ERROR")


    return {"status": "SEND"}

def callTheWaiter(private_key):
    private_key = TablePrivateKey.getByPrivateKey(private_key)
    table = private_key.Table
    restaurant = table.Restaurant

    restaurant_chat_id = restaurant.telegram_channel

    if restaurant_chat_id == "" or restaurant_chat_id == None:
        raise Exception("SEND_ERROR")

    try:
        table.callTheWaiter()
    except:
        waiting_time = table.getSecondsFromCallWithDelta()
        return {"status": "WAIT_ERROR", "waiting_time": waiting_time}

    message = parseCallWaiterMessage(table.number)

    try:
        responce = tg_bot.sendMessage(chat_id = restaurant_chat_id, text = message)
        if not responce["ok"]:
            raise Exception("SEND_ERROR")
    except:
        return {"status": "SEND_ERROR"}

    return {"status": "SUCCESS", "delta": Table.getDelta()}

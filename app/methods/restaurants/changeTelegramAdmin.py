from app.models.Restaurant import Restaurant

from app import tg_bot



def changeTelegramAdmin(restaurant_id, telegram_admin_id):
    restaurant = Restaurant.findById(restaurant_id)

    if not restaurant:
        raise Exception("Not existed restaurant")

    try:
        responce = tg_bot.sendMessage(chat_id = telegram_admin_id, text = "test message")
        if not responce["ok"]:
            raise Exception("SEND_ERROR")
    except:
        raise Exception("SEND_ERROR")

    restaurant.changeTelegramAdminId(telegram_admin_id)

    return restaurant_id

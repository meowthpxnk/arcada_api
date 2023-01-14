from app.models.Restaurant import Restaurant

from app import tg_bot



def changeTelegramAdmin(restaurant_id, telegram_admin_id):
    restaurant = Restaurant.findById(restaurant_id)

    if not restaurant:
        raise Exception("Not existed restaurant")

    try:
        tg_bot.send_message(chat_id = telegram_admin_id, text = "Тестовое сообщение", parse_mode = "HTML")
    except:
        raise Exception("SEND_ERROR")

    restaurant.changeTelegramAdminId(telegram_admin_id)

    return restaurant_id

from app.models.Restaurant import Restaurant
from app.models.Desk import Desk

def changeTurnOfQrMenu(restaurant_id):
    restaurant = Restaurant.findById(restaurant_id)

    if not restaurant:
        raise Exception("Not existed restaurant")

    restaurant.changeTurnOfQrMenu()

    return restaurant_id

def changeTelegramChannel(restaurant_id, telegram_channel_id):
    restaurant = Restaurant.findById(restaurant_id)

    if not restaurant:
        raise Exception("Not existed restaurant")

    restaurant.changeTelegramId(telegram_channel_id)

    return restaurant_id

def createDeskDashboard(restaurant_id, desk_number):
    desk = Desk(desk_number, restaurant_id)
    return {"key": desk.key}

def deleteDeskDashboard(desk_key):
    desk = Desk.findByKey(desk_key)
    desk.delete()
    return

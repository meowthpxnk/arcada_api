from app import db
from app.models.Restaurant import Restaurant
from app.methods.additional import parseTitle


def getRestaurantViaLink(restaurant_link):
    restaurant_link = parseTitle(restaurant_link)
    return db.session.query(Restaurant).filter((Restaurant.link == restaurant_link) & (Restaurant.is_online)).first()


def getQrRestaurantViaLink(restaurant_link):
    restaurant_link = parseTitle(restaurant_link)
    return db.session.query(Restaurant).filter((Restaurant.link == restaurant_link) & (Restaurant.is_online_qr_menu)).first()

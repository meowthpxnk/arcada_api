from app import db

from app.methods.restaurants import getRestaurantViaLink
from app.models.Restaurant import Restaurant

from app.methods.additional import isPathValid

def getRestaurants():
    restaurants_dump = []

    restaurants = db.session.query(Restaurant).filter(Restaurant.is_online).all()


    for restaurant in restaurants:

        restaurants_dump.append(restaurant.getInfo())

    return restaurants_dump




def getBannersViaRestaurant(restaurant_id):
    banners = []
    restaurants = db.session.query(Restaurant).filter((Restaurant.id != restaurant_id) & (Restaurant.is_online)).all()

    for restaurant in restaurants:

        if restaurant.banner != None:
            banners.append({
                "link": restaurant.link,
                "banner": restaurant.banner,
            })

    return banners

def getAnotherRestaurants(restaurant_id):
    restaurants_dump = []

    restaurants = db.session.query(Restaurant).filter((Restaurant.id != restaurant_id) & (Restaurant.is_online)).all()

    for restaurant in restaurants:
        restaurants_dump.append(restaurant.getInfo())

    return restaurants_dump


def getMenu(restaurant_link):


    if not isPathValid(restaurant_link):
        return {"error": "PATH_NOT_VALID"}

    restaurant = getRestaurantViaLink(restaurant_link)

    if restaurant == None:
        return {"error" : "RESTAURANT_NOT_EXISTED"}

    banners = getBannersViaRestaurant(restaurant.id)

    another_restaurants = getAnotherRestaurants(restaurant.id)

    dump_object = {
        "restaurant" : {},
        "categories" : [],
        "dishes": [],
        "banners": banners,
        "another_restaurants": another_restaurants,
    }

    dump_object["restaurant"] = restaurant.getInfo()

    for category in restaurant.categories:
        dump_object["categories"].append(category.getInfo())

        for dish in category.dishes:
            dump_object["dishes"].append(dish.getInfo())


    return dump_object

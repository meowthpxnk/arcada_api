from app import db
from app.models.Order import Order
from app.models.Dish import Dish
from app.models.Customer import Customer
from app.models.Address import Address
from app.models.Restaurant import Restaurant
from app.models.Dish import Dish
from app.models.OrderDish import OrderDish
from app.methods import getAnotherRestaurants


def getOrder(order_id, secret_key):
    order = db.session.query(Order).filter(Order.id == order_id).first()

    if (secret_key != order.secret_key):
        return 'error_secret_key'
    customer = order.Customer

    order_cart = []
    total_price = 0
    dishes = order.dishes
    for dish in dishes:
        total_price += dish.Dish.price * dish.counter
        order_cart.append({
            'id': dish.Dish.id,
            'counter': dish.counter,
            'title': dish.Dish.title,
            'price': dish.Dish.price,
            'image': dish.Dish.photo,
        })

    responce = {
        'order': {
            'cart': order_cart,
            'comment': order.comment,
            'delivery_type': order.delivery_type,
            'delivery_fee': order.delivery_fee,
            'status': order.status,
            'total_price': total_price,
            'delivery_time': order.delivery_time,
            'paid_time': order.paidTime,
        },
        'user_data':{
            'phone': customer.phone,
            'name': customer.name,
        },
        'restaurant_info':{
            'link': order.Restaurant.link,
            'logo': order.Restaurant.logo,
            'color': order.Restaurant.color,
            'title': order.Restaurant.title,
            'start_work': order.Restaurant.start_work,
            'end_work': order.Restaurant.end_work,
        },
        'restaurants_list': getAnotherRestaurants(order.Restaurant.id),
    }

    if order.delivery_type =="DELIVERY":
        responce['user_data']['address'] = {
            "latitude": customer.address.latitude,
            "longitude": customer.address.longitude,
        },



    return responce

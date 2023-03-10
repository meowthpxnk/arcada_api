from app import db, tg_bot
from app.models.Order import Order
from app.models.Dish import Dish
from app.models.Customer import Customer
from app.models.Address import Address
from app.models.Restaurant import Restaurant
from app.models.Dish import Dish
from app.models.OrderDish import OrderDish

from app.console import ConsoleLogs

from app.parse_messages import parseOrderCartText

from secrets import token_urlsafe as generateSecretKey

def createOrder(request):

    secret_key = generateSecretKey(16)
    try_order = db.session.query(Order).filter(Order.secret_key == secret_key).first()

    while(try_order != None):
        secret_key = generateSecretKey(16)
        try_order = db.session.query(Order).filter(Order.secret_key == secret_key).first()



    user_data = request["user_data"]
    order = request["order"]
    # order = request["order"]

    dishes = order["cart"]
    comment = order["comment"]
    delivery_type = order["delivery_type"]
    delivery_time = str(order["delivery_time"])


    restaurant_link = order["link"]

    restaurant = db.session.query(Restaurant).filter(Restaurant.link == restaurant_link).first()



    customer = Customer(user_data["name"], user_data["phone"])
    db.session.add(customer)
    db.session.commit()

    address = None
    address_text = None

    # delivery_fee = 0

    if (delivery_type == "DELIVERY"):
        address = user_data["address"]
        address = Address(address, customer.id)
        address_text = user_data["address_text"]

        db.session.add(address)
        db.session.commit()




    order = Order(customer.id, restaurant.id, comment, delivery_type, delivery_time, secret_key)


    db.session.add(order)
    db.session.commit()


    total_cart_price = 0

    for dish in dishes:
        get_dish = db.session.query(Dish).filter(Dish.id == dish["id"]).first()
        order_dish = OrderDish(order.id, get_dish.id, dish["counter"])
        db.session.add(order_dish)
        db.session.commit()

        total_cart_price += get_dish.price * dish["counter"]

    # ConsoleLogs.PRINT(f"{total_cart_price }")
    # ConsoleLogs.PRINT(f"{restaurant.free_delivery_price }")

    delivery_fee = restaurant.delivery_fee + request["order_taxes"] if ((order.delivery_type == "DELIVERY") and (total_cart_price < restaurant.free_delivery_price)) else 0
    order.delivery_fee = delivery_fee
    db.session.commit()

    restaurant_title = restaurant.title

    try:
        tg_bot.send_message(
            chat_id = restaurant.telegram_admin_id,
            text = parseOrderCartText(dishes, user_data['phone'], user_data['name'], address_text, delivery_type, delivery_time, total_cart_price + delivery_fee, comment, restaurant_title),
            parse_mode = "HTML"
        )
    except:
        raise Exception("SEND_ERROR")

    return {'order_id': order.id, 'secret_key': order.secret_key}

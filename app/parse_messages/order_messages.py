from app.models.Dish import Dish

from .text_parsers import parseTitle


def parseOrderCart(cart):
    dump = []

    for item in cart:
        print(f"{item}")
        dish = Dish.findById(item["id"])
        dump.append({
            "title": parseTitle(dish.title),
            "price": dish.price,
            "counter": item["counter"],
        })
    return dump

def parseOrderCartText(dishes, phone_number, name, address, delivery_type, delivery_time, total_amount, comment, restaurant_title):
    parsedCart = parseOrderCart(dishes)


    text = ""

    is_delivery = True if delivery_type == "DELIVERY" else False

    try:
        if delivery_type == "DELIVERY":
            if delivery_time == "DEFAULT":
                delivery_time = "Ближайшее"
            else:
                minutes = int(delivery_time)%60
                hours = int(delivery_time)//60
                delivery_time = f"{hours}:{minutes}"
    except:
        delivery_time = "Неизвестное(ошибка)"


    print(delivery_time)

    delivery_type = "Доставка" if delivery_type == "DELIVERY" else "Самовывоз"

    total_amount = str(total_amount // 100) + "." + str(total_amount % 100)

    text += f"<b>Ресторан</b>:\n{restaurant_title}\n\n"
    text += f"<b>Номер телефона</b>:\n{phone_number}\n\n"
    name = name if name != None else "-------"
    text += f"<b>Имя заказчика</b>:\n{name}\n\n"
    text += f"<b>Тип заказа</b>:\n{delivery_type}\n\n"

    if is_delivery:
        text += f"<b>Время доставки</b>:\n{delivery_time}\n\n"

    text += f"<b>Стоимость заказа</b>:\n{total_amount}\n\n"
    if address:
        text += f"<b>Адрес доставки</b>:\n{address}\n\n"

    comment = "-------" if not comment else comment
    text += f"<b>Комментарий</b>:\n{comment}\n\n"

    text += "<b>Блюда в заказе</b>\n"


    for item in parsedCart:
        text += f"{item['title']} / <b>кол-во: {item['counter']}</b>\n"

    return text

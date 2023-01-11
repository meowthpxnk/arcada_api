from app.models.Dish import Dish

def parseOrderCart(cart):
    dump = []

    for item in cart:
        dish = Dish.findById(item["id"])
        dump.append({
            "title": dish.title,
            "price": dish.price,
            "counter": item["counter"],
        })
        return dump


def parseOrderCartText(dishes, phone_number, name, address, delivery_type, total_amount, comment):
    parsedCart = parseOrderCart(dishes)


    text = ""

    delivery_type = "Доставка" if delivery_type == "DELIVERY" else "Самовывоз"

    total_amount = str(total_amount // 100) + "." + str(total_amount % 100)

    text += f"<b>Номер телефона</b>:\n{phone_number}\n\n"
    text += f"<b>Имя заказчика</b>:\n{name}\n\n"
    text += f"<b>Тип заказа</b>:\n{delivery_type}\n\n"
    text += f"<b>Стоимость заказа</b>:\n{total_amount}\n\n"
    if address:
        text += f"<b>Адрес доставки</b>:\n{address}\n\n"

    text += f"<b>Комментарий</b>:\n{comment}\n\n"

    text += "<b>Блюда в заказе</b>\n"

    for item in parsedCart:
        text += f"{item['title']}: {item['counter']}\n"

    return text

    # return "Блюда в заказе:\n\n".join("фффффффффффффффффф").join(f"{item['title']}: {item['counter']}\n" for item in parsedCart).join("aaa")
        # .join("Стоимость")

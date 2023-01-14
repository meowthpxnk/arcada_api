from .text_parsers import parseTitle

def parseOrderMessage(desk_number, name, cart, comment):
    comment = None if not comment else comment
    cart_txt = "".join(f"{parseTitle(dish['title'])} x<b>{dish['counter']}</b>\n" for dish in cart)
    text = f"<b>Заказ у стола #{desk_number}</b>\n\n<b>Имя клиента</b>:\n{name}\n\n<b>Комментарий к заказу:</b>\n{comment}\n\n<b>Блюда в заказе:</b>\n{cart_txt}"
    return text

def parseCallWaiterMessage(desk_number):
    return f"Зовут официанта за стол <b>#{desk_number}</b>"

def parseChatIdMessage(chat_id):
    return f"ID вашего канала 😀:\n{chat_id}"

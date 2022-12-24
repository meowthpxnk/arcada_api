
def parseOrderMessage(desk_number, name, cart, comment):
    cart_txt = "".join(f"{dish['title']} x{dish['counter']}\n" for dish in cart)
    # print(cart)
    # cart_txt = "sad"
    return f"Заказ у стола #{desk_number}\nИмя клиента: {name}\nКомментарий к заказу: {comment}\nБлюда в заказе:\n{cart_txt}"

def parseCallWaiterMessage(desk_number):
    return f"Зовут официанта за стол #{desk_number}"

def parseChatIdMessage(chat_id):
    return f"ID вашего канала 😀:\n{chat_id}"

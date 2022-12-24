
def parseOrderMessage(table_number, name, cart, comment):
    cart_txt = "".join(f"{dish['title']} x{dish['counter']}\n" for dish in cart)
    # print(cart)
    # cart_txt = "sad"
    return f"Заказ у стола #{table_number}\nИмя клиента: {name}\nКомментарий к заказу: {comment}\nБлюда в заказе:\n{cart_txt}"

def parseCallWaiterMessage(table_number):
    return f"Зовут официанта за стол #{table_number}"

def parseChatIdMessage(chat_id):
    return f"ID вашего канала 😀:\n{chat_id}"

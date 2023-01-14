from app import tg_bot

@tg_bot.callback_query_handler(func=lambda callback: callback.data == 'qr_accept')
def qr_accept(call):
    message = call.message
    chat = message.chat
    user = call.from_user
    tg_bot.edit_message_text(
        chat_id = chat.id,
        message_id = message.id,
        text = message.text + f"\n\n♻️<b>Заказ принял: </b>{user.username}",
        reply_markup = None,
        parse_mode = "HTML",
    )


@tg_bot.callback_query_handler(func=lambda callback: callback.data == 'qr_decline')
def qr_decline(call):
    message = call.message
    chat = message.chat
    user = call.from_user
    tg_bot.edit_message_text(
        chat_id = chat.id,
        message_id = message.id,
        text = message.text + f"\n\n❌<b>Заказ отклонил: </b>{user.username}",
        reply_markup = None,
        parse_mode = "HTML",
    )

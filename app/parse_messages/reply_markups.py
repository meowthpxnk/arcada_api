# from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# qr_request_status_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
# qr_request_status_keyboard.add(KeyboardButton('Text'))

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

qr_request_status_keyboard = InlineKeyboardMarkup() \
    .add(
        InlineKeyboardButton("✅Принять", callback_data="qr_accept"),
    )

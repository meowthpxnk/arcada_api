from app import app
from app import tg_bot
import requests
from flask import request
from app.parse_messages.qr_messages import parseChatIdMessage

@app.route('/tgBot/webHooks', methods=["POST"])
def tgBotGetHooks():
    data = request.json
    tg_bot.sendMessage(chat_id = "5693374811", text = f"DATA: {data}")
    tg_bot.sendMessage(chat_id = "5693374811", text = f"{'my_chat_member' in data = }")
    tg_bot.sendMessage(chat_id = "5693374811", text = f"{'my_chat_member' in data = }")
    if "my_chat_member" in data:
        try:
            chat_id = data["my_chat_member"]["chat"]["id"]
            text = parseChatIdMessage(chat_id)
            tg_bot.sendMessage(chat_id = id, text = text)
        except:
            return {"ok": False}

    return {"ok": True}

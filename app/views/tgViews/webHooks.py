from app import app
from app import tg_bot
import requests
from flask import request
from app.parse_messages.qr_messages import parseChatIdMessage
import json

@app.route('/tgBot/webHooks', methods=["POST"])
def tgBotGetHooks():
    data = request.json
    data_text = json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
    tg_bot.sendMessage(chat_id = "5693374811", text = f"DATA:\n{data_text}")
    if "my_chat_member" in data:
        try:
            tg_bot.sendMessage(chat_id = id, text = text)
        except:
            return {"ok": False}

    return {"ok": True}

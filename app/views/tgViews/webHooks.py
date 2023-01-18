from app import app
from app import tg_bot
import telebot
import requests
from flask import request
from app.parse_messages.qr_messages import parseChatIdMessage
import json

@app.route('/tgBot/webHooks', methods=["POST"])
def tgBotGetHooks():
    data = request.json

    if request.headers.get('content-type') == 'application/json':

        data_text = json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
        tg_bot.send_message(chat_id = "5693374811", text = f"DATA:\n{data_text}")
        
        update = telebot.types.Update.de_json(data)
        tg_bot.process_new_updates([update])
        return {"ok": True}

    return {"ok": False}

    #
    # data_text = json.dumps(data, indent=4, separators=(',', ': '), sort_keys=True)
    # tg_bot.send_message(chat_id = "5693374811", text = f"DATA:\n{data_text}")
    # if "my_chat_member" in data:
    #     try:
    #         tg_bot.send_message(chat_id = id, text = text, parse_mode = "HTML")
    #     except:
    #         return {"ok": False}
    #
    # return {"ok": True}



# if request.headers.get('content-type') == 'application/json':
#     data = request.stream.read().decode('utf-8')
#
#     update = telebot.types.Update.de_json(data)
#
#     bot.process_new_updates([update])
#     return {"ok":True}
# else:
#     return {"ok":False}

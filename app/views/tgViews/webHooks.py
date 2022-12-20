from app import app
import requests

@app.route('/tgBot/webHooks', methods=['GET'])
def tgBotGetHooks():
    token = '5855595896:AAHdnmM-u0PXDAsf0J3N5SbFJIaTIknfpC0'
    urlSend = f'https://api.telegram.org/bot{token}/sendMessage'
    data = request.json
    params = {
        'chat_id': 5693374811,
        'test': data,
    }
    requsets.get(urlSend, params=params)
    return {"ok": True}

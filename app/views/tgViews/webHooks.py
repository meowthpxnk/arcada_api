from app import app
import requests

@app.route('/tgBot/webHooks', methods=["POST"])
def tgBotGetHooks():
    token = '5855595896:AAHdnmM-u0PXDAsf0J3N5SbFJIaTIknfpC0'
    return token
    urlSend = f'https://api.telegram.org/bot{token}/sendMessage'
    data = request.json
    params = {
        'chat_id': 5693374811,
        'text': data,
    }
    requests.get(urlSend, params=params)
    print(10)
    return {"ok": True}

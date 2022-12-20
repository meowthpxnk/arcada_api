from app import app

@app.route('/tgBot/webHooks', methods=['GET'])
def tgBotGetHooks():
    return {"ok": True}

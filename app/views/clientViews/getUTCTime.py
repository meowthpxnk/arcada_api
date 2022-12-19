from flask import request

from app import app
from app.methods import getUTCTime as getUTCTimeMethod

@app.route('/getUTCTime', methods=['GET'])
def getUTCTime():
    now_utc_time = getUTCTimeMethod()
    return {"ok": True, "dump": now_utc_time}

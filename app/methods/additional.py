import re
import os

from werkzeug.utils import secure_filename
from datetime import datetime, timezone

from app.config import API_KEY
from app import app

def getUTCTime():
    now_utc = datetime.now(timezone.utc)
    return {"hour": now_utc.hour, "minute": now_utc.minute, "second": now_utc.second}

def parseTitle(title):
    title = title.lower()
    return title

def parseArrayOfTitles(array):
    dump_array = []

    for title in array:
        title = parseTitle(title)
        if not title in dump_array:
            dump_array.append(title)

    return dump_array

def checkAPIkey(key):
    if key == API_KEY:
        return {"ok": True}
    else:
        return {"ok": False, "error": "Invalid API key"}

def isPathValid(path):
    match = re.search(r'^([A-Za-z0-9_-]+)$', path)

    if match:
      return True

    else:
      return False

def isHexColorValid(color):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', color)

    if match:
      return True

    else:
      return False

def allowedFile(filename, extention):
    return ('.' in filename) and (filename.rsplit('.', 1)[1].lower() in extention)

def fileSave(file, directory, filename):

    path = os.path.join(app.config['UPLOAD_FOLDER'], directory + filename)
    path = f'images/{directory}/{filename}'
    print(path)
    file.save(path)

    return path

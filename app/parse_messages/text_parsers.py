def parseTitle(title):
    return "".join(title[letter].lower() if letter != 0 else title[letter].upper() for letter in range(len(title)))

from app.models.DeskPrivateKey import DeskPrivateKey

def registerPrivateKey(desk_key):
    private_key = DeskPrivateKey(desk_key)

    return {
        "private_key": private_key.private_key,
        "restaurant_link": private_key.Desk.Restaurant.link
    }

def checkPrivateKey(private_key, restaurant_link):
    private_key = DeskPrivateKey.getByPrivateKey(private_key)
    if not private_key.Desk.Restaurant.link == restaurant_link:
        raise "Not valid responce"

    return {
        "isActive": private_key.isActive(),
        "desk_number": private_key.Desk.number
    }


def verificationPrivateKey(private_key, desk_key):
    private_key = DeskPrivateKey.getByPrivateKey(private_key)


    if not private_key.Desk.key == desk_key:
        raise Exception("Not valid desk_key")


    if not private_key.isActive():
        raise Exception("Not active key")

    return {"restaurant_link": private_key.Desk.Restaurant.link}

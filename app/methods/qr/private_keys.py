from app.models.TablePrivateKey import TablePrivateKey

def registerPrivateKey(table_key):
    private_key = TablePrivateKey(table_key)

    return {
        "private_key": private_key.private_key,
        "restaurant_link": private_key.Table.Restaurant.link
    }

def checkPrivateKey(private_key, restaurant_link):
    private_key = TablePrivateKey.getByPrivateKey(private_key)
    if not private_key.Table.Restaurant.link == restaurant_link:
        raise "Not valid responce"

    return {
        "isActive": private_key.isActive(),
        "table_number": private_key.Table.number
    }


def verificationPrivateKey(private_key, table_key):
    private_key = TablePrivateKey.getByPrivateKey(private_key)


    if not private_key.Table.key == table_key:
        raise Exception("Not valid table_key")


    if not private_key.isActive():
        raise Exception("Not active key")

    return {"restaurant_link": private_key.Table.Restaurant.link}

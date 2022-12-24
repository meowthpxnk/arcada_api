from app.models.Dish import Dish

def parseOrderCart(cart):
    dump = []

    for item in cart:
        dish = Dish.findById(item["id"])
        dump.append({
            "title": dish.title,
            "price": dish.price,
            "counter": item["counter"],
        })
        return dump

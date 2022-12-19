from app import db
from app.models.Category import Category


def isExistedCategory(category_id):
    category = db.session.query(Category).filter(Category.id == category_id).first()

    if category:
        return True
    else:
        return False
    return False

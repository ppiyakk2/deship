from .models import User


def get_user_by_id(user_id):
    return User.select_id(user_id)


def getAllUser():
    return User.select_all()